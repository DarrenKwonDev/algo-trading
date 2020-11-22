import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

ACCESS_TOKEN = os.getenv("ACCESS_KEY")
print(ACCESS_TOKEN)
