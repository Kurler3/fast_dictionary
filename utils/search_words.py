from utils.extract_word import extract_word

# Function to search for matching words


def search_words(lines, query):
    matches = []
    for line in lines:
        eng_word, _, _ = extract_word(line)
        if eng_word.lower().startswith(query.lower()):
            matches.append(line.strip())
    return matches
