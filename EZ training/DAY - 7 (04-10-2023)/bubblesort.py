def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
data=list(map(int, input().split()))
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)