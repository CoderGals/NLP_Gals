import re

sentence = """Albiona Hoti filloi punen si software engineer ne moshen 22."""

tokens = re.split(r'[-\s.,;!?]+', sentence) # 1

'''
    This splits the sentence on whitespace or punctuation that occurs at least once
    (note the + after the closing square bracket in the regular expression).
'''

print(tokens)