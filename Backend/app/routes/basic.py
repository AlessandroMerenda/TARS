from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Il backend è attivo e funzionante!"}

@router.get("/status")
async def get_status():
    return {"status": "OK", "message": "Il server è operativo"}
