from abc import ABC, abstractmethod
from typing import Optional


class BaseTextSplitter(ABC):
    @abstractmethod
    def split(self, text: str) -> list[str]:
        raise NotImplementedError
