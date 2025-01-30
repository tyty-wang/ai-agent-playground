import anthropic

API_KEY = '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'
MODEL_NAME = 'claude-3-5-sonnet-20241022'

client = anthropic.Anthropic(api_key=API_KEY)

def get_response(prompt: str, system_prompt=''):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1000,
        system=system_prompt,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return message.content[0].text

def check(text):
    if 'incorrect' in text.lower() or 'not correct' in text.lower():
        return True
    else:
        return False
    
prompt = '''Is this equation solved correctly below?
2x - 3 = 9
2x = 6
x = 3'''

system_prompt = '''You are a mathematician skilled at solving and checking algebraic equations. 
Answer with either correct or incorrect, and provide a brief explanation. 
If the answer is incorrect, provide the correct work and solution.'''

response = get_response(prompt, system_prompt)

print(response)
print(check(response))