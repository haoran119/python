with open( filename, 'r' ) as f:
    for line in f:
        print(line, end='')

import json
with open( filename, 'w' ) as f:
    json.dump(text, f)

with open(filename, 'r') as f:
    x = json.load(f)
