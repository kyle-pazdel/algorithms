def greatestNumber(array):
    greatest = array[0]
    for i in array:
        if i > greatest:
            greatest = i
    return greatest


print(greatestNumber([1, 56, 3, 8, 768, 21]))
