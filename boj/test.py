import sys

n = int(sys.stdin.readline())
result = []
cnt = 0

def nQueen(col, row):
    result.append([col, row])
    if len(result) == n:
        cnt += 1
    else:
        for i in range(col, n + 1):
            for j in range(1, n + 1):
                for p in result:
                    if i == p[0]:
                        continue
                    elif j == p[1]:
                        continue
                    
                
1,1
1,1 1,2 1,3 1,4
2,1 2,2 2,3 2,4
3,1 3,2 3,3 3,4
4,1 4,2 4,3 4,4
 
nqueen(col,row, cnt)
col~n,