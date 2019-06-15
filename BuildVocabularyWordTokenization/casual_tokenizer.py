from nltk.tokenize.casual import casual_tokenize
from nltk.util import ngrams
import re

message = "RT @TJMonticello Best day everrrrrrr at Monticello.... Awesommmmmmeeeeeeee day :*) "

cas_tok = casual_tokenize(message)

print(cas_tok)

cas_tok2 = casual_tokenize(message, reduce_len=True, strip_handles=True)
print(cas_tok2)

print('------------------')

sentence = "Albiona Hoti filloi punen si software engineer ne moshen 22 vjecare."

pattern = re.compile(r"([-\s.,;!?])+")

tokens = pattern.split(sentence)
tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']
print(tokens)

print('---------------')

two_grams = list(ngrams(tokens, 2))

print(two_grams)

print('---------------')

print([" ".join(x) for x in two_grams])
'''
    Python generators are "smart" functions that behave like iterators,
    yielding only one element at a time instead of returning the entire
    sequence at once.
    This is useful within for loops, where the generator will load each
    individual item insted of loading the whole item list into memory.

'''