import itertools
import pprint
def par_longest_first(padding_item, *sequences):
    """
    if you know in advance which iterable is the longest one,
    you can wrap every other iterable x as itertools.chain(iter(x), itertools.repeat(padding))
    and then call itertools.izip
    """
    iterators = map(iter, sequences)
    for i, it in enumerate(iterators):
        if not i: continue
        iterators[i] = itertools.chain(it, itertools.repeat(padding_item))
    return itertools.izip(iterators)
            
if __name__ == '__main__':
    pprint.pprint(map(list,par_longest_first('x', 'zapper', 'ui','foo')))
    
