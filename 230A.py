m, n = [int(x) for x in input().split()]
l = []
for i in range(n):
	l.append([int(x) for x in input().split()])
c=0
l.sort()
#print(l)
if m>=l[0][0]:
    m = m + l[0][1]
for i in range(n-1):
    if m >= l[i+1][0]:
        m=m+ l[i+1][1]
        c =1

#print(c)        
        
if c==1:
    print("YES")
else:
    print("NO")
