import numpy as np


class EmbeddedChunk:
    def __init__(self, embedding: np.array, payload: dict):
        self.embedding: np.array | list = embedding
        self.payload: dict = payload


class EmbeddedDocument:
    def __init__(self):
        self.embedded_chunks: list[EmbeddedChunk] = []

    def add_chunk(self, chunk: EmbeddedChunk):
        self.embedded_chunks.append(chunk)
