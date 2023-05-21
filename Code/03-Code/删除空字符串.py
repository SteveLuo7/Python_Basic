# 删除空字符串

words = ['hello', '', 'good', '', 'yes']
# for word in words:
#     if word == '':
#         words.remove(word)
# print(words)
words2 = []
for word in words:
    if word != '':
        words2.append(word)
words = words2
print(words)
