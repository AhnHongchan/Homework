path = []
used = [False for _ in range(3)]

def KFC(x):
    if x == 2:
        print(path)
        return
    
    for i in range(3):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = False
KFC(0)