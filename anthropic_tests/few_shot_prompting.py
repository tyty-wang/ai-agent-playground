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

prompt = '''Please complete the conversation by writing the next line, speaking as "A".
Q: Is the tooth fairy real?
A: Of course, sweetie. Wrap up your tooth and put it under your pillow tonight. There might be something waiting for you in the morning.
Q: Will Santa bring me presents on Christmas?'''

print(get_response(prompt))

prompt = '''Silvermist Hollow, a charming village, was home to an extraordinary group of individuals.
Among them was Dr. Liam Patel, a neurosurgeon who revolutionized surgical techniques at the regional medical center.
Olivia Chen was an innovative architect who transformed the village's landscape with her sustainable and breathtaking designs.
The local theater was graced by the enchanting symphonies of Ethan Kovacs, a professionally-trained musician and composer.
Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers.
These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow.

1. Dr. Liam Patel [NEUROSURGEON]
2. Olivia Chen [ARCHITECT]
3. Ethan Kovacs [MISICIAN AND COMPOSER]
4. Isabella Torres [CHEF]


At the heart of the town, Chef Oliver Hamilton has transformed the culinary scene with his farm-to-table restaurant, Green Plate. Oliver's dedication to sourcing local, organic ingredients has earned the establishment rave reviews from food critics and locals alike.
Just down the street, you'll find the Riverside Grove Library, where head librarian Elizabeth Chen has worked diligently to create a welcoming and inclusive space for all. Her efforts to expand the library's offerings and establish reading programs for children have had a significant impact on the town's literacy rates.
As you stroll through the charming town square, you'll be captivated by the beautiful murals adorning the walls. These masterpieces are the work of renowned artist, Isabella Torres, whose talent for capturing the essence of Riverside Grove has brought the town to life.
Riverside Grove's athletic achievements are also worth noting, thanks to former Olympic swimmer-turned-coach, Marcus Jenkins. Marcus has used his experience and passion to train the town's youth, leading the Riverside Grove Swim Team to several regional championships.

1. Oliver Hamilton [CHEF]
2. Elizabeth Chen [LIBRARIAN]
3. Isabella Torres [ARTIST]
4. Marcus Jenkins [COACH]


Oak Valley, a charming small town, is home to a remarkable trio of individuals whose skills and dedication have left a lasting impact on the community.
At the town's bustling farmer's market, you'll find Laura Simmons, a passionate organic farmer known for her delicious and sustainably grown produce. Her dedication to promoting healthy eating has inspired the town to embrace a more eco-conscious lifestyle.
In Oak Valley's community center, Kevin Alvarez, a skilled dance instructor, has brought the joy of movement to people of all ages. His inclusive dance classes have fostered a sense of unity and self-expression among residents, enriching the local arts scene.
Lastly, Rachel O'Connor, a tireless volunteer, dedicates her time to various charitable initiatives. Her commitment to improving the lives of others has been instrumental in creating a strong sense of community within Oak Valley.
Through their unique talents and unwavering dedication, Laura, Kevin, and Rachel have woven themselves into the fabric of Oak Valley, helping to create a vibrant and thriving small town.'''

system_prompt = 'Given a blurb about a town and its people, list out the individuals and their professions in brackets according to the format in the examples.'

print(f'User: \n{prompt}')
print(f'Claude: \n{get_response(prompt, system_prompt=system_prompt)}')