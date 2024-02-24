import requests
#here i tried to test api request to chat gpt but it want some money i dont wanna pay
# open ai key
api_key = 'your open ai api key'

# your text
text_to_summarize = "Your long text goes here..."

response = requests.post(
    'https://api.openai.com/v1/engines/gpt-3.5-turbo-instruct/completions',
    headers={
        'Authorization': f'Bearer {api_key}'
    },
    json={
        'prompt': f"Summarize this for a second-grade student:\n\n{text_to_summarize}",
        'temperature': 0.7,
        'max_tokens': 150
    }
)

# print retell
print(response.json())