#wap to find how many zero at the end of the factorial
def countzero(num):
    count=0
    i = 5
    while i <= num:
        count = count+num//i
        i=i*5
    return count
print(countzero(30))
