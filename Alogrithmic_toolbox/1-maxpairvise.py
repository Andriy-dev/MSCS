def max2(dataset):
    max2=[None,None]
    for current in dataset:
        if max2[0] is None:
            max2[0] = current
        else:
            if current > max2[0]:
                current, max2[0] = max2[0],current
            if max2[1] is None:
                max2[1] = current
            else:
                if current > max2[1]:
                    max2[1] = current
    return max2

if __name__ == "__main__":
    dataset = map(int,input().split())
    m = max2(dataset)

    print (m[0]*m[1])
