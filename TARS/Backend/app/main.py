from fastapi import FastAPI
from app.routes.filesystem_routes import router as filesysytem_router

app = FastAPI()

# Collega il router
app.include_router(filesysytem_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Benvenuto nel backend API!"}
