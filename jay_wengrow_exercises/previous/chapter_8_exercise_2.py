
# make a key dict from the array with all values set to zero using a loop
# incriment each value in the dict plus one for each instance of the element
# within this loop, if any value increments greater than one, return that value and break the loop

letters = ["a", "b", "c", "d", "c", "e", "f"]


# SOLUTION ONE
# def find_duplicate(arr):
#     key = {}
#     for i in arr:
#         key[i] = 0
#     for j in arr:
#         key[j] += 1
#         if key[j] > 1:
#             print(j)
#             return j


# SOLUTION TWO
def find_duplicate(arr):
    key = {}
    for i in arr:
        if key.get(i):
            print(i)
        else:
            key[i] = True


find_duplicate(letters)
