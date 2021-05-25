"""
tbl = [[0 for i in range(7)] for j in range(5)]
for i, row in enumerate(tbl):
    for j, elem in enumerate(row):
        if j > 0: 
            print(" ", end = "")
        print(elem, end = "")
    print()
"""

cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]
n = int(input())

for i in range(n):
    ch,rank=input().split()
    rank=int(rank)
    cards[pattern.index(ch)][rank-1] = True

for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j+1)