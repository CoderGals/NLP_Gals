import re
sentence = """Albiona Hoti filloi punen si software engineer ne moshen 22."""

pattern = re.compile(r"([-\s.,;!?])+")

tokens = pattern.split(sentence)

print(tokens[-10:])

print([x for x in tokens if x and x not in '- \t\n.,;!?'])

# If you want practice with lambda and filter(), use
#  list(filter(lambda x: x if x and x not in '- \t\n.,;!?' else None, tokens))