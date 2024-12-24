def para_func (*para) :
    result = 0

    for num in para :
        result = result + num

    return result

hap = 0

hap = para_func(10, 20)
print("매개 변수 2개 호출: %d" % hap)
hap = para_func(10, 20, 30)
print("매개 변수 3개 호출: %d" % hap)