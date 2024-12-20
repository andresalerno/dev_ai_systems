from openai import OpenAI
from dotenv import load_dotenv
import os

import openai

load_dotenv()

# Create an OpenAI API client.
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

# Use the try statement
try: 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
    )
    # Print the response
    print(response.choices[0].message.content)
# Use the except statement
except openai.AuthenticationError as e:
    print("Please double check your authentication key and try again, the one provided is not valid.")