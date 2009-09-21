#!/usr/bin/env python

from itertools import count

def prime_gen():
    prime_list = [2]
    for p in prime_list: yield p
    for n in count(prime_list[-1] + 1):
        for p in prime_list:
            if p * p > n:
                prime_list.append(n)
                yield n
                break
            elif n % p == 0:
                break
        else:
            raise Exception("Shouldn't have run out of primes!")
if __name__ == '__main__':
    prime_list = prime_gen()
    n = 0
    while n<100000 :
        print prime_list.next()
        n +=1            