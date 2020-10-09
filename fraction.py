import random
from Write_in import write_in
from fractions import Fraction

def cal(a,sign,b):             #计算
    if(sign == '+'):
        return  a+b
    elif(sign == '-'):
        return  a-b
    elif(sign == '*'):
        return a*b
    else:
        return a/b

def Fractional_Calcu(i,r,signNum):  #faction calculate 分数计算
    # i是题目序号 signnum是符号数量 r是数的范围
    fmRange = r
    Range = r
    question='a'
    answer='a'
    st = ('+', '-', '*', '/')
    print('第', i, '题', end=": ")
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

        f1 = Fraction(fz1,fm1)
        f2 = Fraction(fz2,fm2)
        f3 = Fraction(fz3,fm3)
        f4 = Fraction(fz4,fm4)
        #按运算符优先顺序分类
        if((sign2 == '*' or sign2 == '/')  and (sign1 == '+' or sign1=='-')):           #231
            answer = cal(f1,sign1, cal( cal(f2,sign2,f3),sign3,f4))
        elif((sign3 == '*' or sign3 =='/' ) and ( sign2 == '+' or sign2 == '-')):       #312
            answer = cal( cal(f1,sign1,f2),sign2, (cal(f3, sign3,f4) ) )
        else:                                                         #123
            answer = cal( cal( cal(f1,sign1,f2),sign2,f3),sign3,f3)

        question = '(', fz1, '/', fm1, ')', sign1, '(', fz2, '/', fm2, ')', sign2, '(', fz3, '/', fm3, ')' \
            , sign3, '(', fz4, '/', fm4, ')'
        question = "".join('%s' %id for id in question)
        print(question.replace("/", "÷").replace("*", "×"), end=' = ')

    elif (signNum == 2):  # 两运算符算式
        sign1 = st[random.randint(0, 3)]  # 随机得符号
        sign2 = st[random.randint(0, 3)]
        fm1 = random.randint(1, fmRange)  # 随机分数
        fz1 = random.randint(1, fmRange * Range)
        fm2 = random.randint(1, fmRange)
        fz2 = random.randint(1, fmRange * Range)
        fm3 = random.randint(1, fmRange)
        fz3 = random.randint(1, fmRange * Range)
        f1 = Fraction(fz1,fm1)
        f2 = Fraction(fz2,fm2)
        f3 = Fraction(fz3,fm3)

        if( sign1 == '*' or sign1 =='/'):
            answer = cal( cal(f1,sign1,f2) , sign2 , f3 )
        else:
            answer = cal( f1 , sign1 , cal(f2,sign2,f3) )

        question = '(', fz1, '/', fm1, ')', sign1, '(', fz2, '/', fm2, ')', sign2, '(', fz3, '/', fm3, ')'
        question = "".join('%s' % id for id in question)
        question.replace("/", "÷").replace("*", "×")
        print(question, end=' = ')

    else:  # 一运算符算式
        sign1 = st[random.randint(0, 3)]  # 随机得符号
        fm1 = random.randint(1, fmRange)  # 随机分数   分母fm  分子fz
        fz1 = random.randint(1, fmRange * Range)
        fm2 = random.randint(1, fmRange)
        fz2 = random.randint(1, fmRange * Range)

        f1 = Fraction(fz1,fm1)           #得两分数
        f2 = Fraction(fz2,fm2)

        answer = cal(f1,sign1,f2)            #得结果
        question = '(',fz1,'/',fm1, ')', sign1, '(',fz2, '/',fm2, ')'
        question = "".join('%s' % id for id in question)
        print(question.replace("/", "÷").replace("*", "×"), end=' = ')


    # 假分数 变 带分数
    if(answer%1):                  #判断计算结果是否是整数
        if( answer > 1 ):
            n = str(answer).index('/')     #找出 除号的位置来当分界符  得到分子和分母
            t = 0
            fz = 0
            fm = 0
            l = len(str(answer))
            while(t<n):          # 分子
                fz = int(str(answer)[t]) + fz * 10
                t = t + 1

            t = t +1           #跳过 '/'

            while(t<l):       # 得分母
                fm = int(str(answer)[t]) + fm * 10
                t = t +1

            num = 0
            if( fz > fm ):
                num = fz // fm
                fz = fz % fm
            print(str(num)+ '`' + str(fz)+'/'+str(fm))
            answer = str(num)+ '`' + str(fz)+'/'+str(fm)
            write_in(i, question, str(answer))


        elif( answer < -1 ):
            n = str(answer).index('/')  # 找出 除号的位置来当分界符  得到分子和分母
            t = 1           # 0是负号
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

            print('-'+ str(num) + '`' + str(fz)+'/'+str(fm))
            answer = '-'+ str(num) + '`' + str(fz)+'/'+str(fm)
            write_in(i, question, str(answer))

        else:
            answer = str(answer)
            print(answer)
            write_in(i, question, answer)
    else:
        answer = str(answer)
        print(answer)
        write_in(i, question, answer)
