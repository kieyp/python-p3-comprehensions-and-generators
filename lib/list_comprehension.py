#!/usr/bin/env python3

def return_evens(num_list):
    pass
    even_list=[ x for x in num_list if x % 2 == 0]
    
    if not even_list:
        return []
    else:
        return even_list
print(return_evens(num_list=[7]))



def make_exclamation(sentence_list):
    pass
    data= [n + "!" for n in sentence_list]
    return data
print (make_exclamation(sentence_list=["a","b","c"]))
