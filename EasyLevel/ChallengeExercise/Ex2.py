#  Write a program that checks if a string is a palindrome (a word, phrase, number, or sequence that reads the same forward and backward, e.g., "madam").
while True:
    string = input("Enter a normal string:")
    # starting from the end of the string (due to the -1 step) and moves towards the start
    reversed_string = string[::-1]
    if string == reversed_string:
        print("This is a palindrome string")
        break
    else:
        print("This is not a palindrome string")