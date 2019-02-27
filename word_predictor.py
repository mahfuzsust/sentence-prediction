import re
import random

def get_file_content(filename):
    with open(f'./data/{filename}', 'r') as f:
        txt = f.read()
    return txt

def get_data_words():
    content = get_file_content('pride_and_prejudice.txt')
    content = content + get_file_content('hucleberry_finn.txt')
    words = re.split('[^A-Za-z]+', content.lower())
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

def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w > r:
         return c
      upto += w

def getNGramSentenceRandom(gram, word, n = 50):
    arr = []
    for i in range(n):
        arr.append(word)
        choices = [element for element in gram if element[0][0] == word]
        if not choices:
            break
        
        word = weighted_choice(choices)[1]
    return arr

def getWord():
    pass

def getSuggestedSentence(searchText):
    ngram = generateNgram(get_data_words(), n=5)
    word_sequence = getNGramSentenceRandom(ngram, searchText, 5)
    sentence = ' '.join(word_sequence[1:])
    return sentence

if __name__ == "__main__":
    getSuggestedSentence("hello")