from nltk.tokenize import TreebankWordTokenizer

sentence = "Albiona Hoti filloi punen si s'ishte software engineer ne moshen 22."

tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(sentence))