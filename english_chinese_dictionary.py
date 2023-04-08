import tkinter as tk
from utils.extract_word import extract_word
from utils.search_words import search_words

with open('words.txt', 'r') as f:
    lines = f.readlines()

matches = []

# Function to display the word details
def show_word_details(event):
    
    global matches
    
    # Get the selected word from the listbox
    selection = listbox.curselection()
    if selection:
        index = selection[0]
     
        line = matches[index]
        # Extract the word details
        eng_word, word_type, ch_meaning = extract_word(line)

        # Update the entry fields with word details
        eng_word_entry.delete(0, tk.END)
        eng_word_entry.insert(0, eng_word)
        word_type_entry.delete(0, tk.END)
        word_type_entry.insert(0, word_type)
        ch_meaning_entry.delete(0, tk.END)
        ch_meaning_entry.insert(0, ch_meaning)

# Function to update the matches list
def update_matches(event):
    
    global matches
    
    # Get the query string from the entry field
    query = query_entry.get()

    if not query:
        listbox.delete(0, tk.END)
        count_label.config(text="")
        return
    
    matches.clear()
    # Get the matching words
    matches = search_words(lines, query)
    
    # Update the matches list
    listbox.delete(0, tk.END)
    for match in matches:
        eng_word, _, _ = extract_word(match)
        listbox.insert(tk.END, eng_word)
        
        
    
    # Update the match count label
    count_label.config(text=f"{len(matches)} matches found")    
    

# Create the GUI
root = tk.Tk()
root.title("Smart English-Chinese Dictionary")

# Create the widgets

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
listbox.configure(yscrollcommand=listbox_scrollbar.set)

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

# Bind events
query_entry.bind("<KeyRelease>", update_matches)
listbox.bind("<ButtonRelease-1>", show_word_details)

# Pack the widgets
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

# RUNNING THIS SCRIPT AS THE MAIN FILE => CALL THE MAIN FUNC
if __name__ == '__main__':
    # Start the main loop
    root.mainloop()     