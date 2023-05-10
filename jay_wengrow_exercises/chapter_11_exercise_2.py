def even_numbers(array, result=[]):
    if array[0] % 2 == 0:
        result.append(array[0])
    if len(array) == 1:
        return result
    even_array = even_numbers(array[1:])


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers(array)
