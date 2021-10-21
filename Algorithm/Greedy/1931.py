# 백준 1931번 - 회의실 배정
n = int(input())

timeList = []

for _ in range(n):
    start, end = map(int, input().split())
    timeList.append((start, end))

timeList.sort(key=lambda time: (time[1], time[0]))

count = 0
end = 0

for next in timeList:
    if end <= next[0] :
        end = next[1]
        count += 1

print(count)



