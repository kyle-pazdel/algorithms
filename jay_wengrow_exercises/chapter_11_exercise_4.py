def find_x(string, ind=0):
    if string[0].lower() == "x":
        print(ind)
        return ind
    return find_x(string[1:], ind + 1)


string = "abcdefghijklmnopqrstuvwxyz"

find_x(string)
