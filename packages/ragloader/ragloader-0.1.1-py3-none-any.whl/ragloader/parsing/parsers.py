from enum import Enum

from . import (
    TxtFileParser,
    Docx2txtFileParser,
    PyMuPDFFileParser,
    OpenAIImageParser)


class FileParsers(Enum):
    """Mapper from parsers' names in config to parsing classes."""
    txt_parser = TxtFileParser
    pymupdf_parser = PyMuPDFFileParser
    docx2txt_parser = Docx2txtFileParser
    openai_image_parser = OpenAIImageParser
