FROM python:3.10-alpine

COPY . .

RUN python3 -m pip install -r requirements.txt
RUN alembic upgrade head

CMD ["uvicorn", "run", "main:app", "--host", "0.0.0.0", "--port", "80"]