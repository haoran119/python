import os

root = '.'

for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith('.json'):
            filename = os.path.join(path, name)
            print(filename) # '.\path\test.json'
