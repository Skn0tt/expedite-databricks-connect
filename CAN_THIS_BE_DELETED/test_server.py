from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="token-abc123")

completion = client.chat.completions.create(
    model="neuralmagic/Meta-Llama-3.1-405B-Instruct-quantized.w4a16",
    messages=[{"role": "user", "content": "Hello!"}],
)

print(completion)
