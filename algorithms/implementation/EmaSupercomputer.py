#https://www.hackerrank.com/challenges/two-pluses
import sys
from itertools import permutations

from janitor.plugincore import plugin

N, M = map(int, input().split())

def checkValidPlus(i, j, lb, grid):
    if i - lb < 0 or i + lb >= N or j -lb < 0 or j +lb >= M:
        return False
    #check colums, y is fixed
    for x in range(i-lb,i+lb+1):
        if grid[x][j] == 'B':
            return False
    #check rows, x is fixed
    for y in range(j-lb,j+lb+1):
        if grid[i][y] == 'B':
            return False
    return True

def plusesCompatible(i1,j1,lb1, i2,j2,lb2):
    areaBy1 = [(a,b) for a in range(i1-lb1, i1+lb1+1) for b in range(j1-lb1, j1+lb1+1) if a == i1 or b ==j1]
    assert len(areaBy1) == 1 + lb1*4
    areaBy2 = [(a,b) for a in range(i2-lb2, i2+lb2+1) for b in range(j2-lb2, j2+lb2+1) if a == i2 or b == j2]
    assert len(areaBy2) == 1 + lb2*4
    intersection = set(areaBy1) & set(areaBy2)
    if len(intersection) ==0:
        return True
    return False


max_branch_size = min(N,M)//2
grid = []
for line in sys.stdin:
    row = []
    for l in line.rstrip():
        row += l
    grid.append(row)
    if len(grid) == N:
        break

#Construct all valid Pluses
validPlus = []
for (i,j,lb) in [(i,j,lb) for i in range(N) for j in range(M) for lb in range(max_branch_size+1) if not grid[i][j] == 'B' ]:
    if checkValidPlus(i,j,lb,grid):
        validPlus.append((i,j,lb))

#Only keep pluses that don't overlap
# compatible_plus = []
max_area = 0
for (p1,p2) in permutations(validPlus,2):
    (i1,j1,lb1),(i2,j2,lb2) = (p1,p2)
    if plusesCompatible(i1,j1,lb1, i2,j2,lb2):
        # compatible_plus.append((p1,p2))
        max_area = max(max_area, (1+4*lb1) * (1 +4*lb2))


print(max_area)
