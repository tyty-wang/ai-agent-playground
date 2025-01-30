import anthropic
import re

API_KEY = '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'
MODEL_NAME = 'claude-3-5-sonnet-20241022'

client = anthropic.Anthropic(api_key=API_KEY)

def get_response(prompt: str, system_prompt='', prefill=''):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        system=system_prompt,
        stop_sequences=['</classification>'],
        messages=[
            {'role': 'user', 'content': prompt},
            {'role': 'assistant', 'content': prefill}
        ]
    )
    
    return message.content[0].text

prompt = '''My Mixmaster will not turn on, even though I have plugged it in. Please help.
Classification: B. This email is about broken or defective components.

I am trying to sign up for the subscription online, but my payment is not being processed. What am I doing wrong?
Classification: C. This is an issue with billing and payment.

What other Mixmaster models are there?
Classification: A. This is asking a pre-sale question.

Note that Classification D (other) is only used if none of the other categories fit. 

Please classify this email as either A, B, C, or D: {email}'''

prefill = '<classification>'

emails = [
    'Hi -- My Mixmaster4000 is producing a strange noise when I operate it. It also smells a bit smoky and plasticky, like burning electronics.  I need a replacement.', # (B) Broken or defective item
    'Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?', # (A) Pre-sale question OR (D) Other (please explain)
    'I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???', # (C) Billing question
    'How did I get here I am not good with computer.  Halp.' # (D) Other (please explain)
]

answers = [
    ['B'],
    ['A', 'D'],
    ['C'],
    ['D']
]

alt_prompt = '''Emails may be classified into one or more of the following categories:
A - Pre-sale questions.
B - Broken or defective components.
C - Issues with billing or payment.
D - Other.
Please classify this email as either A, B, C, or D: {email}'''

for i, email in enumerate(emails):
    prompt_formatted = prompt.format(email=email)
    
    response = get_response(prompt_formatted, prefill=prefill)
    
    grade = any([bool(re.search(ans, response[-1])) for ans in answers[i]])
    
    print(f'User: \n{prompt_formatted}')
    print(f'Assistant: \n{prefill}')
    print(f'Claude: \n{response}')
    print(f'Check: {grade}')
    print('--------------------------------------------')

print('============== USING ALTERNATE PROMPT ==============')
for i, email in enumerate(emails):
    prompt_formatted = alt_prompt.format(email=email)
    
    response = get_response(prompt_formatted, prefill=prefill)
    
    grade = any([bool(re.search(ans, response[-1])) for ans in answers[i]])
    
    print(f'User: \n{prompt_formatted}')
    print(f'Assistant: \n{prefill}')
    print(f'Claude: \n{response}')
    print(f'Check: {grade}')
    print('--------------------------------------------')