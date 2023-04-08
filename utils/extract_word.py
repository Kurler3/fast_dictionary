# Function to extract English word and Chinese meaning from a line in the file
def extract_word(line):
    parts = line.split(' ')
    eng_word = parts[0]
    word_type = parts[1].split('.')[0]
    ch_meaning = ''.join(parts[1].split('.')[1:]).strip()
    return eng_word, word_type, ch_meaning