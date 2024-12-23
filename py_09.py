myList = [30, 10, 20]
print("현재 리스트: %s" % myList)

myList.append(40)
print("append(40) 후의 리스트: %s" % myList) # [30, 10, 20, 40]

print("pop()으로 추출한 값: %s" % myList.pop()) # 40
print("pop() 후의 리스트: %s" % myList) # [30, 10, 20]

myList.sort() # 오름차순 정렬
print("%s" % myList) # [10, 20, 30]

myList.reverse() # 내림차순 정렬
print("%s" % myList) # [30, 20, 10]

print("20값의 위치: %d" % myList.index(20)) # 1

myList.insert(2, 222) 
print("%s" % myList) # [30, 20, 222, 10]

myList.remove(222)
print("%s" % myList) # [30, 20, 10]

myList.extend([77, 88, 77])
print("%s" % myList) # [30, 20, 10, 77, 88, 77]

print("77값의 개수: %d" % myList.count(77)) # 2

myList = [30, 10, 20]
newList = sorted(myList)
print("%s" % myList)
print("%s" % newList)