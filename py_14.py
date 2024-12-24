def multi(v1, v2) :
    retList = [] # 리스트 선언
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1) # 요소 추가
    retList.append(res2)
    return retList

myList = []
hap, sub = 0, 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]

print("Multi()에서 돌려준 값: %d, %d" % (hap, sub))