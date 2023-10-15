def bs(l,target):
    #floor=-1
    #ceil=float('inf')
    def bsf(si,ei):
        if si<=ei:
            mid=(si+ei)//2
            if l[mid]==target:
                return l[mid]
            if l[mid]<target:
                #floor=l[mid]
                return bsf(mid+1,ei)
            return bsf(si,mid-1)
            #ceil=l[mid]
        
        if target<l[0]:
            return -1
        #return floor
        #return ceil
        return l[si-1]
    return bsf(0,len(l)-1)


l=list(map(int,input().split()))
target=int(input())
print(bs(l,target))