from id_logic import ids
from totalpersonnels import locations


# Create a dictionary to map IDs to locations
assignments = dict(zip(ids, locations))

# Display the assignments
def main():
    for id, location in assignments.items():
        print(f"ID: {id} assigned to {location}")

# run program 
main()
