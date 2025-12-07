from fastapi import FastAPI
from app.api import auth
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth")
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
