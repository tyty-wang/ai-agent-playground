from openai import OpenAI
from utility import encode_image

client = OpenAI(api_key='sk-proj-ILowSM433CCVU7Xxxh4NT3BlbkFJOI4v1JPcYbw67JqzkmCT') # create GPT client

prompt = 'What does this image depict about the user\'s privacy preference? Provide your response in JSON format, with the privacy feature as the key and the user\'s preference as the value.'
img_path = 'camera_privacy_preference.png'

b64_img = encode_image(img_path=img_path)

response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': prompt},
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': f'data:image/png;base64,{b64_img}'
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print('Completion Tokens:', response.usage.completion_tokens)
print('Prompt Tokens:', response.usage.prompt_tokens)
print('Total Tokens:', response.usage.total_tokens)
print('Possible Responses:')
for choice in response.choices:
    print(choice.message.content)
print('\n')
print('Final Response:', response.choices[0].message.content)