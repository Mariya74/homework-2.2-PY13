import chardet

def init_filename():
    filename = input('Введите имя файла для обработки: ')  + '.txt'
    return filename


def get_read():
    f = init_filename()
    code = chardet.detect(open(f, 'rb').read())['encoding']
    return open(f, 'r', encoding=code)


def get_dict_words(f):
    words = {}
    for s in f:
        for word in s.strip().lower().split(' '):
            if len(word) > 6:
                count = words.get(word, 0)
                words[word] = count + 1
    return words


def get_frequent(words):
    rank = list(zip(words.values(), words.keys()))
    rank.sort(reverse=True)

    for s in range(10):
        print(rank[s])


get_frequent(get_dict_words(get_read()))





