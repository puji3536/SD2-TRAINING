def insertionsort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[i]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
a=list(map(int,input().split()))
insertionsort(a)
print(a)