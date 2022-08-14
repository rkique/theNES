num = 921830

def basechange(num,base):
        if num >= 1:
            basechange(num // base, base) #disregard remainder
            print(num % base, end="") #print remainder

basechange(1230129124,9)

c = []
def binary(num):
    if num >= 1:
        c.append(num % 2)
        binary(num // 2)
    return c

print(binary(3024))