# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input().strip())
mset = set(map(int, input().strip().split()))
n = int(input().strip())
nset = set(map(int, input().strip().split()))

olist = list(mset.difference(nset).union(nset.difference(mset)))
olist.sort()
for item in olist:
    print(item)
