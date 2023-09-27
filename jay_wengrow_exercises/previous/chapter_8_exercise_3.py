# create a dictionary with all letters of the alphabet as keys with values of True
# split the string into an array
# iterate over the new array with a loop
# within use .get method to return the value if it throws a key exception

string = "the quick brown box jumps over a lazy dog"


def return_missing_letter(string):
    key = "abcdefghijklmnopqrstuvqxyz"
    chars = {}
    arr = list(string.replace(" ", ""))
    for i in arr:
        chars[i] = True
    for j in key:
        try:
            none = chars[j]
        except KeyError as ke:
            print(ke)


return_missing_letter(string)
