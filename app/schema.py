# create schema.py file in the root directory
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
	first_name: str
	last_name: str
	email: str
	password: str
	role: str
	
class ShowUser(BaseModel):
	first_name: str
	last_name: str
	email: str
	class Config():
		orm_mode = True

class Login(BaseModel):
	username: str
	password: str
	
class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	email: Optional[str] = None

