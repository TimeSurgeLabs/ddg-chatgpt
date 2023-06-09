dev:
  uvicorn --reload --port 8000 --host 0.0.0.0 --reload main:app

build-docker:
  docker build --platform linux/amd64 -t ghcr.io/timesurgelabs/ddg-chatgpt:main .

run-docker:
  docker run --platform linux/amd64 --rm -p 8000:8000 ghcr.io/timesurgelabs/ddg-chatgpt:main

push-docker:
  docker push ghcr.io/timesurgelabs/ddg-chatgpt:main
