FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app/app
COPY ./main.py /app/main.py
COPY ./.env /app/.env

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9527"]
