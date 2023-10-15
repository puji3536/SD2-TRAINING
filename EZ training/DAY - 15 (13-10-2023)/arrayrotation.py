#METHOD-1
'''l=list(map(int,input().split()))
r=int(input())
for i in range(r):
    l.insert(0,l.pop())
print(*l)'''

#METHOD-2 USING TEMPORARY VARIABLE
'''l=list(map(int,input().split()))
r=int(input())
n=len(l)
for i in range(r):
    temp=l[-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=temp
print(*l)'''

#METHOD-3 USING SLICING
l=list(map(int,input().split()))
r=int(input())
a=len(l)-r
if r>=len(l):
    r=r%len(l)
    if len(l)==0 or r==0:
        print("None")
l[:]=l[a:]+l[:a]
print(*l)