from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Secret message")
token

# TODO:
# Create nonce and message
# Sign message
# Submit message to api
# Print "Success!" if api returns OK

# Small test suite: add test case that modifies the nonce or message. Verify that API returns false.
