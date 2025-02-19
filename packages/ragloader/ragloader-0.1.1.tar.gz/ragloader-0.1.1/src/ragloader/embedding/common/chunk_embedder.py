from abc import ABC, abstractmethod

from ragloader.embedding.common.embedded_items import EmbeddedChunk
from ragloader.splitting.common.chunked_items import DocumentChunk


class ChunkEmbedder(ABC):
    vector_length = None
    @abstractmethod
    def embed(self, chunk: DocumentChunk) -> EmbeddedChunk:
        raise NotImplementedError
