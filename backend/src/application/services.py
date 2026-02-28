from typing import List
from src.domain.ports import SearchPort, MetadataPort, SynthesisPort
from src.domain.models import Article

class LineAIService:
    def __init__(self, searcher: SearchPort, metadata: MetadataPort, synthesizer: SynthesisPort):
        self.searcher = searcher
        self.metadata = metadata
        self.synthesizer = synthesizer

    def research_phase(self, query: str) -> List[Article]:
        """Workflow: Search Titles -> Fetch Real Metadata."""
        titles = self.searcher.find_titles(query)

        if not titles:
            return []

        verified_articles = []
        seen_dois = set()

        for t in titles:
            article = self.metadata.get_metadata(t)
            if article and article.doi not in seen_dois:
                verified_articles.append(article)
                seen_dois.add(article.doi)
        return verified_articles

    def synthesis_phase(self, query: str, selected_articles: List[Article]) -> str:
        """Workflow: Take user-selected articles -> Final text."""
        return self.synthesizer.synthesize(query, selected_articles)