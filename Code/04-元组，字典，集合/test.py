chars = ['a', 'b', 'c', 'x', 'd', 'p', 's', 't', 'a', 't', 'm', 'n', 'v', 'x', 'z']

# print(chars.count('a'))

char_count = {}

for char in chars:
    if char in char_count:
        # print('字典已经有了该字符%s' % char)
        char_count[char] += 1

    else:
        char_count[char] = 1
print(char_count)