from pydantic import BaseModel, EmailStr
from typing import Optional, List



class User(BaseModel):
    email: EmailStr
    password: str


    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }




class UserSignIn(BaseModel):
    email: EmailStr
    password: str
 
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }
