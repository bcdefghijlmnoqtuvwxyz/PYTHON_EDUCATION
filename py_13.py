def func1() :
    global a # 이 함수 안에서 a는 전역 변수
    a = 10
    print("func1()의 a 값: %d" % a)

def func2() :
    print("func2()의 a 값: %d" % a)

# a = 20 

func1()
func2()