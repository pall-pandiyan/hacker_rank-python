def sortSum(arr):
    print(arr)
    result = arr[0]
    for i in range(1, len(arr)):
        s = arr[:i+1]
        s.sort()
        result += s[0]
        for j in range(1,len(s)):
            result += s[j] * (j+1)
    return result

def main():
    print("Enter number of array:", end=" ")
    n = int(input().strip())
    print("Please enter the array:", end=" ")
    arr = list(map(int, input().strip().split()))
    print("\nResult is:",sortSum(arr))

if __name__=="__main__":
    main()
