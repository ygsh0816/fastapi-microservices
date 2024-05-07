FROM python:3.9

ENV APP_ENV dev
WORKDIR /app

COPY /app /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash", "./app/executable.sh"]

#CMD ["uvicorn", "app.main:fast_app","--host", "0.0.0.0",  "--port", "8000", "--reload"]