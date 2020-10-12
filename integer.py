import random
from Write_in import write_in
from fractions import Fraction

def cal(a, sign, b):  # 一运算符计算
    if (sign == '+'):
        return a + b
    elif (sign == '-'):
        return a - b
    elif (sign == '*'):
        return a * b
    else:
        return a / b

def Integer_Calcu(i, r, signNum):  # 整数计算
    # i是题目编号 r是范围 signnum是字符数量
    st = ("+", "-", "*", "/")
    question = 'a'
    answer = 'a'
    if (signNum == 3):
        # 三运算符算式
        num1 = Fraction(random.randint(1, r))
        num2 = Fraction(random.randint(1, r))
        num3 = Fraction(random.randint(1, r))
        num4 = Fraction(random.randint(1, r))
        sign1 = st[random.randint(0, 3)]
        sign2 = st[random.randint(0, 3)]
        sign3 = st[random.randint(0, 3)]
        if (sign1 == '/'):
            if (num1 > num2):
                Integer_Calcu(i, r, signNum)
                return 0
            if (sign2 == '/'):
                if (int(cal(num1, sign1, num2)) > num3):
                    Integer_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '/' and int(cal(cal(num1, sign1, num2), sign2, num3)) > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '-' and int(cal(cal(num1, sign1, num2), sign2, num3)) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
            elif (sign2 == '-'):
                if (sign3 == '+' and int(cal(num1, sign1, num2)) < num3):
                    Integer_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '-'):
                    if (int(cal(num1, sign1, num2)) < num3):
                        Integer_Calcu(i, r, signNum)
                        return 0
                    if (int(cal(cal(num1, sign1, num2), sign2, num3)) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                if (sign3 == '*'):
                    if (cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                if (sign3 == '/'):
                    if (num3 > num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                    if (cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '+'):
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and num3 > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            else:
                if (sign3 == '-' or sign3 == '/'):
                    if (cal(cal(num1, sign1, num2), sign2, num3) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
        elif (sign1 == '-'):
            if (sign2 == '-'):
                if (sign3 == '-'):
                    if (num1 < num2 or cal(num1, sign1, num2) < num3 or (
                            cal(cal(num1, sign1, num2), sign2, num3) < num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (num3 > num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                    else:
                        if (num1 < num2 or (cal(num1, sign1, num2) < num3)):
                            Integer_Calcu(i, r, signNum)
                            return 0
                elif (sign3 == '*'):
                    if (num1 < num2 or cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                else:
                    if (num1 < num2 or cal(num1, sign1, num2) < num3):
                        Integer_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '/'):
                if (sign3 == '/'):
                    if (num2 > num3 or cal(num2, sign2, num3) > num4 or num1 < cal(cal(num2, sign2, num3), sign3,
                                                                                   num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '-'):
                    if (num2 > num3 or num1 < cal(num2, sign2, num3) or cal(cal(num1, sign1, num2), sign2,
                                                                            num3) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '+'):
                    if (num2 > num3 or num1 < cal(num2, sign2, num3)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                else:
                    if (num2 > num3 or num1 < cal(cal(num2, sign2, num3), sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '+'):
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(num1, sign1, num2), sign2, num3) > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    if (num1 < num2):
                        Integer_Calcu(i, r, signNum)
                        return 0
            else:
                if (sign3 == '-'):
                    if (num1 < cal(num2, sign2, num3) or cal(cal(num1, sign1, num2), sign2, num3) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (num3 > num4 or num1 < cal(cal(num2, sign2, num3), sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '+'):
                    if (num1 < cal(num2, sign2, num3)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                else:
                    if (num1 < cal(cal(num2, sign2, num3), sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
        elif (sign1 == '+'):
            if (sign2 == '+'):
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(num1, sign1, num2), sign2, num3) > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            elif (sign2 == '-'):
                if (sign3 == '-'):
                    if (cal(num1, sign1, num2) < num3 or cal(cal(num1, sign1, num2), sign2, num3) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (num3 > num4 or cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '*'):
                    if (cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                else:
                    if (cal(num1, sign1, num2) < num3):
                        Integer_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '*'):
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(num1, sign1, num2), sign2, num3) > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            else:
                if (sign3 == '-'):
                    if (cal(num1, sign1, num2) > num3 or cal(cal(num1, sign1, num2), sign2, num3) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (cal(num1, sign1, num2) > num3 or cal(cal(num1, sign1, num2), sign2, num3) > num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                else:
                    if (cal(num1, sign1, num2) > num3):
                        Integer_Calcu(i, r, signNum)
                        return 0
        else:
            if (sign2 == '+'):
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and num3 < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            elif (sign2 == '-'):
                if (sign3 == '+' and cal(num1, sign1, num2) < num3):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '-'):
                    if (cal(num1, sign1, num2) < num3 or cal(cal(num1, sign1, num2), sign2, num3) < num4):
                        Integer_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '*' and cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/'):
                    if (num3 > num4 or cal(num1, sign1, num2) < cal(num3, sign3, num4)):
                        Integer_Calcu(i, r, signNum)
                        return 0
                else:
                    pass
            elif (sign2 == '*'):
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(num1, sign1, num2), sign2, num3) > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            else:
                if (cal(num1, sign1, num2) > num3):
                    Integer_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '-' and cal(cal(num1, sign1, num2), sign2, num3) < num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(num1, sign1, num2), sign2, num3) > num4):
                    Integer_Calcu(i, r, signNum)
                    return 0
                else:
                    pass

                # 计算
        if (sign1 == '*' or sign1 == '/'):
            if (sign2 == '*' or sign2 == '/'):
                answer = cal(cal(cal(num1, sign1, num2), sign2, num3), sign3, num4)
            else:
                if (sign3 == '*' or sign3 == '/'):
                    answer = cal(cal(num1, sign1, num2), sign2, cal(num3, sign3, num4))
                else:
                    answer = cal(cal(cal(num1, sign1, num2), sign2, num3), sign3, num4)
        else:
            if (sign2 == '*' or sign2 == '/'):
                if (sign3 == '*' or sign3 == '/'):
                    answer = cal(num1, sign1, cal(cal(num2, sign2, num3), sign3, num4))
                else:
                    answer = cal(cal(num1, sign1, cal(num2, sign2, num3)), sign3, num3)
            else:
                if (sign3 == '*' or sign3 == '/'):
                    answer = cal(cal(num1, sign1, num2), sign2, cal(num3, sign3, num4))
                else:
                    answer = cal(cal(cal(num1, sign1, num2), sign2, num3), sign3, num4)


        print("第", i, '题: ' + str(num1) + sign1 + str(num2) + sign2 + str(num3) + sign3 + str(num4), end=" = ")
        question = str(num1) + sign1 + str(num2) + sign2 + str(num3) + sign3 + str(num4)

    elif (signNum == 2):
        # 双运算符算式
        num1 = Fraction(random.randint(1, r))
        num2 = Fraction(random.randint(1, r))
        num3 = Fraction(random.randint(1, r))
        sign1 = st[random.randint(0, 3)]
        sign2 = st[random.randint(0, 3)]
        
        if(sign1 == '/'):              #伪随机
            if(num1>num2):
                Integer_Calcu(i, r, signNum)
                return 0
            if(sign2 == '-' and int(cal(num1,sign1,num2))<num3):
                Integer_Calcu(i, r, signNum)
                return 0
            if(sign2 == '/' and int(cal(num1,sign1,num2))>num3):
                Integer_Calcu(i, r, signNum)
                return 0
        elif(sign1 == '-'):
            if(sign2 == '+'  and num1<num2):
                Integer_Calcu(i, r, signNum)
                return 0
            if(sign2 == '-'):
                if(num1<num2):
                    Integer_Calcu(i, r, signNum)
                    return 0
                if(int(cal(num1,sign1,num2)<num3)):
                    Integer_Calcu(i, r, signNum)
                    return 0
            if(sign2 == '*' and num1<int(cal(num2,sign2,num3))):
                Integer_Calcu(i, r, signNum)
                return 0
            if(sign2 == '/'):
                if(num2>num3):
                    Integer_Calcu(i, r, signNum)
                    return 0
                if(num1<int(cal(num2,sign2,num3))):
                    Integer_Calcu(i, r, signNum)
                    return 0
        elif(sign1 == '*'):
            if(sign2 == '-' and cal(num1,sign1,num2) < num3):
                Integer_Calcu(i, r, signNum)
                return 0
            if((sign2 == '/' and cal(num1,sign2,num2) > num3)):
                Integer_Calcu(i, r, signNum)
                return 0
        else:
            if (sign2 == '-' and cal(num1, sign1, num2) < num3):
                Integer_Calcu(i, r, signNum)
                return 0
            if ((sign2 == '/' and num2 > num3)):
                Integer_Calcu(i, r, signNum)
                return 0

        if (sign1 == '*' or sign1 == '/'):                   # 计算
            answer = cal(cal(num1, sign1, num2), sign2, num3)
        else:
            if (sign2 == '*' or sign2 == '/'):
                answer = cal(num1, sign1, cal(num2, sign2, num3))
            else:
                answer= cal(cal(num1, sign1, num2), sign2, num3)

        question = str(num1) + sign1 + str(num2) + sign2 + str(num3)
        print("第", i, '题: ' + str(num1) + sign1 + str(num2) + sign2 + str(num3), end=" = ")

    else:
        # 单运算符

        num1 = Fraction(random.randint(1, r))
        num2 = Fraction(random.randint(1, r))
        sign1 = st[random.randint(0, 3)]

        if (sign1 == '-' and num1 < num2):  # 伪随机
            Integer_Calcu(i, r, signNum)
        if (sign1 == '/' and num1 > num2):
            Integer_Calcu(i, r, signNum)

        question = str(num1) + sign1 + str(num2)
        answer = cal(num1, sign1, num2)
        print("第", i, '题: ' + str(num1) + sign1 + str(num2), end=" = ")

    # 化为带分数
    if (answer % 1):  # 判断计算结果是否是整数
        if (answer > 1):  # 正数
            n = str(answer).index('/')  # 找出 除号的位置来当分界符  得到分子和分母
            t = 0
            fz = 0
            fm = 0
            l = len(str(answer))
            while (t < n):  # 分子
                fz = int(str(answer)[t]) + fz * 10
                t = t + 1

            t = t + 1  # 跳过 '/'

            while (t < l):  # 得分母
                fm = int(str(answer)[t]) + fm * 10
                t = t + 1

            num = 0
            if (fz > fm):
                num = fz // fm
                fz = fz % fm
            answer = str(num) + '`' + str(fz) + '/' + str(fm)
            write_in(i, question, answer)
            print(answer)

        elif (answer < -1):
            n = str(answer).index('/')  # 找出 除号的位置来当分界符  得到分子和分母
            t = 1  # 0是负号
            fz = 0
            fm = 0
            l = len(str(answer))
            while (t < n):  # 分子
                fz = int(str(answer)[t]) + fz * 10
                t = t + 1

            t = t + 1  # 跳过 '/'

            while (t < l):  # 得分母
                fm = int(str(answer)[t]) + fm * 10
                t = t + 1

            num = 0
            if (fz > fm):
                num = fz // fm
                fz = fz % fm

            answer = '-' + str(num) + '`' + str(fz) + '/' + str(fm)
            write_in(i, question, answer)
            print(answer)
        else:
            write_in(i, question, str(answer))
            print(answer)
    else:
        write_in(i, question, str(answer))
        print(answer)

'''      记录下用的  join  和  eval
def Integer_Calcu(i,r,signNum):    #整数计算
    #i是题目编号 r是范围 signnum是字符数量
    st = ("+", "-", "*", "/")
    else:
    #单运算符算式
        print("第",i,'题',end=": ")
        num1 = random.randint(1, r)
        num2 = random.randint(1, r)
        sign1 = st[random.randint(0, 3)]
        
        if(sign1 == '-' and num1 < num2 ):      #改动
            Integer_Calcu(i, r, 1)
        elif(sign1 == '/' and  num1 > num2 ):
            Integer_Calcu(i, r, 1)
        else:
            b = [str(num1), sign1, str(num2)]   #改动结束
            
    g = ''.join(b)
    print(g, end='=', )
    final = float(eval(g))
    print("%.*f" % (3,final))
    write_in(i, g, str(final))
