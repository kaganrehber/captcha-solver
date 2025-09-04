from fastapi import FastAPI
from pydantic import BaseModel
import base64
import cv2
import pytesseract
import numpy as np

app = FastAPI()

class CaptchaRequest(BaseModel):
    image_base64: str
    
def solve_captcha(base64_string: str) -> str:
    if base64_string.startswith("data:image"):
        base64_string = base64_string.split(",", 1)[1]

    image_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    cv2.imwrite("debug_raw.png", img)
    config = "--oem 3 --psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789"
    text = pytesseract.image_to_string(img, lang="captcha", config=config).strip()

    return text

@app.post("/solve-is-kazasi")
def solve(request: CaptchaRequest):
    text = solve_captcha(request.image_base64)
    return {"text": text}
