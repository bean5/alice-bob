from cryptography.fernet import Fernet
import os
import requests

API_URL = os.environ.get("API_URL")

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Secret message")
print(token)

# TODO: submit token to API and print response


response = requests.post(f"{API_URL}/verify", json={"token": token})
print(response.json())
print("Success!" if response.json().get("message") == "ok" else "Failure!")

# TODO:
# Create nonce and message
# Sign message
# Submit message to api
# Print "Success!" if api returns OK

# Small test suite: add test case that modifies the nonce or message. Verify that API returns false.
