from itertools import permutations

print([" ".join(combo) for combo in \
       permutations("Mire mengjes Rosa!".split(), 2)])

print('---------')
print('Ne shqip')

s = """Gjej literature qe permbajne titul sikur 'NLP', ose 'natyral' \
            dhe 'gjuhe', ose 'kompjuterike' dhe 'gjuhesi'."""

print(len(set(s.split())))


print('Ne anglisht')
s2 = """Find textbooks with titles containing 'NLP', or
              'natural' and 'language', or 'computational' and 
              'linguistics'."""

print(len(set(s2.split())))


print('-----------')
import numpy as np
print(np.arange(1,12 + 1).prod()) # factorial(12) - arrange(1,13).prod()

'''
       np.arange(10)
       array([0,1,2,3,4,5,6,7,8,9])

       np.arange(2,10)
       start count from the value 2 included - up to 10 excluded

       np.arange(2,10,2) -> third step size parameter
       which prints only every second element
       array([2,4,6,8])

       np.arange(2,10,3)
       array([2,5,8])

       the forth parameter - data type
       np.arange(2,10,3, dtype=np.float32)
       array([2.,5.,8.], dtype=float32) -> 32 bits
'''


