"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False

set an o and x counter to zero
Loop over each character in the string
do a check if it contains an 'x'
    increment the x counter
do a check if it contains an 'o'
    increment the o counter

check if x counter is equal to a counter
    return true to the caller
otherwise
    return false to the caller
"""
def XO(txt:str) -> bool:
    # Your code here
    #set an o and x counter to zero
    o_counter = 0
    x_counter = 0
#    Loop over each character in the string
for char in txt:
        #   do a check if it contains an 'x'
        if char == 'x'
        #      increment the x counter
            x_counter += 1
        # do a check if it contains an 'o'
        elif char =='o'
        #    increment the o counter
            o_counter += 1

    #check if x counter is equal to a counter
    if x_counter == o_counter:
     #   return true to the caller
        return True
    #otherwise
    else:
     #   return false to the caller
        return False


print(XO("ooxx")) # ➞ True
print(XO("xooxx")) # ➞ False
print(XO("ooxXm")) # ➞ True (Case insensitive)
print(XO("zpzpzpp")) # ➞ True (Returns True if no x and o)
print(XO("zzoo")) # ➞ False
