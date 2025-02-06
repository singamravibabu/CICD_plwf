import os

# Reading environment variables
global_message = os.getenv("GLOBAL_MESSAGE", "Default Global Message")
pi_value = os.getenv("PI_VALUE", "Default PI Vaue")
secret_key = os.getenv("SECRET_KEY", "No secret key found")
runtime_message = os.getenv("RUNTIME_MESSAGE", "Default Runtime Message")

# Printing environment variables
print(f"Global message: {global_message}")
print(f"PI Value: {pi_value}")
print(f"Secret Key: {secret_key}")
print(f"Runtime Message: {runtime_message}")
