# [백준] 11047번 - 동전0
n, k = map(int, input().split())
ans = 0
coinList = []
for _ in range(n) :
    coinList.append(int(input()))
coinList.reverse()
for coin in coinList :
    ans += k//coin
    k %= coin

print(ans)