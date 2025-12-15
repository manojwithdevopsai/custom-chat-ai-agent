import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

# Environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo-16k")

# Azure AD token provider (REQUIRED for AAD auth)
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

# Create Azure OpenAI client (NEW SDK + AAD)
client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_ad_token_provider=token_provider,
    api_version="2024-02-15-preview"
)

def ask_llm(prompt, memory):
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    for msg in memory:
        messages.append({"role": "user", "content": msg})

    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,   # deployment name
        messages=messages
    )

    return response.choices[0].message.content

