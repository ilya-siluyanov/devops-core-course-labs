# Lab 1 task solution

## Overview


The application provides a storage of text notes.

## Usage

In order to build and launch the app, there are some steps:

1. Install [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

1. Install [Markdown linter](https://github.com/DavidAnson/markdownlint)

1. Install [MarkdownLinterCLI](https://github.com/igorshubovych/markdownlint-cli)

1. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   npm install 
   ```

1. Run the application:

   ```bash
   python3 main.py
   ```

1. Create a note:

    ```bash
    > curl -X POST -d '{"text": "abcd"}' -H 'content-type: application/json' http://localhost:8000/notes/
    {"uuid":"0197e693-9abc-417c-b281-eacc3e1a4ecf"}
    ```

1. Get the same note:

    ```bash
    > curl http://localhost:8000/notes/0197e693-9abc-417c-b281-eacc3e1a4ecf
    {"id":"0197e693-9abc-417c-b281-eacc3e1a4ecf","text":"abcd","created_at":"2023-09-16T18:14:08.990677Z"}

    ```

Help is also available:

```bash
> python3 main.py --help
usage: main.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Interface to listen (default: 0.0.0.0)
  --port PORT  Port to listen (default: 8000)
```

## Docker

### Build

```bash
docker build -t app_python:dev .
```

NOTE: here as a context we use `.`, which can be seen as a bad practice.
Nevertheless, in `Dockerfile` we explicitly specify
which files are included into the image

### Pull

```bash
docker pull ilyasiluyanov/app_python:dev
```

### Run

```bash
docker run --rm -p 8000:8000 --name app_python ilyasiluyanov/app_python:dev
```

## Unit tests

```bash
pytest tests
```

## CI/CD

For each commit there is a pipeline with:

- lint job
- Snyk vulnerability scanner
- test job
- build and push docker image job
