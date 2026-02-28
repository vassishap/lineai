import uvicorn
import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
from typing import List

from src.infrastructure.gemini_adapter import GeminiAdapter
from src.infrastructure.crossref_adapter import CrossrefAdapter
from src.application.services import LineAIService
from src.domain.models import Article

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv("GEMINI_API_KEY")
service = LineAIService(GeminiAdapter(api_key), CrossrefAdapter(), GeminiAdapter(api_key))


class QueryRequest(BaseModel):
    query: str


class SynthesisRequest(BaseModel):
    query: str
    selected_articles: List[Article]


@app.post("/search")
@limiter.limit("5/minute")
async def search(req: QueryRequest, request: Request):
    articles = service.research_phase(req.query)
    return articles


@app.post("/synthesize")
@limiter.limit("2/minute") # Added protection for your Gemini tokens
async def synthesize(req: SynthesisRequest, request: Request):
    result = service.synthesis_phase(req.query, req.selected_articles)
    return {"text": result, "references": req.selected_articles}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) 
    uvicorn.run(app, host="0.0.0.0", port=port)
