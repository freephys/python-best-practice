#!/usr/bin/env python

from itertools import count

def prime_gen():
    yield 2
    n = 3
    yield n
    prime_list = [(2,4),(3,9)]
    it = count(4)
    for n in it:
        n = it.next()
        for p,p2 in prime_list:
            if n % p == 0 :
                break
            elif p2 > n :
                prime_list.append((n,n*n))
                yield n
                break
        else:
            raise RuntimeError("should not run out of prime")
if __name__ == '__main__':
    prime_list = prime_gen()
    n = 0
    while n<100000 :
        print prime_list.next()
        n +=1            
                
    
    
   
        
    