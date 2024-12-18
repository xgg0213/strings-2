# Create a function that returns whether or not the string is a Palindrome.

# Write your function here.
def is_palindrome(a):
    if len(a) % 2 == 0:
        i = 0
        while i<=len(a)/2:
            if a[i]!=a[len(a)-1-i]:
                return False
            i+=1
    if len(a) % 2!=0:
        j=0
        while j<=len(a) // 2:
            if a[j] !=a[len(a)-1-j]:
                return False
            j+=1
    return True

print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False