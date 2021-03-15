'''Quick sort use divide and conquer here we choose pivot the last
element of array''' 


def quick_sort(arr,low,high):
    if len(arr) == 1:
        return arr
    if (low<high):
        partition_point = partition(arr,low,high)
        quick_sort(arr,low,partition_point-1)
        quick_sort(arr,partition_point+1,high)
    return arr
    

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

arr = [6,5,4,3,2,1]
low = 0
high = len(arr)-1
print(quick_sort(arr,low,high))

            
        
        
    
