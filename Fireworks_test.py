import os
from dotenv import load_dotenv
from fireworks.client import Fireworks

load_dotenv()

fireworks_api_key = os.getenv('FIREWORKS_API_KEY')
fw = Fireworks(api_key=fireworks_api_key)

# Test the client
try:
    response = fw.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-405b-instruct",
        messages=[{"role": "user", "content": "Hello, World!"}]
    )
    print("Fireworks client is working correctly.")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"Error occurred: {e}")