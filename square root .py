#wap to find square root of a number in int form

def squareroot(num):
    for i in range(1,num):
        if i*i == num:
            return i
        elif i*i > num:
            return i-1
#the upper function  is  the basic function of finding the square root
#by traversing the whole list which have O(N) time complexity

#so for improving we have to use binary search instead of linear search

def sqrt1(num):
    mid = num//2
    while mid*mid>=num:
        if mid*mid == num:
            return mid
        mid = mid//2
    while True:
        if mid*mid == num:
            return mid
        elif mid*mid>num:
            return mid-1
        mid=mid+1

print(squareroot(626))
print(sqrt1(629))
        
