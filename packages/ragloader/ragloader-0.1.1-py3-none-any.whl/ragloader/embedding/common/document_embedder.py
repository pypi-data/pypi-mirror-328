from ragloader.conf.config import Config
from ragloader.splitting import ChunkedDocument
from ragloader.embedding.embedding_models import EmbeddingModels
from ragloader.embedding.common.embedded_items import EmbeddedChunk, EmbeddedDocument


class DocumentEmbedder:
    """Class for embedding a chunked document."""

    def __init__(self, config: Config):
        self.embedding_model_name: str = config["pipeline_stages"]["embedding"]["embedding_model"]
        self.embedding_model = EmbeddingModels.__getitem__(self.embedding_model_name).value()

    def embed(self, chunked_document: ChunkedDocument):
        embedded_document: EmbeddedDocument = EmbeddedDocument()
        for chunk in chunked_document.chunks:
            embedded_chunk: EmbeddedChunk = self.embedding_model.embed(chunk)
            embedded_document.add_chunk(embedded_chunk)

        return embedded_document
