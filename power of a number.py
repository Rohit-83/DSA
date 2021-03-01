#wap to find the power of a number a power b or 2 power 3 = 8
import time
def power(a,b):
    #a = number
    #b = power raised
    result = 1
    start = time.time()
    for i in range(1,b+1):
        result = result*a
    print(time.time()-start)
    return result
print(power(10,20))


#the above works on linear search i.e its time complexity O(b)
#we can improve the program by using binary search by dividing the num

def fast_power(a,b):
    start1 = time.time()
    result = 1
    while b>0:
        if b%2 != 0:
            result = result*a #base case
        a = a*a
        b = b//2
    print(time.time()-start1)
    return result
print(fast_power(10,20))

