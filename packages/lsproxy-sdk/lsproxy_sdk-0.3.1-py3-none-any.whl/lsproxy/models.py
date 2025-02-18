from typing import List, Optional, Union
from pydantic import BaseModel, Field


class Position(BaseModel):
    """Specific position within a file."""

    line: int = Field(..., description="0-indexed line number.", example=10, ge=0)
    character: int = Field(
        ..., description="0-indexed character index.", example=5, ge=0
    )

    def __lt__(self, other: "Position") -> bool:
        """Compare positions by line first, then character."""
        if self.line != other.line:
            return self.line < other.line
        return self.character < other.character

    def __eq__(self, other: "Position") -> bool:
        """Check if two positions are equal."""
        return self.line == other.line and self.character == other.character

    def __le__(self, other: "Position") -> bool:
        """Less than or equal comparison."""
        return self < other or self == other

    def __gt__(self, other: "Position") -> bool:
        """Greater than comparison."""
        return not (self <= other)

    def __ge__(self, other: "Position") -> bool:
        """Greater than or equal comparison."""
        return not (self < other)


class FilePosition(BaseModel):
    """Specific position within a file, including the file path."""

    path: str = Field(..., description="The path to the file.", example="src/main.py")
    position: Position = Field(..., description="The position within the file.")

    @property
    def as_tuple(self) -> tuple[str, int, int]:
        return (self.path, self.position.line, self.position.character)

    def __lt__(self, other: "FilePosition") -> bool:
        """Compare file positions by path first, then position."""
        if self.path != other.path:
            raise NotImplementedError(
                f"Comparing file positions with different paths: {self.path} and {other.path}"
            )
        return self.position < other.position

    def __eq__(self, other: "FilePosition") -> bool:
        """Check if two file positions are equal."""
        return self.path == other.path and self.position == other.position

    def __le__(self, other: "FilePosition") -> bool:
        """Less than or equal comparison."""
        return self < other or self == other

    def __gt__(self, other: "FilePosition") -> bool:
        """Greater than comparison."""
        return not (self <= other)

    def __ge__(self, other: "FilePosition") -> bool:
        """Greater than or equal comparison."""
        return not (self < other)

    def __hash__(self) -> int:
        return hash((self.path, self.position.line, self.position.character))


class Range(BaseModel):
    start: Position = Field(..., description="Start position of the range.")
    end: Position = Field(..., description="End position of the range.")

    def __hash__(self) -> int:
        return hash((self.start.line, self.start.character, self.end.line, self.end.character))


class FileRange(BaseModel):
    """Range within a file, defined by start and end positions."""

    path: str = Field(..., description="The path to the file.", example="src/main.py")
    range: Range = Field(..., description="The range within the file.")

    def contains(self, file_position: FilePosition) -> bool:
        """Check if a position is within the range."""
        return (
            self.path == file_position.path
            and self.range.start <= file_position.position
            and file_position.position <= self.range.end
        )

    def __lt__(self, other: "FileRange") -> bool:
        """Compare ranges by path first, then start position."""
        if self.path != other.path:
            return self.path < other.path
        return self.range.start < other.range.start

    def __eq__(self, other: "FileRange") -> bool:
        """Check if two ranges are equal."""
        return (
            self.path == other.path
            and self.range.start == other.range.start
            and self.range.end == other.range.end
        )

    def __le__(self, other: "FileRange") -> bool:
        """Less than or equal comparison."""
        return self < other or self == other

    def __gt__(self, other: "FileRange") -> bool:
        """Greater than comparison."""
        return not (self <= other)

    def __ge__(self, other: "FileRange") -> bool:
        """Greater than or equal comparison."""
        return not (self < other)

    def __hash__(self) -> int:
        return hash(
            (
                self.path,
                self.range.start.line,
                self.range.start.character,
                self.range.end.line,
                self.range.end.character,
            )
        )


class CodeContext(BaseModel):
    """Contextual information of the source code around a symbol or reference."""

    range: FileRange = Field(..., description="The range within the file.")
    source_code: str = Field(
        ..., description="The source code within the specified range."
    )


class Symbol(BaseModel):
    """Representation of a symbol defined in the codebase."""

    kind: str = Field(
        ...,
        description="The kind of the symbol (e.g., function, class).",
        example="class",
    )
    name: str = Field(..., description="The name of the symbol.", example="User")
    identifier_position: FilePosition = Field(
        ..., description="The start position of the symbol's identifier."
    )
    file_range: FileRange = Field(..., description="The full range of the symbol.")

    def __hash__(self) -> int:
        return hash((self.kind, self.name, self.identifier_position, self.file_range))


