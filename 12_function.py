# 연습) 두개의 수를 매개변수로 전달받아 그 중에 큰 수를 찾아 반환하는 함수
def 켘(a,b):
    return max(a,b)

# print(켘(int(input('첫번째 수 입력 : ')),int(input('두번째 수 입력 : '))))

# 연습) 세개 중 큰 수 찾기
print( max( int( input('첫번째 수 입력 : ') ) ,
            int( input('두번째 수 입력 : ') ),
            int(input('세번째 수 입력 : ')) ) )