num=int(input("Enter the number :"))
factorial=1
def fact(num):
    for i in range(num,1,--1):
        factorial=factorial*num
        num-=1
    return factorial


print("Factorial is :",fact(num))
