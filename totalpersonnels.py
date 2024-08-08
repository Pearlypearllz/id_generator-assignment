# Generate unique IDs for 20 personnel and locations
# import 
import random

locations = []
for i in range(1, 21):
    """Generate 0 locations"""
    locations.append(f"Location {i}") 
random.shuffle(locations)
