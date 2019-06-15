'''
    S○ Let's use an even more efficient form of a dictionary, a Pandas Series. 
    And you'll wrap that up in a Pandas DataFrame so you can add more sentences 
    to your binary vector "corpus" of texts about Albiona Hoti.
     All this hand waving about gaps in the vectors and sparse versus 
     dense bags of words should become clear as you add more sentences 
     and their corresponding bag-of-words vectors you your DataFrame - table
      of vectors corresponding to texts in a corpus
'''

import pandas as pd

sentence1 = """Albiona Hoti filloi punen si software engineer ne moshen 22."""

df = pd.DataFrame(pd.Series(dict([(token, 1) for token in sentence1.split()])), columns=['sent']).T

# print(df)

'''
    Let's add a few more texts to your corpus to see how a DataFrame stacks up.
    A DataFrame indexes both the columns (documents) and rows (words) so itcan be
    an "inverse index" for document retrieval, in case you want to find a Trivial 
    Pursuit answer in a hurry
'''

sentences = """Albiona Hoti filloi te krijoj web aplikacione \
    ne moshen 22 vjecare.\n Dizajni i aplikacioneve eshte bere nga studente te \
    tjere. \n Albiona u zhvendos ne Prishtine ne vitin 2017. \n Duke punuar ne \
    web aplikacione, tashme ajo ishte fokusuar shume ne ato teknologji.
""" # 1

corpus = {}

for i, sent in enumerate(sentences.split('\n')):
  corpus['sent{}'.format(i)] = dict((tok, 1) for tok in sent.split())

df2 = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T # 2

print(df2[df2.columns[:10]]) # 3

''' 
#1 This is the original sentence defined in.
#2 Normally you should use .splitlines() but here you explicitly add a single '\n'
character to the end of each line/sentence, so you need to explicitly splot on this character.

#3 This shows just the first 10 tokens (DataFrame columns) to avoid wrapping

    == With a quick scan, ypu can see little overlap in word usage for these sentences.
    Among the first seven words in your vocabulary - only the word "aplikacione"
    appeats in more than one sentence. Now you need to be able to compute thie overlap
    within your pipeline whenever you want compare documents or search for similar doc.
    -- One way to check for the similarities between sentences is to count
    the number of overlapping tokens using a dot product 

'''
print('---------------')

'''
    Measuring bag-of-words overlap

    = If you can measure the bag of words overlap for two vectors, we can get
    a good estimate of how similar they are in the words they use.
    And this is a good estimate how similar they are in meaning.



'''

df2 = df2.T

print(df2.sent0.dot(df2.sent1))

print(df2.sent0.dot(df2.sent2))

print(df2.sent0.dot(df2.sent3))

print(df2.sent0.dot(df2.sent4))

print('--------------')

''' 
    From this you can tell that one word was used in both sent0 and sent2.
    Likewise two of the words in the vocabulary was used in both sent0 and sent2

    This overlap of words is a measure of their similarity.

    Here is one way to find the word that is shared by sent0 and sent3

'''

sent02 = [(k, v) for (k, v) in (df2.sent0 & df2.sent1).items() if v]

print(sent02)