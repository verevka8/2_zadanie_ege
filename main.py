import itertools, fnmatch
def f1(a,i):
    a = sorted(a)
    w, x, y, z = a[0][i],a[1][i],a[2][i],a[3][i]
    return int((x <= y) and ((not(w)) == z))
def f2(a,i):
    a = sorted(a)
    w, x, y, z = a[0][i], a[1][i], a[2][i], a[3][i]
    return int((x <= y) == (w or (not(z))))


res = [["z"],["y"],["x"],["w"]]
maska = [
    "?101?0",
    "?0000?",
    "0?0001"]
checker = [0,0,0]

for x in (0,1):
    for y in (0,1):
        for w in (0,1):
            for z in (0,1):
                res[0].append(z), res[1].append(y), res[2].append(x),res[3].append(w)

res = list(itertools.permutations(res,4))
for l in res:
    for i in range(1,len(l[0])):
        s = str(l[0][i]) + str(l[1][i]) + str(l[2][i]) + str(l[3][i]) + str(f1(l,i)) + str(f2(l,i))
        for j in range(len(maska)):
            if fnmatch.fnmatch(s,maska[j]):
                checker[j] = 1
                break
    if sum(checker) == 3:
        print(l[0][0],l[1][0],l[2][0],l[3][0])
    checker = [0,0,0]



