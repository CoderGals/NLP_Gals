stop_words = ['ka', 'eshte', 'kjo', 'ose', 'edhe', 'marr']
tokens = ['Shtepia', 'ka', 'marr', 'zjarr']

tokens_without_stopwords = [x for x in tokens if x not in stop_words]

print(tokens_without_stopwords)


