import os
from dotenv import load_dotenv
from fastapi import APIRouter, Request
from murf import Murf

load_dotenv()
router = APIRouter()

API_KEY = os.getenv("API_KEY")
STYLE = os.getenv("STYLE")
VOICE_ID = os.getenv("VOICE_ID")


@router.get("/")
def index():
    data = {
        "name": "Akshat",
        "project": "AI Voice Agent",
        "day": 1
    }
    return data

@router.post("/getTTS")
async def TTS(request: Request):

    data = await request.json()
    text = data.get("text" , "")

    if not text:
        return {
            "status" : 400,
            "error": "please enter some text to convert it into speech"
        }

    client = Murf(api_key=API_KEY)

    response = client.text_to_speech.generate(
        text = text,
        voice_id = VOICE_ID,
        style =  STYLE,
        rate = 0
    )

    return {"audio_url" : response.audio_file}







