from pydantic import BaseModel, Field

class RequestSchema(BaseModel):
    path: str | None = None
