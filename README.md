# signing verification API

A demo for signing and verifying signed packages. This demonstrates a _trusted_ use of Alice-Bob communication. Note that if the communication occurs over insecure channels, a man-in-the-middle attack is possible. This is for demonstration purposes only.

## Design decisions

Python is used for almost everything because it well-known packages exist for [APIs](https://fastapi.tiangolo.com/) (or [github](https://github.com/fastapi)) and for [cryptograhy](https://cryptography.io/en/latest/).

This service has zero infrastructure for deployment, including deployment wrapping through Docker. Most of my projects have this additional wrapping, but to keep this project simple, I forego this step.

If you want to modify this project in VS Code (or derivatives), there are some recommended extensions defined in `.vscode/extensions.json`. They are not required.

## Requirements

Python 3.14

## Setup

```sh
pip install -r requirements.txt
make start_api &
make test
```

## Ideas

- Place behind SSL curtain to mitigate MITM vector
- Make this more declarative by using one or both of the following
  - Docker containers
  - NixOS flakes
- For development, add hot-reload in API to streamline iteration

## Development

This project includes some development infrastructure in `./notebooks/` such as:

- main.ipynb
- nix flake

The requirements to run that are in that same folder. If you are running nix, standing up the jupyter server is simple: `cd nixos; nix develop`
