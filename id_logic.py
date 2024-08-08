# Generate unique IDs for 20 personnel

import random
import string
# import itertools

# Function to generate a random ID
def generate_id():
    while True:
        digs = random.choice(string.digits[6:]) + random.choice(string.digits[:4])
        letters = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
        id = f"fh-{digs}{letters}"
        if digs[0] not in '12345':
            return id


ids = []

while len(ids) < 20:
    ids.append(generate_id())
    
