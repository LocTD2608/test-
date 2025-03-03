a1,a2,a3,b1,b2,b3 = map(int,input().split())
n = int(input())
a = a1 + a2 + a3
b = b1 + b2 + b3
c = 0
if a % 5 == 0 :c += (a//5)
else:c += (a//5 +1)
if b % 10 == 0:c += (b//10)
else:c += (b//10+1)
if c <= n:print('YES')
else:print('NO')