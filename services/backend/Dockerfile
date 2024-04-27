FROM alpine:3.17 as builder

RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl
RUN adduser -D app

USER app

WORKDIR /home/app

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8000
CMD /home/app/.local/bin/uvicorn main:app --reload --host 0.0.0.0
