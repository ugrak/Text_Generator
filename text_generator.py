from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams

filename = input()
tk = WhitespaceTokenizer()
with open('./' + filename, 'r', encoding="utf-8") as file:
    tokens = tk.tokenize(file.read())
    bigrams = list(bigrams(tokens))
    print(f'Number of bigrams: {len(bigrams)}')
    while True:
        user_number = input()
        if user_number.lower() == 'exit':
            break
        else:
            try:
                bgrm = bigrams[int(user_number)]
                print(f'Head: {bgrm[0]} Tail: {bgrm[0]}')
            except ValueError:
                print('Type Error. Please input an integer.')
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
