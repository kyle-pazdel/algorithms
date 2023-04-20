# create dictionaries from the first array (using one loop each), assigning True to as all values
# crate an empty array to be used in the next loop
# loop through the second array
# write a condition that weighs whether i in the second array is equivalent to True in the dictionary
# in that condition append the empty array with the i value
# return the appended array

first_array = [1, 2, 3, 4, 5]
{1: True, 2: True, 3: True, 4: True, 5: True}
second_array = [0, 2, 4, 6, 8]


def find_intersection(arr1, arr2):
    key = {}
    for i in arr1:
        key[i] = True
    res = []
    print(key.get(0, None))
    for j in arr2:
        if key.get(j, None):
            res.append(j)
    print(res)


find_intersection(first_array, second_array)
