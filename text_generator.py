from nltk.tokenize import WhitespaceTokenizer

filename = input()
tk = WhitespaceTokenizer()
with open('./' + filename, 'r', encoding="utf-8") as file:
    tokens = tk.tokenize(file.read())
    print(f'Corpus statistics\nAll tokens: {len(tokens)}\nUnique tokens: {len(set(tokens))}')
    while True:
        user_number = input()
        if user_number.lower() == 'exit':
            break
        else:
            try:
                print(tokens[int(user_number)])
            except ValueError:
                print('Type Error. Please input an integer.')
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
