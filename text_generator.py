from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter

filename = input()
tk = WhitespaceTokenizer()
with open('./' + filename, 'r', encoding="utf-8") as file:
    tokens = tk.tokenize(file.read())
    bigrams_list = list(bigrams(tokens))
    bigrams_dict = {}
    for element in bigrams_list:
        bigrams_dict.setdefault(element[0], []).append(element[1])
    for element in bigrams_list:
        bigrams_dict[element[0]] = Counter(bigrams_dict[element[0]])
    while True:
        user_word = input()
        if user_word.lower() == 'exit':
            break
        else:
            try:
                content = bigrams_dict[user_word]
                print(f'Head: {user_word}')
                for key, value in content.most_common():
                    print(f'Tail: {key}    Count: {value}')
            except KeyError:
                print('Key Error. The requested word is not in the model. Please input another word.')
