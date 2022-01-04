"""IngestorInterface defined and Ingestor class."""
from abc import ABC, abstractclassmethod
from .quoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """abstract class used as a template."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if extension is correct."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractclassmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Children classes must define the parse methode."""
        pass
