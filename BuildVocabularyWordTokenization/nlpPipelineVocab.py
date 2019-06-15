# 1million tokens in your NLP pipeline vocabulary

num_rows = 3000 * 3500 * 15

print(num_rows)

print('-----------')

num_bytes = num_rows * 1000000
print(num_bytes)

print('-----------')

again = num_bytes/1e9
print(again)

print('terabytes\n',again/1000)
