from python:3.11-slim

workdir /app/

run pip install playwright

run playwright install --with-deps chromium

copy main.py /app/

cmd ["python", "main.py"]