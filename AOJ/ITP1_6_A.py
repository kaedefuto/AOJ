"""
n = int(input())
a = list(map(int,input().split()))
#a.reverse()
for i in a[::-1]:
    print(i,end=" ")
"""

n = int(input())
a = list(map(int, input().split()))
print(*reversed(a))