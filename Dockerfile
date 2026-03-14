FROM python:3.13-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libldap2-dev \
    libsasl2-dev \
    libpq-dev \
    postgresql-client \
    vim \
    snmp \
    tshark \
    libcap2-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY ./cipherconverter .
