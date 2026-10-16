def is_palindrome(text):
    """Return True when text reads the same forwards and backwards."""
    return text == text[::-1]


user_text = input("Enter a string: ")

if is_palindrome(user_text):
    print("That is a palindrome.")
else:
    print("That is not a palindrome.")