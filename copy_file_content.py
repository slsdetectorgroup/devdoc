
import os 

with open("binaryfileformat.html", 'r') as f:
    content = f.read()

for file in os.listdir('.'):
    if file.endswith('.html') and file != "index.html":
        with open(file, 'w') as f:
            f.write(content)
