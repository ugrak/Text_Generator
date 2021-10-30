import string
from random import choice, choices
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter
SENTENCE_LENGTH = 5
AMOUNT_OF_SENTENCES = 10


def build_sentence(bgrms_dict):
    for i in range(AMOUNT_OF_SENTENCES):
        while True:
            last_word = choice(list(bgrms_dict.keys()))
            if last_word[0] in string.ascii_uppercase and last_word[-1] not in '.!?':
                break
        sentence = last_word
        for j in range(SENTENCE_LENGTH - 2):
            last_word = choices(list(bgrms_dict[last_word].keys()), weights=list(bgrms_dict[last_word].values()))[0]
            sentence = sentence + ' ' + last_word
        while True:
            last_word = choices(list(bgrms_dict[last_word].keys()), weights=list(bgrms_dict[last_word].values()))[0]
            if last_word[-1] in '.!?':
                break
        sentence = sentence + ' ' + last_word
        print(sentence)


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
    build_sentence(bigrams_dict)
