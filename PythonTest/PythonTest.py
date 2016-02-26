import datetime
import random
def task1():
    name=input("Ваше имя: ")
    age=int(input("Ваш возраст: "))
    num=int(input("Введите число повторений: "))
    for i in range(num):
        print("В %d году Вам будет 100 лет"%(datetime.date.today().year+100-age))

def task2():
    number=int(input("Введите целое число: "))
    if number%2==1:
        print("Число %s нечетное"%number)
    else:
        print("Число %s четное"%number)
        if number%4==0:
            print("Число %s делится на 4"%number)
        else:
            print("Число %s не делится на 4"%number)
    number1=int(input("Введите ещё одно целое число: "))
    if number%number1==0:
        print("Число %s делится на %s"%(number,number1))
    if number1%number==0:
        print("Число %s делится на %s"%(number1,number))

def task3():
    a=[1,1,2,3,5,8,13,21,34,55,69]
    #c=[]
    d=[]
    c=filter(lambda x: x<20,a)
    for b in a:
        if b>5:
            print(b)
        if b<20:
            d.append(b)
    for a in c:
        print(a,end = " ")
    print()
    print(d)

def task4():
    num=int(input("Введите целое число: "))
    max=int(num**0.5)
    divs=[]
    for a in range(1,max+1):
        if num%a==0:
            divs.append(a)
            if a!=num/a:
                divs.append(int(num/a))
    divs.sort()
    print("Делители числа %d: "%num)
    for a in divs:
        print(a,end = " ")
    print()
def task5():
    random.seed()
    a=[]
    b=[]
    for i in range(15):
        a.append(random.randint(0,99))
        b.append(random.randint(0,99))
    a=set(a)
    b=set(b)
    print(a)
    print(b)
    print("Пересечение множеств:")
    print(a&b)
    print("Объединение множеств:")
    print(a|b)
task=1
while task!=0:
    task=int(input("Номер задания (0-выход): "))
    if task==1:
        task1()
    if task==2:
        task2()
    if task==3:
        task3()
    if task==4:
        task4()
    if task==5:
        task5()