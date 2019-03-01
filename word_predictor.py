import random
import pickle
import json
from ngram import setNgram, getNgram, FILE, NGRAM_FILE

def get_file_content(filename):
    with open(f'./data/{filename}.txt', 'rb') as f:
        my_list = pickle.load(f)
        return my_list

def write_file_content(filename, content):
    with open(f'./data/{filename}.txt', 'a+') as f:
        f.write(content)
        f.write("\n")

def get_highest_counter(choices):
	maximum = 0
	for item in choices:
		if maximum < item[1]:
			maximum = item[1]
	return maximum

def get_most_used_word(choices, maximum):
	arr = []
	for item in choices:
		if(item[1] == maximum):
			arr.append(item[0][1])
	total = len(arr)
	if(total == 1):
		return arr[0]
	r = random.uniform(0, total)
	return arr[int(r)]

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


def getNgramSequence(gram, word):
    arr = []
    maximum = -1
    for item in gram:
        if item[0][0] == word and item[1] >= maximum:
            arr.append(item)
            if item[1] > maximum:
                maximum = item[1]
    
    print(arr)
    if len(arr) > 0:
        item = random.choice(arr)
        return list(item[0])
    return []

def getNGramSentence(gram, word, n = 50):
    arr = []
    for i in range(n):
        arr.append(word)
        choices = [element for element in gram if element[0][0] == word]
        if not choices:
            break
        
        word = get_most_used_word(choices, get_highest_counter(choices))
    return arr

def getNgramFromFile():
    ngram = get_file_content(NGRAM_FILE)
    return ngram

def getSuggestedSentence(searchText):
    ngram = get_file_content(NGRAM_FILE)
    word_sequence = getNgramSequence(ngram, searchText.lower())
    sentence = ' '.join(word_sequence[1:])
    return sentence

def save_text(text):
    write_file_content(FILE, text)
    setNgram()

if __name__ == "__main__":
    setNgram()
    pass