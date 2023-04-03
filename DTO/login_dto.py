from pydantic import BaseModel

class LoginDTO(BaseModel):
    email: int
    password: str