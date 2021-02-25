#wap to find all prime number till the given number

#we can solve this by a method known as sieve of eratosthenes

def total_prime(num):
    #we create an empty array and mark all the element in array to 0
    #if the number is a multiple of some number then we mark that by 1
    arr =[]
    for i in range(num+1):
        arr.append(0)
    for i in range(2,num+1):
        if arr[i] == 0:
            for j in range(i*i,num+1,i):
                arr[j] = 1
    for i in range(2,num+1):
        if arr[i] == 0:
            print(i,end=" ")
    
print(total_prime(100))
#this operation takes O(NlogN) time which is faster from basic method.
