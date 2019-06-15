import numpy as np
import pandas as pd

sentence1 = """Albiona Hoti filloi punen si software engineer ne moshen 22.""" 

token_sequence = str.split(sentence1) 
# 1 str.split() is a quick-and-dirty tokenizer

vocab = sorted(set(token_sequence))
# 2 Your vacabulary lists all the unique tokens (words) that you want to
# keep track of

', '.join(vocab)
# 3 Sorted lexographically (lexically) so numbers come BEFORE LETTERS, 
# and CAPITAL LETTERS COME before lowercase letters

num_tokens = len(token_sequence)

vocab_size = len(vocab)

onehot_vectors = np.zeros((num_tokens, vocab_size), int)
# 4 The empty table is as WIDE as your count of unique vocabulary terms and as 
# HIGH as the length of your document, 10 rows by 10 columns.

for i, word in enumerate(token_sequence):
  onehot_vectors[i, vocab.index(word)] = 1
# 5 For each word in the sentence, mark the column for that word in your vocabulary
# with a 1.

' '.join(vocab)
print(onehot_vectors)


'''
 Pandas datagrames can help make this a little easier on the eyes and more informative.

 Pandas wraps a 1D array with some helper functionality in an object called a SERIES.
 And Pandas is particularly handy with tables of numbers like lists of lists, 2D numpy
 arrays, 2D numpy matrices, arrays of arrays, dictionaries of dictionaries, etc.

'''

dataframePandas = pd.DataFrame(onehot_vectors, columns=vocab)

print(dataframePandas)

'''
    One-hot vectors are super-sparse, containing only one nonzero value in each row
    vector.
    - We can make that table of one-hot vectors even prettier by replacing zeros
    with blanks.
    - Don't do this with any DataFrame you intend to use in your machine learning
      pipeline, because it will crete a lot of non-numerical objects within
      your numpy array
'''

dataframePandas[dataframePandas == 0] = ''

print (dataframePandas)

print('----------------')


print('The sentence look as a binary bag-of-words vector')

sentence_bow={}
for token in sentence1.split():
  sentence_bow[token] = 1

sortedSent = sorted(sentence_bow.items())
print(sortedSent)