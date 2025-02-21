ARG PYTHON_VERSION=3.9 \
    SUZIEQ_VERSION

# Install uv
FROM python:$PYTHON_VERSION-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

# Copy the project into the intermediate image
ADD . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

ARG PYTHON_VERSION=3.9 \
    SUZIEQ_VERSION

FROM python:$PYTHON_VERSION-slim

ARG PYTHON_VERSION=3.9 \
    SUZIEQ_VERSION \
    USERNAME=suzieq \
    USER_ID=1000

# Copy the environment, but not the source code
COPY --from=builder --chown=app:app /app/.venv /app/.venv

RUN apt-get update && \
    apt-get install -y vim-tiny ssh traceroute iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME [ "/home/$USERNAME/parquet" ]

ENV SQENV=docker

USER $USERNAME
WORKDIR /home/$USERNAME
ENTRYPOINT ["/bin/bash"]

# Set the Labels
LABEL name=suzieq
LABEL description="Network Observability Tool"
LABEL version=$SUZIEQ_VERSION
LABEL python_version=$PYTHON_VERSION
