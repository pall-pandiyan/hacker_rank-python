if __name__ == '__main__':
    slist = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        slist.append([score, name])
    slist.sort()

    nlist = list()
    for i in slist:
        nlist.append(i[0])

    fmin = nlist[0]
    for i in range(1, len(nlist)):
        smin = nlist[i]
        sminInd = i
        if(smin > fmin):
            break
    sminCount = nlist.count(smin)

    # print(fmin)
    # print(smin)
    # print(sminInd)
    # print(sminCount)

    olist = list()
    for i in range(sminInd, sminInd+sminCount):
        olist.append(slist[i][1])
    olist.sort()

    for i in olist:
        print(i)
