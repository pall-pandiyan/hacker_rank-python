if __name__ == '__main__':
    n = int(input())

    if((n % 2) != 0):
        print("Weird")
    else:
        if((n > 1) and (n < 6)):
            print("Not Weird")
        if((n > 5) and (n < 21)):
            print("Weird")
        if(n > 20):
            print("Not Weird")
