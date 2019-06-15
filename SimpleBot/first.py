import re

r = "(hi|hello|hey)[ ]*([a-z]*)"

print(re.match(r, 'Hello Albiona', flags=re.IGNORECASE))

print('-----')

'''
    '|' means "OR" and '\*' => means the preceding character can occur 0
    or more times and still match. So our regex will match greetings that
    start 'hi' or 'hello' or 'hey'

    - Specify a character class => using  [ ]
    - then use a dash ( - ) to indicate a range of characters without having to type them all.
    - "[a-z]" -> any single lowercase letter, "a" through "z"
    - the '*' -> after a character class means that the regular expression will amtch any
    number of consecutive characters if they are all within that character class.
    
    

'''


r2 = r'''[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']
{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})'''

re_greeting = re.compile(r2, flags=re.IGNORECASE)
# You can compile regular expressions so you don't have to specify
# the options (flags) each time you use it.

print(re_greeting.match('Hello Rosa'))


print(re_greeting.match('Hello Rosa').groups())


print(re_greeting.match('Good evening Rosa Parks').groups())
print('-----')

print(re_greeting.match("Good Morning Rosa"))

print(re_greeting.match("Good morning Rosa"))


print(re_greeting.match("Yo rosa").groups())


'''
    1.  You can compile regular expressions so you don't have to
    specify the options (flags) each time you use it.
    2.  Notice that this regular expression cannot recognize(match) words with types.
    3.  Out chatbot - can separate different parts of the greeting
        into groups, but it will be unaware of Rosa's famous last
        name, -> we don't have any pattern to match any character
        after the first name.

        - The 'r' before the quote specifies a raw string, not a regular
        expression.
'''

# Create a "template" for our chatbot response:

my_names = set(['rosa', 'rose', 'chatty', 'chatbot', 'bot', 'chatterbot'])

curt_names = set(['hal', 'you', 'u'])

greeter_name = ''

match = re_greeting.match(input())

if match:
    at_name = match.groups()[-1]
    if at_name in curt_names:
        print("Good one.")
    elif at_name.lower() in my_names:
        print("Hi {}, How are you?".format(greeter_name))

















































