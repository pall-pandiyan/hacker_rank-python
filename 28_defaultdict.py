from collections import defaultdict
inputs = input().split(' ')
an = int(inputs[0])
bn = int(inputs[1])

d = defaultdict(list)

for i in range(an):
    d['A'].append(input())
print(d['A'])

for i in range(bn):
    d['B'].append(input())
print(d['A'])

exit

result_str = ''
for i in d['B']:
    current_line = ''
    for k,v in enumerate(d['A']):
        print('i,v', i,v)
        if i == v:
            print('k+1:', k+1)
            current_line = current_line + str(k+1) + ' '
    if current_line:
        result_str = result_str + current_line.rstrip() + '\n'
        current_line = ''
    else:
        result_str = result_str + '\n-1'
print(result_str)
