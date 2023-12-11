# Author: Caleb Moura

# Nested list containing rows of names.
rows = [
    ["Alice", "Jesus", "Timothy"],
    ["Bob", "Sheryll", "Joseph"],
    ["Charlie", "Jayden", "James"],
    ["David", "Marcus", "Christian"],
]

# Function to print each person's name in possessive form using while loops.
def print_possessive_names(data):
    index = 0
    
    # Iterate through each row using a while loop.
    while index < len(data):
        # Extract name from the current row.
        name = data[index][0]
        
        # Determine if name ends with 's.'
        if name[-1].lower() == 's':
            possessive_form = f"{name}'"
        else:
            possessive_form = f"{name}'s"
        
        # Print possessive form of the name.
        print(possessive_form)
        
        # Add the index for the next iteration.
        index += 1

# Call the function with provided nested list.
print_possessive_names(rows)