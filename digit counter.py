#wap to  find number of digits in a given number.
#1.we can find it by using counter by dividing the number by 10
def count_digit(num):
    counter = 0
    while num>0:
        counter+=1
        num = num//10
    return counter

print(count_digit(123))
print(count_digit(123450))

#this method takes time complexity O(digit) , but instead of this if we
#mathematical function then it will take less time

def count_digit_mathematically(num):
    import math
    k = math.floor(math.log10(num)+1)
    return k

print(count_digit_mathematically(123))
print(count_digit_mathematically(123450))
