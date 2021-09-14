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

# Examples

- A Book of homage to Shakespeare.
  
  - 10 most common words:
  
  ('the', 10566), ('of', 7624), ('and', 4504), ('a', 4029), ('to', 3832), ('in', 3609), ('is', 1907), ('that', 1705), ('shakespeare', 1594), ('his', 1594)
  
  - 10 most common words of length greater than 4 letters, excluding the words 'there', 'these', 'other', 'which' :
  
  ('shakespeare', 1594), ('their', 422), ('homage', 363), ('would', 306), ('great', 261), ('world', 220), ('english', 215), ('first', 202), ('plays', 184), ('hamlet', 175)
  
  
- Comparison between 2 manifests, Hitler's "Mein Kampf" and Kazinsky's "Industrial Society and its Future".

  10 most common words of length greater than 4 letters, excluding the words 'they', 'those', 'there' and specified words 'I' :
  
  Mein Kampf:
  
  ('i', 247), ('which', 124), ('german', 81), ('people', 54), ('their', 46), ('first', 39), ('would', 38), ('could', 34), ('became', 32), ('state', 31)
  
  The word "i" appears 247 times (1.61%)
 
 
  Industrial Society and its Future:
  
  ('society', 234), ('system', 220), ('people', 217), ('their', 188), ('would', 154), ('power', 154), ('human', 140), ('technology', 127), ('because', 115), ('other', 95)
  
  The word "i" appears 7 times (0.02%)
  
  
