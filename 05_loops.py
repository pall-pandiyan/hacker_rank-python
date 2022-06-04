if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i*i)


def is_leap(year):
    leap = False

    if (year % 4 == 0):
        leap = True
        if(year % 100 == 0):
            if(year % 400 == 0):
                leap = True
            else:
                leap = False

    return leap
