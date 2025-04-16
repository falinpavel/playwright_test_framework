FROM ubuntu:latest
LABEL authors="Alove"

ENTRYPOINT ["top", "-b"]

FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g playwright \
    && playwright install chromium

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--alluredir=reports/allure-results"]