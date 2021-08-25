import time

def remain(money):
    
    a = 0 # 500
    b = 0 # 100
    c = 0 # 50
    d = 0 # 10

    while(True):
        if money >= 500:
            money -= 500
            a += 1
        else:
            break
    while(True):
        if money >= 100:
            money -= 100
            b += 1
        else:
            break
    while(True):
        if money >= 50:
            money -=50
            c += 1
        else:
            break
    while(True):
        if money != 0:
            money -= 10
            d += 1
        else:
            break
    return a,b,c,d

money = input("돈을 입력하세요?")

start = time.time()

a,b,c,d = remain(int(money))
# if int(money) % 10 == 0:
# else :
    # print("금액을 잘못입력했습니다.")

end = time.time()

print("500원 {0} 100원 {1} 50원 {2} 10원 {3}".format(a,b,c,d))
print(end-start)

