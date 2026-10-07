# Exercise 3: Customer Greeting Formatter

def format_greeting(name, title="Customer"):
    # Remove extra spaces from the beginning and end
    name = name.strip()

    # Check if the name is empty
    if name == "":
        return "Hello, Valued Customer!"

    # Capitalize the first letter of each name
    name = name.title()

    # Split the full name into separate parts
    name_parts = name.split()

    # Get the first name
    first_name = name_parts[0]

    # Return the formatted greeting
    return f"Hello, {first_name} ({title})!"


# Ask the user for their full name
full_name = input("What's your full name? ")

# Call the function and print the result
print(format_greeting(full_name))