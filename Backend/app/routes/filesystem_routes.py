from fastapi import APIRouter, HTTPException
from app.core.file_system import create_folder

router = APIRouter()

@router.post("/create-folder/")
async def create_folder_endpoint(folder_name: str, parent_folder: str = None):
    try:
        result = create_folder(folder_name, parent_folder)
        return result
    except FileExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore interno: {str(e)}")