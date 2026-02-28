from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Article

class SearchPort(ABC):
    @abstractmethod
    def find_titles(self, query: str) -> List[str]:
        """Find a list of potential article titles based on a query."""
        pass

class MetadataPort(ABC):
    @abstractmethod
    def get_metadata(self, title: str) -> Optional[Article]:
        """Fetch verified metadata for a specific title."""
        pass

class SynthesisPort(ABC):
    @abstractmethod
    def synthesize(self, query: str, articles: List[Article]) -> str:
        """Generate a cited sentence from a claim and selected articles."""
        pass