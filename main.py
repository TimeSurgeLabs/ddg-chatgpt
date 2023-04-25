from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from duckduckgo_search import ddg, ddg_news

from models import SearchRequest, SearchResponse, ContentRequest, ContentResponse
from utils import get_text
from browser import get_site

# create a new FastAPI app with cors enabled
app = FastAPI(title="Web Search")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.post("/search", description="Search for a query", response_model=SearchResponse)
def search(search_req: SearchRequest):
    results = ddg(search_req.query)
    return {"results": results}


@app.post('/news', description="Get the latest news", response_model=SearchResponse)
def news(search_req: SearchRequest):
    results = ddg_news(search_req.query)
    return {"results": results}


@app.post("/content", description="Get the content of a URL", response_model=ContentResponse)
def content(content_req: ContentRequest):
    resp = get_site(content_req.url)
    text = get_text(resp)
    return {"content": text}


@app.get('/.well-known/ai-plugin.json', include_in_schema=False)
def read_ai_plugin_json() -> Response:
    with open('ai-plugin.json', 'r') as f:
        return Response(f.read(), media_type='application/json')


@app.get('/robots.txt', include_in_schema=False)
def read_robots_txt() -> Response:
    with open('robots.txt', 'r') as f:
        return Response(f.read(), media_type='text/plain')
