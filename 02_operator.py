# 연산자 : 산술, 비교, 논리
# 산술    :   +   -   *   /(실수나누기)    //(정수나누기)   **(지수승)     %(나머지)
# 비교    :   >   >=  <   <=  ==  !=
# 논리    :   and or  not

# a,b = 5,2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)
# print('-'*50)
# a+=1
# print(a)

# a,b = 5,2
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)

# a='10'
# b='20'
# print(a+b)
# print(int(a)+int(b))

# a = 10
# b = -5
# c = 0
# d='hello'
# e=32.7
# f=0.0
# print(a,bool(a))
# print(b,bool(b))
# print(c,bool(c))
# print(d,bool(d))
# print(e,bool(e))
# print(f,bool(f))

# print(int(True))
# print(int(False))

# name=input('이름을 입력하시오=>')
# print(name)

# 연습) 사용자한테 어떤 숫자 하나를 입력받아 +1 하여 출력한다
# a=input('숫자를 입력하시오 : ')
# print(int(a)+1)

# 연습) 사용자한테 나이를 입력받아 20살 이상인지 판별하여 True, False를 출력 한다
# age=int(input('나이를 입력하시오 : '))
# print(age>=20)

# 연습) 두 사람의 나이를 입력받아 모두 20살 이살이면 True, 아니면 False 출력
# a,b=int(input('a의 나이를 입력하시오 : ')),int(input('b의 나이를 입력하시오 : '))
# print(a>=20 and b>=20)

# a,b=input('두 사람의 나이를 입력하시오. 공백으로 구분 : ').split()
# print(int(a)>=20 and int(b)>=20)

'''
if문의 형식

if 조건식:
    명령어1
    명령어2
    명령어3
    ..
else:
    명령어4
    명령어5
'''

# 연습) 어떤 수를 입력받아서 짝수,홀수 판별
# a=int(input('숫자 하나를 입력하시오 : '))
# if(a%2==0):
#     print('짝수')
# else:
#     print('홀수')

# 연습) 사용자한테 세개의 수를 입력받아 그 중에 가장 큰 수를 찾아 출력
# a,b,c = input('세개의 수 입력. 공백으로 구분 : ').split()
# print(max(int(a),int(b),int(c)))

'''
    물어봐야 할 것이 많다면 elif를 사용할 수 있다
    if 조건1:
        명령1
    elif 조건2:
        명령2
    elif 조건3:
        ...
    else:
        ..
'''

# 연습) 0~9사이의 정수를 입력받아 한글표기식 출력
# h=['영','일','이','삼','사','오','육','칠','팔','구']
# n=int(input('0~9 사이 숫자 하나를 입력하시오 : '))
# print(h[n])

# 연습) 0~99사이의 수를 입력받아 한글표기식 출력
h=['영','일','이','삼','사','오','육','칠','팔','구']
a = int(input('숫자 입력 0-99 : '))
if(a>=20):
    if(a%10!=0):
        print(h[a//10]+'십'+h[a%10])
    else:
        print(h[a//10]+'십')
elif(a>10 and a<20):
    print('십'+h[a%10])
elif(a==10):
    print('십')
else:
    print(h[a])