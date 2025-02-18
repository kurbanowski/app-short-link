import os, random, string, urllib.parse
from fastapi import FastAPI, HTTPException, Query
from starlette.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise
from app.schemas import LinkCreate, LinkResponse
from app.models import ShortLink

app = FastAPI(
    title="FastAPI Link Shortener",
    description="A FastAPI based app for short link generation and redirection using REST API.",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# TOrtoise db config
user = os.getenv('POSTGRES_USER')
password = urllib.parse.quote_plus(os.getenv("POSTGRES_PASSWORD"))
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')
db = os.getenv('POSTGRES_DB')

register_tortoise(
    app,
    db_url=f"postgres://{user}:{password}@{host}:{port}/{db}",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
def read_root():
    return {"message": "API is running!"}

def generate_short_link(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.get("/{short_url}")
async def redirect_to_original(short_url: str):
    link = await ShortLink.filter(short_url=short_url).first()
    if not link:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=link.original_url)

@app.post("/new", response_model=LinkResponse)
async def new_short_link(link: LinkCreate, length: int = Query(6, ge=6, le=20, description="Must be between 6 and 20 characters")):
    """
        Generate short link for given URL.
        The 'original_url' parameter is provided in the request body.
    """
    if length < 6 or length > 20:
        raise HTTPException(
            status_code=400,
            detail="Short link length must be 6 to 20 characters long."
        )
    existing = await ShortLink.filter(original_url=link.original_url).first()
    if existing:
        return {
            "original_url": existing.original_url,
            "short_url": f"http://localhost:8000/{existing.short_url}"
        }

    short_url = generate_short_link(length)
    new_link = await ShortLink.create(original_url=link.original_url,
                                      short_url=short_url)
    return {
        "original_url": new_link.original_url,
        "short_url": f"http://localhost:8000/{new_link.short_url}"
    }
