# Word-Counter

This is a Python 3 script for quantitive analysis of document files. The script returns the most common words and their count and it also gives the ability to the user to search for one or more specific words and see their count. The script ignores hypens and counts words seperated by it as one while it deletes any other punctuation.

# Details

The script can take multiple files as input (txt, docx, csv, json, html, epub, biblatex, bibtex, docbook and many others) and it converts the file to txt. It creates a dictionary with all the unique words that appear in the text and returns the most common ones along with the user specified ones. Time efficiency is considered here but more emphasis is given on memory efficiency. This is done to be able to deal with large files and to minimize memory leaks.

# Features
- Returns most common words of the text. The user can specify the number of most common words.

- Returns the count of one or more user specified words and also includes percentages

- Searching for words that are bigger than a specified length

- Excluded words specified by the user that the script will ignore and not count.

- Simple progress bar

- Easy to specify the encoding in case it's not UTF-8
