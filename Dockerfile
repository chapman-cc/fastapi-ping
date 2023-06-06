FROM python:3.10.11-alpine3.18

ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py main.py
COPY src src

EXPOSE ${PORT}

CMD [ "python", "main.py" ]