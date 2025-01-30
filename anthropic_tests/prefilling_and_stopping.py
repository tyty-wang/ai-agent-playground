import anthropic

API_KEY = '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'
MODEL_NAME = 'claude-3-5-sonnet-20241022'

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt='', prefill=''):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        stop_sequences=['</haiku>', '}'], # stops once it reaches this tag -- does not print it out!
        messages=[
          {'role': 'user', 'content': prompt},
          {'role': 'assistant', 'content': prefill}
        ]
    )
    return message.content[0].text

animal = 'rabbit'
prompt = f'Please write a haiku about {animal}. Put it in tags.'
prefill = '''<haiku>
Soft bunny hopping'''
print('User: ')
print(prompt)
print('Assistant: ')
print(prefill)
print('Claude: ')
print(get_completion(prompt, prefill=prefill))

json_prompt = f'Please write a haiku about {animal}. Use JSON format with the keys as \"first_line\", \"second_line\", and \"third_line\".'
json_prefill = '{'
print('User: ')
print(json_prompt)
print('Assistant: ')
print(json_prefill)
print('Claude: ')
print(get_completion(json_prompt, prefill=json_prefill))