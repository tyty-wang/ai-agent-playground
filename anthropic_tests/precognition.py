import anthropic

API_KEY = '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'
MODEL_NAME = 'claude-3-5-sonnet-20241022'

client = anthropic.Anthropic(api_key=API_KEY)

def get_response(prompt: str, system_prompt='', prefill=''):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        system=system_prompt,
        messages=[
            {'role': 'user', 'content': prompt},
            {'role': 'assistant', 'content': prefill}
        ]
    )
    
    return message.content[0].text

system_prompt = 'You are a savvy reader of movie reviews.'

review_prompt= '''Is this review sentiment positive or negative? First, write the best arguments for each side in  and  XML tags, then answer.
This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since 1900.'''

print(get_response(review_prompt, system_prompt))

print('--------------------------------------------------')

actor_prompt = '''Name a famous movie starring an actor who was born in the year 1956. 
First brainstorm about some actors and their birth years in  tags, then give your answer.'''

print(get_response(actor_prompt))