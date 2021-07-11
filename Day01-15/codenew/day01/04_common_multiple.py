

def common_multiple(a, b):
    v = max(a,b)
    while(True) :
        if v % a == 0 and v % b == 0 :
            return v
        else :
            v += 1
    return a * b

def common_divisor(a, b) :
    v = min(a, b)
    for i in range(v, 2, -1):
        if a % v == 0 and b % v == 0:
            return i
    return 1

if __name__ == "__main__" :
    a = int(input("a-->"))
    b = int(input("b-->"))
    m = common_multiple(a, b)
    v = common_divisor(a, b)
    print("m = {0}, v = {1}".format(m, v))
