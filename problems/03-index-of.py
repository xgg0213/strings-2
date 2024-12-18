# Create a function that returns the index of a given letter in the string.

# Write your function here.
def index_of(a,b):
    try:
        return a.index(b)
    except ValueError:
        return 0

print(index_of("Arm", "a"))  #> 0
print(index_of("Pie", "e"))  #> 2
print(index_of("Lucid", "i"))  #> 3
print(index_of("Obvious","u"))  #> 5
