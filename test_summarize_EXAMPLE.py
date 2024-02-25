from g4f.client import Client
import re
import requests

import re

# Raw subtitle text with timings and other information.
raw_subtitle_text = """
YOUR SUBTITLES
"""

# Regular expression pattern to match the timing and numbering in the subtitles.
pattern = r'\d+\n\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\n'

# Remove the timing and numbering from the subtitles.
cleaned_text = re.sub(pattern, '', raw_subtitle_text)

# Remove additional newlines and leading/trailing whitespace.
cleaned_text = cleaned_text.strip().replace('\n', ' ')

# Now cleaned_text contains only the spoken content without timings and can be used in the summarization API.

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "YOUR PROMPT TO CHATGPT MODEL :"+ cleaned_text}]
)
print(response.choices[0].message.content)