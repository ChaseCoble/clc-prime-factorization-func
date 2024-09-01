import numpy


def prime_factorize(target):
    n = target + 1

    def primesfrom2to(n):
        sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
        for i in range(1, int(n**0.5) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
        return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1)   |1)]

    prime_list = primesfrom2to(n).tolist()
    counter = len(prime_list)
    factor_list = [1]
    if target in prime_list:
        factor_list.append(target)
        counter = 0
    while counter != 0:
        if target in prime_list:
            factor_list.append(target)
            prime_list.remove(target)
        elif target % prime_list[0] == 0:
            factor_list.append(prime_list[0])
            target = target // prime_list[0]
            prime_list.pop(0)
        else:
            prime_list.pop(0)
            for x in reversed(prime_list):
                if x >= target or target % x != 0:
                    prime_list.remove(x)
        counter = len(prime_list)
    return print(f'The prime factors are {factor_list}')

def intCheck(inputVar):
    if inputVar.isdigit():
        if int(inputVar) <= 0:
            inputVar = print("That was not a positive integer above zero!\n")
            return False
        return True
    print("That was not even a number!")    
    return False
                       

def continuePrompt():
    while True:
        response = input("Would you like to try it again? Type 'y' for yes and 'n' for no: ")
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("That was not a valid answer.")


willContinue = True

while willContinue:
    isInt = False
    print("This is a function that will find all prime factorizations of any target integer above zero you wish to submit! \n")
    while not isInt:
        targetInt = input("What number do you want to find the prime factors for?  ")
        isInt = intCheck(targetInt)
    targetInt = int(targetInt)
    prime_factorize(targetInt)
    willContinue = continuePrompt()
  
print("Thank you for trying my code!")
