# TASK: Write a program that checks if a word is a palindrome


# Prompt the user to enter a string
usr_input = input("Enter string:")
# Reverse string using slicing
reversed_string = user_input[::-1]
# Check original string is equal to reversed string
if user_input == reversed_string:
    # If they are equal, it's a palindrome
    print("String is a palindrome")
else:
    # If they aren't equal, not palindrome
    print("Sting isn't a palindrome")


# TASK: Create a program to count number of vowels in words


# Prompt user to enter string
user_input = input("Enter string:")
# Define string containing every vowel
vowels = "aeiouAEIOU"
# Initialize a counter to zero
count = 0
# Read over the characters in string
for char in user_input:
    if char in vowels:
# If character is vowel, add the counter    
    count += 1

# Display total amount of vowels found
print(f"Number of vowels in string: {count}")

# TASK: Write a program to reverse word input by user


# Prompt user to enter word
word = input("Enter word:")
# Reverse word with slicing
reversed_word = word[::-1]
# Display word in reverse
print(f"Reversed word is: {reversed_word}")