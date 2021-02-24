#wap to find lcm and hcf
def lcm(num1,num2):
    if num1>num2:
        greater = num1
    else:
        greater = num2

    while True:
        if (greater%num1 == 0) and (greater%num2 == 0):
            lcm = greater
            break
        greater+=1
    return lcm

#print(lcm(54,24))

#the above method takes very large time so we go through hcf

def hcf(num1,num2):
    if num1 == 0:
        return num2
    return hcf(num2%num1,num1)

print(hcf(30,42))


def lcm1(num1,num2):
    hcf1 = hcf(num1,num2)
    lcm1=(num1*num2)//hcf1
    return lcm1
print(lcm1(54,24))
