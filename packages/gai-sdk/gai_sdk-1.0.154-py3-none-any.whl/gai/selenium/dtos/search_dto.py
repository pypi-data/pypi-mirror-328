from pydantic import BaseModel, Field
from typing import Optional

class SearchRequest(BaseModel):
    query: str
    n_results: int = 10
    period: Optional[str]=None

class ChunkResult(BaseModel):
    index: int = Field(..., description="The index of the chunk in the list of chunks.")
    link_title: str = Field(..., description="The title of the search result that this chunk belongs to and can be used as citation.")
    link:str = Field(..., description="The link can be used to reference the SearchResult that this chunk belongs to and can be used as citation.")
    chunk: str = Field(..., description="The text content of the chunk.")
    score: float = Field(..., description="The relevance score of this chunk.")

class SearchResult(BaseModel):
    title: str
    link: str
    snippet: Optional[str]=""
    html_text: Optional[str]=None
    parsed_text: Optional[str]=None
    score: Optional[float]=None
    chunks: Optional[list[ChunkResult]]=None

class SearchResponse(BaseModel):
    query: str
    result: list[SearchResult]
