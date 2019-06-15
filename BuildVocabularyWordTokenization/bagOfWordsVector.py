sentence1 = "Albiona Hoti filloi punen si software engineer ne moshen 22."


sentence_bow = {}
for token in sentence1.split():
  sentence_bow[token] = 1

print(sorted(sentence_bow.items()))