import json
import httpx
import time
from typing import List, Optional


from .models import (
    DefinitionResponse,
    ReadSourceCodeResponse,
    ReadSourceCodeRequest,
    ReferencesResponse,
    GetDefinitionRequest,
    GetReferencesRequest,
    Symbol,
    FindIdentifierRequest,
    IdentifierResponse,
    GetReferencedSymbolsRequest,
    ReferencedSymbolsResponse,
    ReferenceWithSymbolDefinitions,
)

class Lsproxy:
    """Client for interacting with the lsproxy API."""

    def __init__(
        self,
        base_url: str = "http://localhost:4444/v1",
        timeout: float = 60.0,
        auth_token: Optional[str] = None,
    ):
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={"Content-Type": "application/json"},
            limits=httpx.Limits(max_keepalive_connections=20, max_connections=100),
        )
        headers = {"Content-Type": "application/json"}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"
        self._client.headers = headers

    def _request(self, method: str, endpoint: str, **kwargs) -> httpx.Response:
        """Make HTTP request with retry logic and better error handling."""
        try:
            response = self._client.request(method, endpoint, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                error_data = e.response.json()
                raise ValueError(error_data.get("error", str(e)))
            raise

    def definitions_in_file(self, file_path: str) -> List[Symbol]:
        """Retrieve symbols from a specific file."""
        response = self._request(
            "GET", "/symbol/definitions-in-file", params={"file_path": file_path}
        )
        symbols = [
            Symbol.model_validate(symbol_dict)
            for symbol_dict in json.loads(response.text)
        ]
        return symbols

    def find_definition(self, request: GetDefinitionRequest) -> DefinitionResponse:
        """Get the definition of a symbol at a specific position in a file."""
        if not isinstance(request, GetDefinitionRequest):
            raise TypeError(
                f"Expected GetDefinitionRequest, got {type(request).__name__}. Please use GetDefinitionRequest model to construct the request."
            )
        response = self._request(
            "POST", "/symbol/find-definition", json=request.model_dump()
        )
        definition = DefinitionResponse.model_validate_json(response.text)
        return definition

    def find_references(self, request: GetReferencesRequest) -> ReferencesResponse:
        """Find all references to a symbol."""
        if not isinstance(request, GetReferencesRequest):
            raise TypeError(
                f"Expected GetReferencesRequest, got {type(request).__name__}. Please use GetReferencesRequest model to construct the request."
            )
        response = self._request(
            "POST", "/symbol/find-references", json=request.model_dump()
        )
        references = ReferencesResponse.model_validate_json(response.text)
        return references

    def find_identifier(self, request: FindIdentifierRequest) -> IdentifierResponse:
        """Find all occurrences of an identifier by name in a file.

        Args:
            request: The request containing the identifier name, file path, and optional position.
                    If position is provided, returns exact match or closest matches.

        Returns:
            Response containing the found identifiers.
        """
        if not isinstance(request, FindIdentifierRequest):
            raise TypeError(
                f"Expected FindIdentifierRequest, got {type(request).__name__}. Please use FindIdentifierRequest model to construct the request."
            )
        response = self._request(
            "POST", "/symbol/find-identifier", json=request.model_dump()
        )
        return IdentifierResponse.model_validate_json(response.text)

    def list_files(self) -> List[str]:
        """Get a list of all files in the workspace."""
        response = self._request("GET", "/workspace/list-files")
        files = response.json()
        return files

    def read_source_code(self, request: ReadSourceCodeRequest) -> ReadSourceCodeResponse:
        """Read source code from a specified file range.
        
        Args:
            request: The request containing the file path and an optional range.
        
        Returns:
            ReadSourceCodeResponse containing the source code.
        """
        if not isinstance(request, ReadSourceCodeRequest):
            raise TypeError(
                f"Expected ReadSourceCodeRequest, got {type(request).__name__}. Please use ReadSourceCodeRequest to construct the request."
            )
        response = self._request(
            "POST", "/workspace/read-source-code", json=request.model_dump()
        )
        return ReadSourceCodeResponse.model_validate_json(response.text)

    @classmethod
    def initialize_with_modal(
        cls,
        repo_url: str,
        git_token: Optional[str] = None,
        sha: Optional[str] = None,
        timeout: Optional[int] = None,
        version: str = "0.4.0",
    ) -> "Lsproxy":
        """
        Initialize lsproxy by starting a Modal sandbox with the server and connecting to it.
        Waits up to 3 minutes for the server to be ready.

        Args:
            repo_url: Git repository URL to clone and analyze
            git_token: Optional Git personal access token for private repositories
            sha: Optional commit to checkout in the repo
            timeout: Sandbox timeout in seconds (defaults to Modal's 5-minute timeout if None)
            version: lsproxy version to use (defaults to "0.4.0")

        Returns:
            Configured Lsproxy client instance

        Raises:
            ImportError: If Modal or PyJWT are not installed
            ValueError: If repository cloning fails
        """

        try:
            from .modal import ModalSandbox
        except ImportError:
            raise ImportError(
                "Modal and PyJWT are required for this feature. "
                "Install them with: pip install 'lsproxy-sdk[modal]'"
            )


        sandbox = ModalSandbox(repo_url, git_token, sha, timeout, version)

        # Wait for server to be ready
        client = cls(base_url=f"{sandbox.tunnel_url}/v1", auth_token=sandbox.jwt_token)

        print("Waiting for server start up (make take a minute)...")
        for attempt in range(180):
            if client.check_health():
                break
            time.sleep(1)
        else:  # No break occurred - server never became healthy
            raise TimeoutError("Server did not start up within 3 minutes")

        print("Server is ready to accept connections")

        # Store sandbox reference for cleanup
        client._sandbox = sandbox

        return client

    def check_health(self) -> bool:
        """Check if the server is healthy and ready."""
        try:
            response = self._request("GET", "/system/health")
            health_data = response.json()
            return health_data.get("status") == "ok"
        except Exception:
            return False

    def find_referenced_symbols(
        self, request: GetReferencedSymbolsRequest
    ) -> ReferencedSymbolsResponse:
        """Find all symbols that are referenced from the symbol at the given position.
        
        Args:
            request: The request containing the position to analyze for referenced symbols.
            
        Returns:
            Response containing the referenced symbols categorized as:
            - workspace_symbols: Symbols found in the workspace with their definitions
            - external_symbols: Symbols that only have definitions outside the workspace  
            - not_found: Symbols where no definitions could be found
            
        Raises:
            TypeError: If the request is not a GetReferencedSymbolsRequest
            ValueError: If the server returns a 400 error
            httpx.HTTPError: For other HTTP errors
        """
        if not isinstance(request, GetReferencedSymbolsRequest):
            raise TypeError(
                f"Expected GetReferencedSymbolsRequest, got {type(request).__name__}. "
                "Please use GetReferencedSymbolsRequest model to construct the request."
            )
        
        response = self._request(
            "POST", 
            "/symbol/find-referenced-symbols", 
            json=request.model_dump()
        )
        
        return ReferencedSymbolsResponse.model_validate_json(response.text)

    def close(self):
        """Close the HTTP client and cleanup Modal resources if present."""
        self._client.close()
        if hasattr(self, "_sandbox"):
            self._sandbox.terminate()
