from fastapi import FastAPI
from app.database import engine, Base
from app import models
from fastapi.middleware.cors import CORSMiddleware

from app.routes import user 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)