
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

k = []

r = len(m)

c = len(m[0])

k = [[0 for _ in range(r)] for _ in range(c)]

for i in range(0 , r ):
    for j in range(0 , c):
      a = (r-1)-i
      k[j][a] = m[i][j] 
    
for i in range(0 , r ):
    for j in range(0 , c):
      print(k[i][j], end=" ") 
    print( )
print(k)