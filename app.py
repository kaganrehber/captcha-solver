from fastapi import FastAPI
from pydantic import BaseModel
import base64
import cv2
import pytesseract
import numpy as np
import easyocr

app = FastAPI()

reader = easyocr.Reader(['en'])

class CaptchaRequest(BaseModel):
    image_base64: str
    
def solve_captcha(base64_string: str) -> str:
    if base64_string.startswith("data:image"):
        base64_string = base64_string.split(",", 1)[1]

    image_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    cv2.imwrite("debug_raw.png", img)
    
    results = reader.readtext(img, detail=0)
    text = "".join(results).strip() if results else ""
    return text

@app.post("/solve")
def solve(request: CaptchaRequest):
    text = solve_captcha(request.image_base64)
    return {"text": text}
