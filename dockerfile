FROM python:3.10-slim

#Install system deps (tesseract + opencv libs)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    libglib2.0-0 libsm6 libxext6 libxrender-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

#Install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Make sure traineddata is in Tesseract path
# Assuming your captcha.traineddata is in ./tessdata
RUN mkdir -p /usr/share/tesseract-ocr/5/tessdata
COPY tessdata/captcha.traineddata /usr/share/tesseract-ocr/5/tessdata/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
