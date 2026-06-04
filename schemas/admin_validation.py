from pydantic import BaseModel

class admin_create(BaseModel):
    name: str
    age: int

class admin_response(BaseModel):
    id: int
    name: str
    age: int

class admin_update(BaseModel):
    name: str | None = None
    age: int | None = None