# 함수 : 어떤 문제해결을 위한 서로 관련있는 명령어 들의 집합
'''
def 함수이름():
    명령어들
    return (값1,값2,..)
'''
# 반환값 여러개면 튜플로 반환

#  두개의 수를 매개변수로 전달받아 더하기 하여 결과를 돌려주는 함수
# def add(a,b):
#     r = a + b
#     return r
#
# r = add(6,7)
# print(r)

# 더하기, 빼기, 곱하기, 나누기 결과 반환 함수
def calc(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a//b
    return add,sub,multi,div


print(calc(int(input('첫번째 수 : ')),int(input('두번째 수 : '))))