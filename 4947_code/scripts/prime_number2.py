#!/usr/bin/env python

from itertools import count;
#from math import sqrt;
def prime():
    """
    generator of prime
    """
    prime = []
    for n in count(2):
        if all(n%p for p in prime if p*p <= n):
            prime.append(n)
            yield n
if __name__ == '__main__':
    prime_list = prime()
    n = 0
    while n<1000 :
        print prime_list.next()
        n +=1