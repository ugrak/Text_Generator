from random import choice, choices
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter
SENTENCE_LENGTH = 10

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
    for i in range(SENTENCE_LENGTH):
        last_word = choice(list(bigrams_dict.keys()))
        sentence = last_word
        for j in range(SENTENCE_LENGTH - 1):
            last_word = choices(list(bigrams_dict[last_word].keys()), weights=list(bigrams_dict[last_word].values()))[0]
            sentence = sentence + ' ' + last_word
        print(sentence)
