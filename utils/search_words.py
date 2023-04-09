from utils.extract_word import extract_word



# Function to search for matching words
def search_words(lines, query):
    
    # INIT MATCHES
    matches = []
    
    # FOR EACH LINE
    for line in lines:
        # EXTRACT THE DATA FROM THAT LINE
        eng_word, word_type, ch_meaning = extract_word(line)
        
        # IF THE ENGLISH WORD MATCHES WITH THE QUERY
        if eng_word.lower().startswith(query.lower()):
            # PUSH ARRAY WITH ENGLISH WORD, WORD TYPE AND CHINESE MEANING
            matches.append([eng_word, word_type, ch_meaning])
            
    # RETURN MATCHES ARRAY
    return matches
