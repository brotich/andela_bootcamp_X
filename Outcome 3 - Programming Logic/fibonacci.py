#!/usr/bin/env python2
"""
A program to generate and display the first n numbers fibonacci sequence
worst case = (n)
"""

class Fibonacci(object):

  def fib_num(self, n):
    """
      generates the list of fibonnaci sequence using recursion
    """
    if type(n) != int:
      raise TypeError("Expected integer as parameter value for n")
    if n < 0:
      raise ValueError("Positive integers of equal or more than 0 are accepeted by the function")
      
    if n == 0 or n == 1:
      return n
    return self.fib_num(n-2) + self.fib_num(n-1)

  def fib(self, count):
    """
      get the n numbers of the fibonacci sequence
    """
    if type(count) != int:
      raise TypeError("Expected integer as parameter value for count")
    if count < 1:
      raise ValueError("Expected integer at least of the 1 fibonacci sequence number")

    fib_seq = []
    for i in xrange(count):
      fib_seq.append(self.fib_num(i) )
    return fib_seq



if __name__ == '__main__':
    count = 5
    print Fibonacci().fib(count)