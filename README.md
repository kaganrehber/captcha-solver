# Captcha Solver API (Dockerized)

-specified for SGK - Vizite Giriş Sistemi ve İş Kazası ve Meslek Hastalığı Bildirimi sistemi

## Requirements

- Docker (Desktop or CLI)
- fastapi
- uvicorn[standard]
- pydantic
- pytesseract
- opencv-python-headless
- numpy

## Build the Docker Image

From the project root (`captcha-solver/`):

```bash
docker build -t captcha-solver .
```

## Run the container

docker run -p 8000:8000 captcha-solver

## Solver endpoint

Solver runs on http://localhost:8000/solve-is-kazasi

## Request body

{
"image_base64": "<base64-encoded PNG or JPG image>"
}

## Response

{
"text": "solved_text_here"
}
