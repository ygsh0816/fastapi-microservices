FROM python:3.9

WORKDIR /app
COPY /app /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:fast_app","--host", "0.0.0.0",  "--port", "8000", "--reload"]