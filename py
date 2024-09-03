
# user_input.py

# Ask the user for their name and store it in a variable
name = input("What is your name? ")

# Ask the user for their age and store it in a variable
age = input("How old are you? ")

# Ask the user for their location and store it in a variable
location = input("Where do you live? ")

# Create a personalized message
message = f"Hello {name}, you are {age} years old and live in {location}."

# Print the message to the console
print(message)

# Write the message to a file
with open('output.txt', 'w') as file:
    file.write(message)
