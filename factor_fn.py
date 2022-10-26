from audioop import reverse
from timeit import repeat
import numpy
#Original code
target = 15
n = target + 1
#Original code ends
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n Code taken from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n"""
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
#Original code from here down
prime_list = primesfrom2to(n).tolist()
counter = len(prime_list)
factor_list = [1]

while counter != 0:
    if target in prime_list:
        factor_list.append(target)
        counter = 0
        
    elif target % prime_list[0] == 0:
        factor_list.append(prime_list[0])
        target = target // prime_list[0]
        prime_list.pop(0)
        for x in reversed(prime_list):
            if x > target:
                prime_list.remove(x)
                counter = len(prime_list)
                if counter == 0:
                    print(f'The prime factors are {factor_list}')
                else:
                    break
                    
            else:
                break
        counter = len(prime_list)
    elif target % prime_list[0] != 0:
        prime_list.pop(0)
        counter = len(prime_list)
        repeat
    else:
        print(f'The prime factors are {factor_list}')
        break
print(f'The prime factors are {factor_list}')