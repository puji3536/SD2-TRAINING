def sort(l,n):
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if l[j]<l[mini]:
                mini=j
        (l[i],l[mini])=(l[mini],l[i]) 
l=list(map(int,input().split()))
n=len(l)
sort(l,n)
print(l)