import tkinter as tk
import time

from utils.extract_word import extract_word
from utils.search_words import search_words

##########################################
## INIT DATA #############################
##########################################

# LOAD ALL LINES INITIALLY
with open('words.txt', 'r') as f:
    lines = f.readlines()

# INIT MATCHES ARRAY
matches = []

##########################################
## FUNCTIONS #############################
##########################################

# Function to display the word details
def show_word_details(event):
    
    global matches
    
    # Get the selected word from the listbox
    selection = listbox.curselection()
    if selection:
        index = selection[0]
     
        line = matches[index]
   
        # Update the entry fields with word details
        eng_word_entry.delete(0, tk.END)
        eng_word_entry.insert(0, line[0])
        word_type_entry.delete(0, tk.END)
        word_type_entry.insert(0, line[1])
        ch_meaning_entry.delete(0, tk.END)
        ch_meaning_entry.insert(0, line[2])

# Function to update the matches list
def update_matches(event):
    
    # USE MATCHES FROM OUTER BLOCK
    global matches
    
    # Get the query string from the entry field
    query = query_entry.get()

    # CLEAN WORD DETAILS LABELS
    eng_word_entry.delete(0, tk.END)
    word_type_entry.delete(0, tk.END)
    ch_meaning_entry.delete(0, tk.END)
    
    # IF NO QUERY INPUT => CLEAR LIST BOX AND COUNT LABEL
    if not query:
        listbox.delete(0, tk.END)
        count_label.config(text="")
        return
    
    # Start the timer
    start_time = time.time()
    
    # EMPTY MATCHES ARRAY
    matches.clear()
    
    # Get the matching words
    matches = search_words(lines, query)
    
    # End the timer
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    
    # Update the matches list
    listbox.delete(0, tk.END)
    for match in matches:
        # PUSH THE ENGLISH WORD TO THE LIST BOX
        listbox.insert(tk.END, match[0])
        
    # Update the match count label
    count_label.config(text=f"{len(matches)} matches found")    
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    
    
##########################################
# CREATE THE GUI #########################
##########################################

root = tk.Tk()
root.title("Fast English-Chinese Dictionary")

##########################################
# CREATE THE WIDGETS #####################
##########################################

# QUERY LABEL
query_label = tk.Label(root, text="Enter query:")

# QUERY INPUT BOX
query_entry = tk.Entry(root)

# COUNT LABEL
count_label = tk.Label(root, text="")

# LIST BOX 
listbox = tk.Listbox(root, width=70, height=30)

# LIST BOX SCROLLBAR
listbox_scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)

# ENG WORD LABEL
eng_word_label = tk.Label(root, text="English Word:")

# ENG WORD ENTRY
eng_word_entry = tk.Entry(root)

# WORD TYPE LABEL
word_type_label = tk.Label(root, text="Word Type:")

# WORD TYPE ENTRY
word_type_entry = tk.Entry(root)

# CHINESE MEANING LABEL
ch_meaning_label = tk.Label(root, text="Chinese Meaning:")

# CHINESE MEANING ENTRY
ch_meaning_entry = tk.Entry(root)

# BIND EVENTS
query_entry.bind("<KeyRelease>", update_matches)
listbox.bind("<ButtonRelease-1>", show_word_details)

# PACK THE WIDGETS
query_label.pack()
query_entry.pack()
count_label.pack()
listbox.pack()
eng_word_label.pack()
eng_word_entry.pack()
word_type_label.pack()
word_type_entry.pack()
ch_meaning_label.pack()
ch_meaning_entry.pack()

##########################################################################
# RUNNING THIS SCRIPT AS THE MAIN FILE => CALL THE MAIN FUNC #############
##########################################################################

if __name__ == '__main__':
    # START THE GUI PROGRAM
    root.mainloop()     