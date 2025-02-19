from enum import Enum

from . import (
    ParaphraseMultilingualMpnet
)


class EmbeddingModels(Enum):
    """Mapper from embedding models' names and embedding models."""
    paraphrase_multilingual_mpnet = ParaphraseMultilingualMpnet
