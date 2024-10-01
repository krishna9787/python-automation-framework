import os
from dotenv import load_dotenv

# load .env file to environment
load_dotenv()

TEST_URL = os.getenv('TEST_URL')
BROWSER = os.getenv('BROWSER')
IMPLICIT_WAIT = os.getenv('IMPLICIT_WAIT')

print("Test URL: ", TEST_URL)