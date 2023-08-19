import re

with open('output.txt', encoding='utf-8') as f: 
    fragments = f.read()

with open('output.txt', 'w') as f:
    f.write(re.sub('[^a-zA-Z0-9\n\.]', ' ', fragments))