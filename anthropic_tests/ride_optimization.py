import anthropic
import base64, mimetypes

API_KEY = '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'
MODEL_NAME = 'claude-3-5-sonnet-20241022'

client = anthropic.Anthropic(api_key=API_KEY)

def get_response(prompt: str, system_prompt='', prefill=''):
    # img_message = create_image_message('map.jpeg')
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        system=system_prompt,
        messages=[
            {'role': 'user', 'content': prompt},
            # img_message,
            {'role': 'user', 'content': prefill}
        ]
    )
    
    return message.content[0].text

def create_image_message(image_path):
    '''Create properly formatted image message for Claude API'''
    with open(image_path, 'rb') as image_file:
        binary_data = image_file.read()
    base64_encoded_data = base64.b64encode(binary_data)
    base64_string = base64_encoded_data.decode('utf-8')
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = 'image/jpeg'
    supported_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    if mime_type not in supported_types:
        print(f'Warning: Image type {mime_type} might not be supported. Supported types are: {supported_types}')
    return [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image',
                    'source': {
                        'type': 'base64',
                        'media_type': mime_type,
                        'data': base64_string
                    }
                }
            ],
        },
    ]

prompt = f''' When assigning rides to each person, treat it as if it were like a minimization problem. Your goal is to minimize the weights of each car as much as possible, not including the weight of the driver themselves.
Each building is assigned a weight of 1; thus, if the driver is only driving people in the same building, the total weight is 0 (assuming a standard, five-seater car). However, if the driver must drive someone in a different building, then that person would 
be assigned a weight of 1; thus the total weight would be 1. 
Use the graph provided in the resource found below as a reference guide when you are determining rides. Assume that each edge has a weight of 1. You want to make sure that the total weights of each car are minimized. The drivers and riders will be provided.
Take the following steps for each rider:
    1. Find where they live on the graph. 
    2. c Based on the file at calculate their weight respective to where the driver lives on campus. Make sure to take into account the direction of the arrows. Take a look at these examples:
        a. Alice lives in East, and is driving Bob to West. Thus, the weight required for Bob is 3.
        b. Charlie lives in East, and is driving Dave to East. Thus, the weight required for Dave is 0, since they are in the same location.
    3. Find an appropriate driver for this person based on their weighting. Make sure that the car is not at full capacity, and that miniumum weight is ensured across all cars.
    4. Repeat steps 1-3 for all riders.
You will be provided with the riders and drivers in the following format: 
<drivers>
    Driver 1: Name, building, number of seats in car
    Driver 2: Name, building, number of seats in car
    ...
</drivers>
<riders>
    Rider 1: Name, building
    Rider 2: Name, building
    ...
</riders>
Your response should look like the following:
<car_1>
    Driver: Name of driver
    Rider 1: Name of rider
    Rider 2: Name of rider
    ...
</car_1>
<car_2>
    Driver: Name of driver
    Rider 1: Name of rider
    Rider 2: Name of rider
    ...
</car_2>
Make sure that the total weight across the cars is minimized, and that cars are not overfull (there are more people than the car can fit).
The image of the graph used can be found in the next prompt.
'''
system_prompt = 'Given a description about the drivers and riders in an organization, arrange the rides such that the weight of each car is minimized.'
prefill = '''
<drivers>
    Driver 1: Carson, Roosevelt, 4
    Driver 2: Justin, East, 4
    Driver 3: Serena, East, 4
    Driver 4: Pablo, West, 4
    Driver 5: Mileny, East, 4
    Driver 6: Bus, East, 14
</drivers>
<riders>
    Rider 1: Josephine, East
    Rider 2: Ashley, East
    Rider 3: Peter, East
    Rider 4: Colin, East
    Rider 5: Fayaz, East
    Rider 6: James, East
    Rider 7: Matt Liu, East
    Rider 8: Rita, East
    Rider 9: Charles, East
    Rider 10: Harrison, East
    Rider 11: Jess, East
    Rider 12: Pak, East
    Rider 13: Tyler, East
    Rider 14: Harry, East
    Rider 15: Daniel Leung, East
    Rider 16: Mia, Roth
    Rider 17: Meaghan, Roth
    Rider 18: Devin, Roth
    Rider 19: Melissa, Roth
    Rider 20: Joseph, Roth
    Rider 21: Shannon, Roth
    Rider 22: Sister, Roth
    Rider 23: Florence, Tabler
    Rider 24: Darren, Tabler
    Rider 25: Matt Leong, Tabler
    Rider 26: Will, Roosevelt
    Rider 27: Hannah, Roosevelt
    Rider 28: Anderson, Roosevelt
    Rider 29: Sophie, Roosevelt
    Rider 30: Elizabeth, Roosevelt
    Rider 31: Ashley Kong, Roosevelt
    Rider 32: Shriya, Roosevelt
    Rider 33: Britney, West
    Rider 34: Daniel Leong, West
    Rider 35: Josh, West
    Rider 36: Sowon, West
    Rider 37: Leah, West
    Rider 38: Deborah, Kelly
</riders>
'''

response = get_response(prompt, system_prompt, prefill)
print(response)