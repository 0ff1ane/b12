FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev
COPY . .
RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"

ARG SIGNING_KEY
ARG API_URL
ARG NAME
ARG EMAIL
ARG RESUME_URL

# TODO: move SIGNING_KEY env as wofkflow arg
ENV SIGNING_KEY=$SIGNING_KEY
ENV API_URL=$API_URL
ENV NAME=$NAME
ENV EMAIL=$EMAIL
ENV RESUME_URL=$RESUME_URL

CMD ["uv", "run", "main.py"]
