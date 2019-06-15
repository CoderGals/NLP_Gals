import nltk

nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')

len(stop_words)

print(stop_words[:7])