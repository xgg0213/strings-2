# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.

# Write your function here.
def long_burp(a):
    newA = "Bu"  # Start the word with "Bu"
    i = 0
    while i < a:  # Add 'r' a times
        newA += "r"
        i += 1
    newA += "p"  # Finish with "p"
    return newA

print(long_burp(3))  #> "Burrrp"
print(long_burp(5))  #> "Burrrrrp"
print(long_burp(9))  #> "Burrrrrrrrrp"