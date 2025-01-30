import anthropic
import re

API_KEY = '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'
MODEL_NAME = 'claude-3-5-sonnet-20241022'

client = anthropic.Anthropic(api_key=API_KEY)

def get_response(prompt: str):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1000,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return message.content[0].text

def grade_correctness(text):
    pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
    return bool(pattern.match(text))

prompt = 'Starting from one, count to three. Include everything on a single line, comma-separated.'
response = get_response(prompt)

print(response)
print(grade_correctness(response))