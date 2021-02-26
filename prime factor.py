#wap to find prime factor of a number

def primefactor(num):
    import math

    while num%2 == 0:
        print(2,end=" ")
        num = num//2
    #at this point number will becamee odd
    for i in range(3,int(math.sqrt(num))+1,2):
        #we use 2 increment bcz of odd number principle
        while num%i == 0:
            print(i,end=" ")
            num = num//i

    if num>2:
        #only prime number will be remaining
        print(num,end=" ")

print(primefactor(1000))
#this is a basic function of prime factor
