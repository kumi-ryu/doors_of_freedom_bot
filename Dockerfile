FROM python:3.8

WORKDIR /app
COPY ./src /app

RUN pip install discord

ENV TZ Asia/Tokyo

CMD ["python3", "omaraid.py"]