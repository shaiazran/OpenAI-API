import json
import openai
import os

# Exclude OpenAI API from proxy settings
try:
    os.environ['NO_PROXY'] = os.environ.get('NO_PROXY', '') + ',api.openai.com'
except Exception as e:
    print(f"Error setting NO_PROXY: {e}")

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def read_json_file(file_path):
    print(f"Reading JSON file from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['description']

def rewrite_description(description):
    try:
        print("description Text...", description)
        print("Sending request to OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Updated to a generic GPT-4 model for chat
            messages=[
                {"role": "system", "content": "You are a marketing master and SEO expert."},
                {"role": "user", "content": f"Rewrite the following product description in HTML format suitable for WordPress product editor (no divs), keeping the same language: \"{description}\". Include a wow and cool design."}
            ]
        )
        print("Received response from OpenAI.")
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return None

def write_to_new_json(file_path, rewritten_html):
    print(f"Writing rewritten HTML to {file_path}...")
    new_data = {'description': rewritten_html}
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

def main():
    print("Starting script...")
    json_filename = 'PPP1495.json'
    json_filepath = os.path.join(os.path.dirname(__file__), '..', 'new_products', json_filename)
    json_filepath = os.path.normpath(json_filepath)

    description = read_json_file(json_filepath)
    rewritten_html = rewrite_description(description)

    if rewritten_html:
        new_json_filename = 'PPP1495_rewritten.json'
        new_json_filepath = os.path.join(os.path.dirname(json_filepath), new_json_filename)
        write_to_new_json(new_json_filepath, rewritten_html)
        print("Process completed successfully.")
    else:
        print("Failed to rewrite the product description.")

if __name__ == "__main__":
    main()
