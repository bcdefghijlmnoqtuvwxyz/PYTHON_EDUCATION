def myFunc() :
    print('함수 호출')

gVar = 100 # 전역 변수 선언

##메인 코드 부분##
if __name__ == '__main__':
    print('메인 함수 부분 실행')
    myFunc()
    print('전역 변수 값: ', gVar)

