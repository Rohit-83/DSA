#wap to count number of digits in factorial of a number
def digit_counter(num):
    count = 0
    count = float(count)
    import math
    if num == 1:
        return 1
    while num>1:
        #we use mathematical formula for counting the number of digits 
        count += math.log10(num)
        num = num-1
    return int(math.ceil(count))

print(digit_counter(5000))

#when we have to find the number of digits in a number not factorial then we use
#formulla count = int(math.log10(num))+1
