import numpy as np

import pandas as pd
sentence = """Thomas Jefferson began building Monticello at the age of 26."""
sentence1 = """Albiona Hoti filloi punen si software engineer ne moshen 22."""

token_sequence = str.split(sentence1) # token sequence is the sentence splitet in an array -

vocab = sorted(set(token_sequence)) # we are sorting the splited sentence - or token sequence

print('sorted the token sequence\n', vocab)

print('\nWe are joining the sorted array - or sequence of vocab with ", " ..\n')
print(', '.join(vocab)) # join the vocab with 

print('----------')

num_tokens = len(token_sequence)
print('The length number of splited sentence. \n ',num_tokens)

print('----------')

vocab_size = len(vocab)
print('The length number of sorted splited sentence.\n',vocab_size)

print('----------')

onehot_vectors = np.zeros((num_tokens, vocab_size), int)

for i, word in enumerate(token_sequence):
  onehot_vectors[i, vocab.index(word)] = 1

print(' '.join(vocab))

print('----------')

print('One hot vectors or one word vectors: \n', onehot_vectors)


# print(pd.DataFrame(onehot_vectors, columns=vocab))

df = pd.DataFrame(onehot_vectors, columns=vocab)
df[df==0] = ''

print(df)