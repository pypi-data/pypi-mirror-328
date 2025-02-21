# RunLlama

Simple CLI tool for [Ollama (LLM) models](https://ollama.com/search).

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/yandex/perforator/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/runllama?logo=pypi&style=flat&color=blue)](https://pypi.org/project/runllama/)
[![PyPI Version](https://img.shields.io/pypi/v/runllama.svg)](https://pypi.org/project/runllama/)

## Installation

Install via pip:

```bash
pip install runllama
```

Or with Poetry:

```bash
poetry add runllama
```

Run the CLI:

```bash
runllama --help
```

## For Development

Build and run ollama server docker container

```bash
docker build -t runllama .
docker run -d -p 11434:11434 -v ollama:/app/.ollama --name runllama runllama 
```

Install dependencies

```bash
poetry install
poetry shell
```

Run Python script

```bash
python src/main.py --help
```

## Testing

Before running Pytest, ensure the ollama server is running on port 11434.

```bash
pytest -v -s tests/test_*
```

## License

The source code is licensed under the MIT License (see [LICENSE](LICENSE)).
