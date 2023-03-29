arr = [4, 2, 7, 1, 3]


def select_sort(array):
    i = 0
    while i < len(array):
        lowest_number_index = i
        j = i + 1
        while j < len(array):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
            j += 1
        if lowest_number_index != i:
            temp = array[i]
            array[i] = array[lowest_number_index]
            array[lowest_number_index] = temp
        i += 1
    print(array)


select_sort(arr)
