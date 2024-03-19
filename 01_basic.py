# # 처음실행 : ctrl + shift + f10
# # 수정해서 실행 : shift + f10
# print("hello")
# print('python')
# print('\n')
# # 연습 hello 화면에 세번 출력
# print('hello\n'*3)
#
# # 프로그램 : 코드(함수), 데이터(변수)
# # a=3
# # print(a)
#
# # 데이터 : 변수, 상수
# # 데이터 : 숫자(정수,실수), 문자
# a=3
# b='hello'
# print(a)
# print(b)
# print('korea')
# print('\n')
#
# # int   float   str bool
#
# a=20
# b=56.7
# c='hello'
# d=True
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# print(1.1+0.1==1.2)

# a=3
# b=4
# print('a:',a)
# print('b:',b)
# t = a
# a = b
# b = t
# print('a:',a)
# print('b:',b)

a=3
b=4
a,b = b,a
print('a:',a)
print('b:',b)