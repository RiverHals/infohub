from pydantic import BaseModel, Field

class Process(BaseModel):
     name: str = Field(..., title="The name of the process", min_length=1, max_length=150)
     # body: str = Field(..., title="The description of the process", min_length=1, max_length=100)