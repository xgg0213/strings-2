# Create a function that reverses the string using recursion.

# Write your function here.
def recursive_string(a):
    newString=''
    i=0
    while i<len(a):
        newString=newString+a[len(a)-1-i]
        i+=1
    return newString

print(recursive_string("civic")) # civic
print(recursive_string("refer")) # refer
print(recursive_string("string")) # gnirts
print(recursive_string("avocado")) # odacova
print(recursive_string("application")) # noitacilppa