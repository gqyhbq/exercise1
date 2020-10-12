import random
from Write_in import write_in
from fractions import Fraction

def cal(a, sign, b):  # 计算
    if (sign == '+'):
        return a + b
    elif (sign == '-'):
        return a - b
    elif (sign == '*'):
        return a * b
    else:
        return a / b

def Fractional_Calcu(i, r, signNum):  # faction calculate 分数计算
    # i是题目序号 signnum是符号数量 r数的范围
    fmRange = 10
    Range = 1
#    question = 'a'
#    answer = 'a'
    st = ('+', '-', '*', '/')
    if (signNum == 3):
        # 三运算符算式
        sign1 = st[random.randint(0, 3)]  # 随机得符号
        sign2 = st[random.randint(0, 3)]
        sign3 = st[random.randint(0, 3)]
        fm1 = random.randint(1, fmRange)  # 随机分数
        fz1 = random.randint(1, fmRange * Range)
        fm2 = random.randint(1, fmRange)
        fz2 = random.randint(1, fmRange * Range)
        fm3 = random.randint(1, fmRange)
        fz3 = random.randint(1, fmRange * Range)
        fm4 = random.randint(1, fmRange)
        fz4 = random.randint(1, fmRange * Range)

                f1 = Fraction(fz1, fm1)
        f2 = Fraction(fz2, fm2)
        f3 = Fraction(fz3, fm3)
        f4 = Fraction(fz4, fm4)

        if (sign1 == '/'):
            if (f1 > f2):
                Fractional_Calcu(i, r, signNum)
                return 0
            if (sign2 == '/'):
                if (int(cal(f1, sign1, f2)) > f3):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '/' and int(cal(cal(f1, sign1, f2), sign2, f3)) > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '-' and int(cal(cal(f1, sign1, f2), sign2, f3)) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
            elif (sign2 == '-'):
                if (sign3 == '+' and int(cal(f1, sign1, f2)) < f3):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '-'):
                    if (int(cal(f1, sign1, f2)) < f3):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                    if (int(cal(cal(f1, sign1, f2), sign2, f3)) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                if (sign3 == '*'):
                    if (cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                if (sign3 == '/'):
                    if (f3 > f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                    if (cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '+'):
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and f3 > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            else:
                if (sign3 == '-' or sign3 == '/'):
                    if (cal(cal(f1, sign1, f2), sign2, f3) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
        elif (sign1 == '-'):
            if (sign2 == '-'):
                if (sign3 == '-'):
                    if (f1 < f2 or cal(f1, sign1, f2) < f3 or (cal(cal(f1, sign1, f2), sign2, f3) < f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (f3 > f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                    else:
                        if (f1 < f2 or (cal(f1, sign1, f2) < f3)):
                            Fractional_Calcu(i, r, signNum)
                            return 0
                elif (sign3 == '*'):
                    if (f1 < f2 or cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                else:
                    if (f1 < f2 or cal(f1, sign1, f2) < f3):
                        Fractional_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '/'):
                if (sign3 == '/'):
                    if (f2 > f3 or cal(f2, sign2, f3) > f4 or f1 < cal(cal(f2, sign2, f3), sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '-'):
                    if (f2 > f3 or f1 < cal(f2, sign2, f3) or cal(cal(f1, sign1, f2), sign2, f3) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '+'):
                    if (f2 > f3 or f1 < cal(f2, sign2, f3)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                else:
                    if (f2 > f3 or f1 < cal(cal(f2, sign2, f3), sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '+'):
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(f1, sign1, f2), sign2, f3) > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    if (f1 < f2):
                        Fractional_Calcu(i, r, signNum)
                        return 0
            else:
                if (sign3 == '-'):
                    if (f1 < cal(f2, sign2, f3) or cal(cal(f1, sign1, f2), sign2, f3) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (f3 > f4 or f1 < cal(cal(f2, sign2, f3), sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '+'):
                    if (f1 < cal(f2, sign2, f3)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                else:
                    if (f1 < cal(cal(f2, sign2, f3), sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
        elif (sign1 == '+'):
            if (sign2 == '+'):
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(f1, sign1, f2), sign2, f3) > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            elif (sign2 == '-'):
                if (sign3 == '-'):
                    if (cal(f1, sign1, f2) < f3 or cal(cal(f1, sign1, f2), sign2, f3) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (f3 > f4 or cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '*'):
                    if (cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                else:
                    if (cal(f1, sign1, f2) < f3):
                        Fractional_Calcu(i, r, signNum)
                        return 0
            elif (sign2 == '*'):
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(f1, sign1, f2), sign2, f3) > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            else:
                if (sign3 == '-'):
                    if (cal(f1, sign1, f2) > f3 or cal(cal(f1, sign1, f2), sign2, f3) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '/'):
                    if (cal(f1, sign1, f2) > f3 or cal(cal(f1, sign1, f2), sign2, f3) > f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                else:
                    if (cal(f1, sign1, f2) > f3):
                        Fractional_Calcu(i, r, signNum)
                        return 0
        else:
            if (sign2 == '+'):
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and f3 < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            elif (sign2 == '-'):
                if (sign3 == '+' and cal(f1, sign1, f2) < f3):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '-'):
                    if (cal(f1, sign1, f2) < f3 or cal(cal(f1, sign1, f2), sign2, f3) < f4):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                elif (sign3 == '*' and cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/'):
                    if (f3 > f4 or cal(f1, sign1, f2) < cal(f3, sign3, f4)):
                        Fractional_Calcu(i, r, signNum)
                        return 0
                else:
                    pass
            elif (sign2 == '*'):
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(f1, sign1, f2), sign2, f3) > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    pass
            else:
                if (cal(f1, sign1, f2) > f3):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                if (sign3 == '-' and cal(cal(f1, sign1, f2), sign2, f3) < f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                elif (sign3 == '/' and cal(cal(f1, sign1, f2), sign2, f3) > f4):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                else:
                    pass

                    # 按运算符优先顺序分类

                # 计算
                
        if (sign1 == '*' or sign1 == '/'):
            if (sign2 == '*' or sign2 == '/'):
                answer = cal(cal(cal(f1, sign1, f2), sign2, f3), sign3, f4)
            else:
                if (sign3 == '*' or sign3 == '/'):
                    answer = cal(cal(f1, sign1, f2), sign2, cal(f3, sign3, f4))
                else:
                    answer = cal(cal(cal(f1, sign1, f2), sign2, f3), sign3, f4)
        else:
            if (sign2 == '*' or sign2 == '/'):
                if (sign3 == '*' or sign3 == '/'):
                    answer = cal(f1, sign1, cal(cal(f2, sign2, f3), sign3, f4))
                else:
                    answer = cal(cal(f1, sign1, cal(f2, sign2, f3)), sign3, f3)
            else:
                if (sign3 == '*' or sign3 == '/'):
                    answer = cal(cal(f1, sign1, f2), sign2, cal(f3, sign3, f4))
                else:
                    answer = cal(cal(cal(f1, sign1, f2), sign2, f3), sign3, f4)

        print('第', i, '题', end=": ")

        question = '(', fz1, '/', fm1, ')', sign1, '(', fz2, '/', fm2, ')', sign2, '(', fz3, '/', fm3, ')' \
            , sign3, '(', fz4, '/', fm4, ')'
        question = "".join('%s' % id for id in question)
        question = question.replace("/", "÷").replace("*", "×")
        print(question, end=' = ')
        
    elif (signNum == 2):  # 两运算符算式
        sign1 = st[random.randint(0, 3)]  # 随机得符号
        sign2 = st[random.randint(0, 3)]
        fm1 = random.randint(1, fmRange)  # 随机分数
        fz1 = random.randint(1, fmRange * Range)
        fm2 = random.randint(1, fmRange)
        fz2 = random.randint(1, fmRange * Range)
        fm3 = random.randint(1, fmRange)
        fz3 = random.randint(1, fmRange * Range)
        
        f1 = Fraction(fz1, fm1)
        f2 = Fraction(fz2, fm2)
        f3 = Fraction(fz3, fm3)

        if (sign1 == '/'):  # 伪随机
            if (f1 > f2):
                Fractional_Calcu(i, r, signNum)
                return 0
            if (sign2 == '-' and int(cal(f1, sign1, f2)) < f3):
                Fractional_Calcu(i, r, signNum)
                return 0
            if (sign2 == '/' and int(cal(f1, sign1, f2)) > f3):
                Fractional_Calcu(i, r, signNum)
                return 0
        elif (sign1 == '-'):
            if (sign2 == '+' and f1 < f2):
                Fractional_Calcu(i, r, signNum)
                return 0
            if (sign2 == '-'):
                if (f1 < f2):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                if (int(cal(f1, sign1, f2) < f3)):
                    Fractional_Calcu(i, r, signNum)
                    return 0
            if (sign2 == '*' and f1 < int(cal(f2, sign2, f3))):
                Fractional_Calcu(i, r, signNum)
                return 0
            if (sign2 == '/'):
                if (f2 > f3):
                    Fractional_Calcu(i, r, signNum)
                    return 0
                if (f1 < int(cal(f2, sign2, f3))):
                    Fractional_Calcu(i, r, signNum)
                    return 0
        elif(sign1 == '*'):
            if (sign2 == '-' and cal(f1, sign1, f2) < f3):
                Fractional_Calcu(i, r, signNum)
                return 0
            if ((sign2 == '/' and cal(f1, sign2, f2) > f3)):
                Fractional_Calcu(i, r, signNum)
                return 0
        else:
            if (sign2 == '-' and cal(f1, sign1, f2) < f3):
                Fractional_Calcu(i, r, signNum)
                return 0
            if ((sign2 == '/' and f2 > f3)):
                Fractional_Calcu(i, r, signNum)
                return 0

        if( sign1 == '*' or sign1 =='/'):                           #计算
            answer = cal( cal(f1,sign1,f2) , sign2 , f3 )
        else:
             if(sign2 == '*' or sign2 =='/'):
                answer = cal(f1,sign1,cal(f2,sign2,f3))
            else:
                answer= cal(cal(f1,sign1,f2),sign2,f3)
                
        print('第', i, '题', end=": ")
        question = '(', fz1, '/', fm1, ')', sign1, '(', fz2, '/', fm2, ')', sign2, '(', fz3, '/', fm3, ')'
        question = "".join('%s' % id for id in question)
        question = question.replace("/", "÷").replace("*", "×")
        print(question, end=' = ')

    else:  # 一运算符算式
        sign1 = st[random.randint(0, 3)]  # 随机得符号
        fm1 = random.randint(1, fmRange)  # 随机分数   分母fm  分子fz
        fz1 = random.randint(1, fmRange * Range)
        fm2 = random.randint(1, fmRange)
        fz2 = random.randint(1, fmRange * Range)

        f1 = Fraction(fz1, fm1)  # 得两分数
        f2 = Fraction(fz2, fm2)

        if (sign1 == '-' and f1 < f2):  # 伪随机
            Fractional_Calcu(i, r, signNum)
        if (sign1 == '/' and f1 > f2):
            Fractional_Calcu(i, r, signNum)
        print('第', i, '题', end=": ")
        answer = cal(f1, sign1, f2)  # 得结果
        question = '(', fz1, '/', fm1, ')', sign1, '(', fz2, '/', fm2, ')'
        question = "".join('%s' % id for id in question)
        question = question.replace("/", "÷").replace("*", "×")
        print(question, end=' = ')


    if (answer % 1):  # 判断计算结果是否是整数
        if (answer > 1):
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
            if(fz>fm):
                num = fz // fm
                fz = fz % fm

            print(str(num) + '`' + str(fz) + '/' + str(fm))
            answer = str(num) + '`' + str(fz) + '/' + str(fm)
            write_in(i, question, answer)

        else:
            print(answer)
            write_in(i, question, str(answer))
    else:
        print(answer)
        write_in(i, question, str(answer)) 
