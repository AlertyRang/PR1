actCount = input("Введите количество действий: ")
start = 0

while actCount != 0:
    if(start == 0):
        final = float(input("Введите число: "))
        act = input("Введите действие: ")
        y = float(input("Введите следующие число: "))
        start = start + 1
    else:
        act = input("Введите действие: ")
        y = float(input("Введите следующие число: "))
    
    if(act == "+"):
        final = final + y
    elif(act == "-"):
        final =  final - y
    elif(act == "*"):
        final = final * y
    elif(act == "/"):
        if(y == 0):
            print("На ноль делить нельзя!")
            break
        else:
            final = final / y
    elif(act == "%"):
        if(y == 0):
            print("На ноль делить нельзя!")
            break
        else:
            final = final % y
    elif(act == "**"):
        final = pow( final, y)
    else:
        print("Введено некоректное действие!")
    actCount = int(actCount) - 1

print(final)