class Identifier(BaseModel):
    """Representation of an identifier in code."""

    name: str = Field(..., description="The name of the identifier.")
    file_range: FileRange = Field(
        ..., description="The range of the identifier in the file."
    )
    kind: Optional[str] = Field(
        ..., description="The kind of identifier (e.g., function call or decorator. We have this info when finding referenced symbols"
    )


class FindIdentifierRequest(BaseModel):
    """Request to find all occurrences of an identifier by name in a file."""

    name: str = Field(..., description="The name of the identifier to search for.")
    path: str = Field(
        ..., description="The path to the file to search for identifiers."
    )
    position: Optional[Position] = Field(
        None,
        description="The position hint to search for identifiers. If provided, returns exact match or closest matches.",
    )


class IdentifierResponse(BaseModel):
    """Response containing found identifiers."""

    identifiers: List[Identifier] = Field(..., description="List of found identifiers.")


class DefinitionResponse(BaseModel):
    """Response containing definition locations of a symbol."""

    definitions: List[FilePosition] = Field(
        ..., description="List of definition locations for the symbol."
    )
    selected_identifier: Optional[Identifier] = Field(
        None, description='The identifier that was "clicked-on" to get the definition.'
    )
    raw_response: Optional[Union[dict, list]] = Field(
        None,
        description=(
            "The raw response from the language server.\n\n"
            "https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition"
        ),
    )
    source_code_context: Optional[List[CodeContext]] = Field(
        None, description="Source code contexts of the symbol definitions."
    )


class GetDefinitionRequest(BaseModel):
    """Request to retrieve the definition of a symbol."""

    position: FilePosition = Field(
        ...,
        description="The position of the symbol whose definition is to be retrieved.",
    )
    include_raw_response: Optional[bool] = Field(
        False,
        description="Whether to include the raw response from the language server.",
    )
    include_source_code: Optional[bool] = Field(
        False,
        description="Whether to include the source code around the symbol's identifier.",
    )


class ReferencesResponse(BaseModel):
    """Response containing references to a symbol."""

    references: List[FilePosition] = Field(
        ..., description="List of reference locations for the symbol."
    )
    selected_identifier: Optional[Identifier] = Field(
        None, description='The identifier that was "clicked-on" to get the references.'
    )
    context: Optional[List[CodeContext]] = Field(
        None, description="Source code contexts around the references."
    )
    raw_response: Optional[Union[dict, list]] = Field(
        None,
        description=(
            "The raw response from the language server.\n\n"
            "https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references"
        ),
    )


class GetReferencesRequest(BaseModel):
    """Request to find all references to a symbol."""

    identifier_position: FilePosition = Field(
        ...,
        description="The position of the symbol whose references are to be found.",
    )
    include_code_context_lines: Optional[int] = Field(
        None,
        description="Number of source code lines to include around each reference.",
        ge=0,
    )
    include_raw_response: Optional[bool] = Field(
        False,
        description="Whether to include the raw response from the language server.",
    )


class ReferenceWithSymbolDefinitions(BaseModel):
    """Reference with its associated symbol definitions."""
    
    reference: Identifier = Field(..., description="The reference to the symbol")
    definitions: List[Symbol] = Field(..., description="The symbol definitions found")


class ReferencedSymbolsResponse(BaseModel):
    """Response containing categorized referenced symbols."""
    
    workspace_symbols: List[ReferenceWithSymbolDefinitions] = Field(
        ..., 
        description="Symbols found in the workspace with their definitions"
    )
    external_symbols: List[Identifier] = Field(
        ..., 
        description="Symbols that only have definitions outside the workspace"
    )
    not_found: List[Identifier] = Field(
        ...,
        description="Symbols where no definitions could be found"
    )


class GetReferencedSymbolsRequest(BaseModel):
    """Request to get symbols referenced from a specific position."""

    full_scan: Optional[bool] = Field(
        False,
        description="Whether to use more permissive rules for scanning for references",
    )
    
    identifier_position: FilePosition = Field(
        ...,
        description="The position of the identifier whose referenced symbols should be found"
    )


class ErrorResponse(BaseModel):
    """Response representing an error."""

    error: str = Field(..., description="The error message.")


class ReadSourceCodeResponse(BaseModel):
    """Response containing source code for a file range."""

    source_code: str = Field(
        ..., description="The source code for the specified range."
    )


class ReadSourceCodeRequest(BaseModel):
    """Request to read source code from a file with an optional range."""
    path: str = Field(..., description="Path to the file, relative to the workspace root")
    range: Optional[Range] = Field(None, description="Optional range within the file to read")
