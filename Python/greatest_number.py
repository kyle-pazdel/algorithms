# Rewrite this aglorithm to have a time complexity of O(N) instead of O(N^2)

arr = [1, 2, 3, 10, 4, 5, 6]
arr2 = [100, 345, 23455, 2341, 20, 2, 35, 0]

# O(N*2) Method


def greatestNumber(array):
    for i in array:
        isIValTheGreatest = True
        for j in array:
            if j > i:
                isIValTheGreatest = False
        if isIValTheGreatest:
            print(i)
            return i


greatestNumber(arr)
greatestNumber(arr2)

# O(N) Method


def greatest_number(array):
    greatest_number = array[0]
    for i in array:
        if i > greatest_number:
            greatest_number = i
    print(greatest_number)
    return greatest_number


greatest_number(arr)
greatest_number(arr2)
