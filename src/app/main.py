from app.api import notes, ping, auth
from app.db import database, engine, metadata
from fastapi import FastAPI

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
