from uuid import UUID

from ragloader.extraction import ExtractedDocument


class DocumentChunk:
    """Class representing a chunk of a document."""

    def __init__(self, content: str, index: int):
        self.content: str = content
        self.chunk_index: int = index
        self.document_metadata: dict = {}

    def add_metadata(self, document_metadata: dict) -> None:
        self.document_metadata: dict = document_metadata


class ChunkedDocument:
    """Class representing a document split into chunks."""

    def __init__(self, parent_document: ExtractedDocument):
        self.document_uuid: UUID = parent_document.uuid
        self.document_content: str = parent_document.document_content
        self.document_class: str = parent_document.document_class
        self.document_structure: dict = parent_document.document_structure
        self.document_name: str = parent_document.document_name
        self.chunks: list[DocumentChunk] = []

    def add_chunk(self, content: str):
        chunk = DocumentChunk(content, len(self.chunks))
        chunk.add_metadata(
            {
                "parent_document_uuid": self.document_uuid,
                "parent_document_name": self.document_name,
                "parent_document_class": self.document_class
            }
        )
        self.chunks.append(chunk)
