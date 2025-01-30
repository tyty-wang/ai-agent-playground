import base64
import re

# encode image into base64 byte strings
def encode_image(img_path):
    with open(img_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# extract text from image

# extract code from image
def extract_code(txt):
    pattern = r'```python\s+(.*?)\s+```'
    match = re.search(pattern, txt, re.DOTALL)

    if match:
        return match.group(1)
    return None