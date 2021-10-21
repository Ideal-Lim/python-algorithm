# 수 자료형

# 1. 정수형
a = 100  # 양의 정수
a = -100  # 음의 정수
a = 0  # 0

# 정수 계산
a, b = 5, 3

print(a / b) # 나눈 결과 1.6666666666666667
print(a // b) # 몫 1
print(a % b) # 나머지 2
print(a ** b) # 거듭제곱 125

# 큰 정수
a = 100000000000000000000
print(type(a)) # <class 'int'>

# 2. 실수형
a = 165.32 # 양의 실수
a = -145.23 # 음의 실수
a = 5. # 5.0 소수부가 0일 때 0 생략 가능
a = -.6 # -0.6 정수부가 0일 때 0 생략 가능
a = 1.6e-3 # 0.0016 유효숫자 * e^지수 (e= 10) 로 표현
a = 1.6e2 # 1.6 * 10^2 = 160.0
a = 123.52e1 # 1235.2

# 실수 계산
a = 0.3 + 0.6
print(a) # 0.8999999999999999
print(a == 0.9) # False

#round(n, 원하는 소수점 자리)
a = round(123.456, 1)
print(a) # 123.5

