import openai
import os
import json

openai.api_key = os.getenv('OPENAI_API_KEY')

# Use the ChatCompletion API for a conversational model interaction
def chat_with_model(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",  # or "gpt-4-0125-preview" based on availability and your requirement
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ]
    )
    return response.choices[0].message['content'].strip()  # Extracting the response text

# Example Usage
if __name__ == "__main__":
    # Example prompt; replace with the actual prompt you want to send
    prompt_text = "I need help with my physics homework."

    # Getting the response from the model
    response_text = chat_with_model(prompt_text)

    print(f"Response from GPT-4: {response_text}")
