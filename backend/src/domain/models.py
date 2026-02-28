from pydantic import BaseModel, Field

class Article(BaseModel):
    title: str = Field(..., description="The official academic title of the paper")
    authors: str = Field(..., description="Authors formatted in APA style")
    year: str = Field(..., description="Publication year")
    journal: str = Field(..., description="Name of the journal or publisher")
    doi: str = Field(..., description="Full DOI URL")
    issn: str = Field(..., description="ISSN")
    citescore: str = Field(..., description="2 year cite score")
    full_apa: str = Field(..., description="Complete APA 7th edition reference string")