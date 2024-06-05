FROM alpine:3.17

RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl
RUN adduser -D app

USER app

WORKDIR /home/app

COPY requirements.txt .
RUN pip3 install --user -r requirements.txt --no-cache-dir

# Ensure ~/.local/bin is in the PATH
ENV PATH="/home/app/.local/bin:${PATH}"

COPY . .

EXPOSE 8000
CMD ["/home/app/.local/bin/uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
