import ollama

MODEL_NAME = "codellama:7b"

def get_client():
    """
    Returns an instance of the Ollama client configured with the specified model.
    """
    return ollama;

def chat(prompt: str) -> str:
    """
    single point of contact for all the chat interactions with the Ollama model.
    """

    client = get_client()
    response = client.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]