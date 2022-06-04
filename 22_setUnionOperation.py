# Enter your code here. Read input from STDIN. Print output to STDOUT
nEnglish = int(input().strip())
engSet = set(map(int, input().strip().split()))

nFrench = int(input().strip())
freSet = set(map(int, input().strip().split()))

print(len(engSet.union(freSet)))
