#
# create a counts dictionary
# iterate over string and assign a value of 0 to each character as a key value pair in the dictionary
# iterate over the string again and incriment the values by one
# iterate over the stirng again and return a value if it's count is one

string = "minimum"


def find_single(string):
    counts = {}
    for i in string:
        counts[i] = 0
    for j in string:
        counts[j] += 1
    for k in string:
        if counts[k] == 1:
            print(k)
            return (k)


find_single(string)
