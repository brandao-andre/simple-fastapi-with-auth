from fastapi import APIRouter, Depends
from app.auth.auth_bearer import JWTBearer

router = APIRouter()

@router.get("/ping", dependencies=[Depends(JWTBearer())])
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}
