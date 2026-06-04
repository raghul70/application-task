from pydantic import BaseModel,Field

class CreateTask(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    completed: bool = Field(default=False)

class ResponseTask(BaseModel):
    id: int
    title: str
    completed: bool