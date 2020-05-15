def function1(x,y):
    #function2(3.4)
    print(function2(3.4)) #可得到結果
def function2(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1

print(function1(2,3))#不管甚麼功能，只要print沒有return的函式都會出現None

print(function2(3.4))