from timeit import repeat
import numpy


def prime_factorize(target):
  n = target + 1

  def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n Code taken from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n"""
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n**0.5) // 3 + 1):
      if sieve[i]:
        k = 3 * i + 1 | 1
        sieve[k * k // 3::2 * k] = False
        sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

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
            return factor_list
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
      return factor_list

  return print(f'The prime factors are {factor_list}')

def intCheck(inputVar):
  isInt = False
  while not isInt:
    if inputVar.isdigit():
      return int(inputVar)
    else:
      inputVar = input("That was not a positive integer! Please enter the positive integer you intended: ")
                       

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
  print("This is a function that will find all prime factorizations of any target integer you wish to submit!")
  targetInt = input("What number do you want to find the prime factors for?  ")
  checkedInt = intCheck(targetInt)
  prime_factorize(checkedInt)
  willContinue = continuePrompt()
  
print("Thank you for trying my code!")
