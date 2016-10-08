#!/usr/bin/env python2
#A function to generate prime numbers from 0 to n with asymptotic analysis

class PrimeNumbers(object):

  
  def prime(self, n):

    """
      generate prime numbers from 0 to n 
      returns: array with primes numbers, [] if no primes are found
      raise: Typerror when is not int)  
             ValueError when n < 1
      # WorstCase =  (n*2)
    """
    
    if not type(n) == int:
      raise TypeError("only integers expected input to function, current type "+str(type(n)) )
    
    if n < 1:
      raise ValueError("Expected positive integers 1 or more, current parameter \""+str(n)+"\"")
    
    if n == 1:
      return []
    
    if n == 2 or n == 3:
      return [n]
    
    prime_numbers = [2, 3]
    
    for i in xrange(4, n+1):
      is_prime = True
      for p in prime_numbers:
        if i % p == 0:    #is prime add to array
          is_prime = False
          break;
        
      if is_prime:
        prime_numbers.append(i)
    return prime_numbers

if __name__ == '__main__':
    n = 21
    print PrimeNumbers().prime(n)

