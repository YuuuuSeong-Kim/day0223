# 반복문 : while, for
# "hello"를 화면에 3번 출력
# n = 1
# while n <= 3:
#     n += 1
#     print('hello')

# 연습) 사용자한테 n을 입력받아 1~n까지의 합을 누적하여 출력

# n=int(input('숫자 입력 : '))
# i=1
# b=1
# while(i<n):
#     i+=1
#     b += i
# print(b)

# i =1
# while i <= 10:
#     print(i,end=" ")
#     i+=1

# 연습) 사용자 한테 n을 입력받아 n!을 구하여 출력

# n=int(input('숫자 입력 : '))
# i=1
# pac=1
# while i<=n:
#     pac*=i
#     i+=1
# print(str(n)+'! 값은 : '+str(pac))

'''
    for 변수명 in range(시작,종료,증감):
        명령어
    ==> 종료-1 까지 동작

    for 변수명 in range(시작,종료):    증감 기본값 1
        명령어
    ==> 종료-1 까지 동작

    for 변수명 in range(종료):           시작 기본값 0
        명령어
    ==> 종료 까지 동작
'''

# 1에서 10까지의 모든 수를 출력
# for i in range(1,11,1):
#     print(i,end=" ")

# for i in range(1,11):
#     print(i,end=" ")

# for i in range(10):
#     i+=1
#     print(i,end=" ")

# 연습) 구구단 2단 출력
# dan = 2
# for i in range(9):
#     i+=1
#     print(f"{dan} * {i} = {dan * i}")

# 연습) 2단부터 9단까지
# for dan in range(2,10):
#     for i in range(9):
#         i+=1
#         print(f"{dan} * {i} = {dan * i}")
#     print()