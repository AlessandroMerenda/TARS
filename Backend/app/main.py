from fastapi import FastAPI
from app.routes.basic import router as basic_router

app = FastAPI()

# Collega il router
app.include_router(basic_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Benvenuto nel backend API!"}
