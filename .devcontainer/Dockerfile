FROM python:3.10-rc-slim

ENV PYTHONPATH /workspaces/email-provider-switcher

RUN apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated \
    apt-utils \
    dialog \
    procps \
    git \
    lsb-release \
    gcc \
    build-essential \
    libmariadb-dev \
    && pip install --upgrade pip \
    && pip install poetry \
    && pip install --no-cache-dir \
    black \
    flake8 \
    isort \
    pre-commit \
    lizard \
    pyright \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
