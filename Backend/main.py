import sys
import os

# Assicurati che la directory principale sia inclusa nel path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from app.routes.filesystem_routes import router as filesystem_router

# Configurazione dell'app FastAPI
app = FastAPI()

# Collega i router
app.include_router(filesystem_router, prefix='/api')

@app.get("/")
async def root():
    return {"message": "Benvenuto nel backend API!"}

if __name__ == "__main__":
    import uvicorn

    # Esegui l'app con configurazioni di default
    uvicorn.run(app, host="0.0.0.0", port=8000)
