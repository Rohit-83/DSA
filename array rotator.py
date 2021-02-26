#wap to rotate the array by d times

def rotate(arr,d):
    for i in range(d):
        temp =  arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]  = temp
    return arr
arr = [1,2,3,4]
d =2
print(rotate(arr,d))
