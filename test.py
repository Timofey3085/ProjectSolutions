def is_palindrome(s):
    s = s.lower().replace(" ", "")
    length = len(s)
    for i in range(length//2):
        if s[i] != s[length-i-1]:
            return False
        return True


print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Аргентина манит негра"))
print(is_palindrome("Hello World"))
print(is_palindrome("1, 2, 2, 1"))