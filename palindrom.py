def is_palindrome(s):
    """
    Returns True if the given string is a palindrome, False otherwise.
    """
    s = s.lower()  # convert to lowercase to ignore case sensitivity
    s = s.replace(" ", "")  # remove all spaces
    return s == s[::-1]  # compare with the reversed string


# example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True