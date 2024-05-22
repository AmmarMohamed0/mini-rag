# mini-rag_test

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:

```cmd
conda create -n mini-rag python=3.8
```

3. Activate the environment:

```cmd
conda activate mini_rag
```

## Installation

### Install the required packages

```cmd
pip install -r requirements.txt
```

### Setup the environment variables

```cmd
copy .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ sudo docker compose up -d
```

## Run the FastAPI server

```cmd
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)
