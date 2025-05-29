#Using a Loop

def reverse_string(s):
    reversed_str=''

    for char in s:
        reversed_str=char+reversed_str
    return reversed_str

s="Python"

print(reverse_string(s))
