from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as app_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include app routes
app.include_router(app_router)