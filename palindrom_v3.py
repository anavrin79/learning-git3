#is_palindrome = lambda phrase: phrase == phrase[::-1]

def is_palindrome(phrase):
    return phrase == phrase[::-1]

print ("to palindrom") if is_palindrome("aktagenerałamamałarenegatka") else print ("nie palindrom")