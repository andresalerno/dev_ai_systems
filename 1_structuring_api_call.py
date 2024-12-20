
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Create an OpenAI API client.
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

# Create the request
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
   {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}
  ],
  # Specify the response format
  response_format={"type": "json_object"}
)

# Print the response
print(response.choices[0].message.content)