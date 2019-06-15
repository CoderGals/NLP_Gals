from nltk.tokenize import RegexpTokenizer
sentence = "Albiona Hoti filloi punen si software engineer ne moshen 22."

tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')

print(tokenizer.tokenize(sentence))