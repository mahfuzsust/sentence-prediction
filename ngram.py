import re
import pickle
FILE = "data_file"
NGRAM_FILE = "ngram_file"

def get_file_content(filename):
    with open(f'./data/{filename}.txt', 'r') as f:
        txt = f.read()
    return txt

def write_file_content(filename, content):
    with open(f'./data/{filename}.txt', 'wb') as f:
        pickle.dump(content, f)

def get_data_words():
    content = get_file_content(FILE)
    words = re.compile("([\w][\w]*'?\w?)").findall(content.lower())
    words = list(filter(None, words))
    return words

def generateNgram(words, n=1):
    assert n > 0 and n < 100
    gram = dict()
    for i in range(len(words)-(n-1)):
        key = tuple(words[i:i+n])
        if key in gram:
            gram[key] += 1
        else:
            gram[key] = 1
    
    gram = sorted(gram.items(), key=lambda x: x[1], reverse=True)
    return gram

def setNgram():
    ngram = generateNgram(get_data_words(), 4)
    write_file_content(NGRAM_FILE, ngram)

def getNgram():
    return ngram
