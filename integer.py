import random
from Write_in import write_in

def Integer_Calcu(i,r,signNum):    #整数计算
    #i是题目编号 r是范围 signnum是字符数量
    st = ("+", "-", "*", "/")
    if(signNum == 3):
    # 三运算符算式
        print("第",i,'题',end=": ")
        num1 = random.randint(1, r)
        num2 = random.randint(1, r)
        num3 = random.randint(1, r)
        num4 = random.randint(1, r)
        sign1 = st[random.randint(0, 3)]
        sign2 = st[random.randint(0, 3)]
        sign3 = st[random.randint(0, 3)]
        b = [str(num1), sign1, str(num2), sign2, str(num3), sign3, str(num4)]
    elif(signNum == 2):
    #双运算符算式
        print("第",i,'题',end=": ")
        num1 = random.randint(1, r)
        num2 = random.randint(1, r)
        num3 = random.randint(1, r)
        sign1 = st[random.randint(0, 3)]
        sign2 = st[random.randint(0, 3)]
        b = [str(num1), sign1, str(num2), sign2, str(num3)]
    else:
    #单运算符算式
        print("第",i,'题',end=": ")
        num1 = random.randint(1, r)
        num2 = random.randint(1, r)
        sign1 = st[random.randint(0, 3)]
        b = [str(num1), sign1, str(num2)]
    g = ''.join(b)
    print(g, end='=', )
    final = float(eval(g))
    print("%.*f" % (3,final))
    write_in(i, g, str(final))
