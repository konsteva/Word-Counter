import collections
import os
import re
from tqdm import tqdm
import pypandoc


start_time = time.time()

file_path = "Industrial Society and its Future.txt"

# Specific word(s) to find in the text
specific_words = ["society", "system", "people", "power", "human", "technology", "because", "other", "social", "modern", "world"]

# Excluded words
excluded = ['would', 'their', 'which']

# Minimum Length of word (in letters)
min_len = -1

# Write the number of most common words to be found
number_most_common = 10

# Specifying the encoding
enc = "UTF-8"

# Make a dictionary
wordcount = {}

count = 0


# Check to see if the file is .txt and converts to .txt in other case
def Check_filetype(file_path):

    ext = os.path.splitext(file_path)[-1].lower()
    if ext != ".txt":
        try:
            output = pypandoc.convert_file(file_path, 'plain', outputfile="somefile.txt")
            assert output == ""
        except RuntimeError:
            print("Invalid input format! Got {} but expected one of these: biblatex, bibtex, commonmark, "
                  "commonmark_x, creole, csljson, csv, docbook, docx, dokuwiki, epub, fb2, gfm, haddock, html, ipynb, "
                  "jats, jira, json, latex, man, markdown, markdown_github, markdown_mmd, markdown_phpextra, "
                  "markdown_strict, mediawiki, muse, native, odt, opml, org, rst, t2t, textile, tikiwiki, twiki,vimwiki"
                  .format(ext))
            quit()


# Making a dictionary
def Dictionary(file_path, enc):
    total_words = 0
    try:
        num_lines = sum(1 for line in open(file_path, 'r', encoding=enc))
        # Read file
        with open(file_path, encoding=enc) as a:
            for line in tqdm(a, total=num_lines):
                # Replace symbols - hyphen is excluded
                line = re.sub(r"[0-9,.;@#%?!&$:')(/*^\"\[\]\\]+ *", " ", line)
                for word in line.lower().split():
                    total_words += 1
                    if (word not in excluded and len(word) >= min_len) or word in specific_words:
                        if word not in wordcount:
                            wordcount[word] = 1
                        else:
                            wordcount[word] += 1
        print(total_words)
        # Returns the dictionary and the total word count of the document
        return wordcount, total_words
    except IOError:
        print('There was an error while loading the file')
        quit()

    except UnicodeDecodeError:
        print("The file encoding isn't {}".format(enc))
        quit()


# Counting how many times every word appears in the document
def Counter(wordcount, total_words):
    counter = collections.Counter(wordcount)
    most_common_counter = collections.Counter(wordcount).most_common(number_most_common)

    print("The {} most common words are {}: \n".format(number_most_common, most_common_counter))

    # Finding how many times a specific word comes up and its percentage
    for word in specific_words:
        print('The word "{}" appears {} times ({:.2f}%)'.format(word, counter[word.lower()],
                                                                counter[word.lower()] / total_words * 100))


if __name__ == "__main__":

    Check_filetype(file_path)
    wordcount, total_words = Dictionary(file_path, enc)
    Counter(wordcount, total_words)
    
