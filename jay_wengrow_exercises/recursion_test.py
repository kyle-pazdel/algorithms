def countdown(num):
    print(num)
    num -= 1
    if num < 0:
        return
    countdown(num)


countdown(10)
