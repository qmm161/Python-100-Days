from math import sqrt

def check_prime(num) :
    end = int(sqrt(num))
    for i in range(2, end + 2) :
        if num % i == 0 :
            return False
    return True

if __name__ == "__main__" :
    while(True) :   
        num = int(input("-->"))
        if(check_prime(num)) :
            print("{0} is prime".format(num))
        else:
            print("{0} is not prime".format(num))