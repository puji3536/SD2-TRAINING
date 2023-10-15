def pal(s):
    n=len(s)
    left=0
    right=n
    def pal_rev(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left+=1
            right-=1
    return s[left+1:right-1]
    res=[]
    for i in range(len(s)):
        pal1=pal_rev(i,i)
        if len(pal1)>1:
            res.append(pal1)
        pal2=pal_rev(i,i+1)
        if len(pal2)>1:
           res.append(pal2)
    return res
s=input()
r=pal(s)
print(r)