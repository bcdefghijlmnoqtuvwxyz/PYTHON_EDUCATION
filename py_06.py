ch = ""
a, b = 0, 0

while True :
    a = int(input("계산할 첫 번째 수: "))
    b = int(input("계산할 두 번째 수: "))
    ch = input("계산할 연산자 입력: ")

    if(ch == "+") :
        print("%d + %d = %d" % (a, b, a + b))
    elif(ch == "-") :
        print("%d - %d = %d" % (a, b, a - b))
    elif(ch == "*") :
        print("%d * %d = %d" % (a, b, a * b))
    elif(ch == "/") :
        print("%d / %d = %d" % (a, b, a / b))
    elif(ch == "%") :
        print("%d %% %d = %d" % (a, b, a % b)) 
    elif(ch == "//") :
        print("%d // %d = %d" % (a, b, a // b))
    elif(ch == "**") :
        print("%d ** %d = %d" % (a, b, a ** b))      
    else :
        print("연산자 입력 오류")