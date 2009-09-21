#!/usr/bin/env python
from itertools import count

#g = (lambda prime = []:
#    (n for n in count(2) \
#        if (lambda n , prime : (n in prime if prime and n<prime[-1]\
#        else
#            (prime.append(n) or True \
#                if all(n%p for p in prime if p*p < n ))\
#            else False)))(n,prime)))()


g = (lambda primes = []:
    (n for n in count(2) \
     if (lambda n, primes: (n in primes if primes and n<=primes [-1] \
                            else (primes.append(n) or True \
                                  if all(n%p for p in primes if p*p <= n) \
    else False)))(n, primes)))()
    
n = 0
while n<1000 :
    print g.next()
    n +=1
        