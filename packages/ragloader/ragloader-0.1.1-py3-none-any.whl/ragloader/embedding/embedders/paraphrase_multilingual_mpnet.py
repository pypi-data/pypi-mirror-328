from langchain_huggingface import HuggingFaceEmbeddings

from ragloader.embedding.common.chunk_embedder import ChunkEmbedder
from ragloader.splitting.common.chunked_items import DocumentChunk
from ragloader.embedding.common.embedded_items import EmbeddedChunk


class ParaphraseMultilingualMpnet(ChunkEmbedder):
    model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    vector_length = 768

    def embed(self, chunk: DocumentChunk) -> EmbeddedChunk:
        embeddings = HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={'token': "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"}
        )
        embedding = embeddings.embed_query(chunk.content)

        payload = {
            "embedding_model": self.model_name,
            "content": chunk.content,
            "metadata": chunk.document_metadata
        }
        embedded_chunk: EmbeddedChunk = EmbeddedChunk(embedding=embedding, payload=payload)
        return embedded_chunk
