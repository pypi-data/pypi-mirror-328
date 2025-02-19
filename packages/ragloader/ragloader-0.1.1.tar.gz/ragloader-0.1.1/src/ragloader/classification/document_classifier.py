from ragloader.conf.config import Config
from ragloader.parsing import ParsedDocument
from ragloader.classification import ClassifiedDocument


class DocumentClassifier:
    def __init__(self, config: Config):
        self.categories_config: dict = config["pipeline_stages"]["classification"]["categories"]

    def classify(self, parsed_document: ParsedDocument) -> ClassifiedDocument:
        classified_document: ClassifiedDocument = ClassifiedDocument(parsed_document)
        document_class = "unstructured_text"
        classified_document.set_document_class(document_class)
        return classified_document
