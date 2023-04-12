from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    results: list[dict]

class ContentRequest(BaseModel):
    url: str

class ContentResponse(BaseModel):
    content: str
