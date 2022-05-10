if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    maxNum = -100
    result = -100
    for i in range(0, n):
        if(arr[i] > maxNum):
            maxNum = arr[i]

    for i in range(0, n):
        if(arr[i] > result and arr[i] < maxNum):
            result = arr[i]

    print(result)
