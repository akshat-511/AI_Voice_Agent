from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
def index():
    data = {
        "name": "Akshat",
        "project": "AI Voice Agent",
        "day": 1
    }
    return data
