from pydantic import BaseModel

class LinkCreate(BaseModel):
    original_url: str

class LinkResponse(BaseModel):
    original_url: str
    short_url: str
