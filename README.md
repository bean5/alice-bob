# signing verification API

A demo for signing and verifying signed packages. This demonstrates a _trusted_ use of Alice-Bob communication. Note that if the communication occurs over insecure channels, a man-in-the-middle attack is possible. This is for demonstration purposes only.

## Design decisions

Python is used for almost everything because it well-known packages exist for [APIs](https://fastapi.tiangolo.com/) (or [github](https://github.com/fastapi)) and for [cryptograhy](https://cryptography.io/en/latest/).

This service has zero infrastructure for deployment, including deployment wrapping through Docker. Most of my projects have this additional wrapping, but to keep this project simple, I forego this step.

If you want to modify this project in VS Code (or derivatives), there are some recommended extensions defined in `.vscode/extensions.json`. They are not required.

## Requirements

Python 3.14^
[uv](https://github.com/astral-sh/uv) by [Astral](https://github.com/astral-sh) (`pip install uv`)

## Advised

Docker

## Setup

```sh
cd ./
cd api/

uv sync
uv run fastapi dev main.py &

cd ..
cd client/

uv sync
uv run main.py
```

OR with docker:

```sh
docker compose build
docker compose up -d api
docker compose run client
```

## Notes

This project uses FastAPI. Swagger docs are automatically generated as a result and once the service is up, they are available at <http://localhost/docs>

## Ideas

- Place behind SSL curtain to mitigate MITM vector
- Make this more declarative by using one or both of the following
  - Docker containers
  - NixOS flakes
- For development, add hot-reload in API to streamline iteration
