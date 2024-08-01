# Mental Health Chatbot

This project contains a FastAPI server with two endpoints:
- `/rag`: Retrieval-Augmented Generation for mental health chat.
- `/classification`: Text classification.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Train the classifier model:
    ```bash
    python -m app.models.classifier
    ```

3. Run the server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Docker

Build and run the Docker container:
    ```bash
    docker build -t mental_health_chatbot .
    docker run -d -p 8000:80 mental_health_chatbot
    ```

## Unit Tests

Run the tests using pytest:
    ```bash
    pytest tests/
    ```

## Hugging Face Space

To deploy the application to Hugging Face Space, follow the instructions provided on the [Hugging Face documentation](https://huggingface.co/docs).
