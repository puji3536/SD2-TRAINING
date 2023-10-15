def linearSearch(array,target):
    for i in range(0,len(array)):
        if (array[i] == target):
            return i
    return -1
array = list(map(int,input().split()))
target = int(input())
result = linearSearch(array,target)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ",result)