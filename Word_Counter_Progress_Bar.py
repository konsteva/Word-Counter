import collections
import os
import re
from tqdm import tqdm

# Write the file path 
file_path = 

# Write the specific word(s) to find in the text
specific_words = []

# Excluded words
excluded = []

# Minimum Length
min_len = 0

# Write the number of most common words to be found
number_most_common = 10

# Specifying the encoding
enc = "UTF-8"

# Make a dictionary
wordcount = {}

count = 0

# Check to see if the file is .txt
def Check_filetype(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext != ".txt":
        print("The imported file is not .txt")
        quit()

# Making the dictionary
def Dictionary(file_path, enc):
    num_lines = sum(1 for line in open(file_path, 'r', encoding=enc))

    # Read file
    with open(file_path, encoding=enc) as a:
        for line in tqdm(a, total=num_lines):
            # Inside the [ ] are the symbols that get replaced - hyphen is excluded
            line = re.sub(r"[0-9,.;@#%?!&$:')(/*^\"\[\]\\]+ *", " ", line)
            for word in line.lower().split():
                if (word not in excluded and len(word) >= min_len) or word in specific_words:
                    if word not in wordcount:
                        wordcount[word] = 1
                    else:
                        wordcount[word] += 1
    return wordcount


# Counting how many times every word appears in the txt
def Counter(wordcount):
    counter = collections.Counter(wordcount)
    most_common_counter = collections.Counter(wordcount).most_common(number_most_common)

    print("The {} most common words are {}: ".format(number_most_common, most_common_counter))

    # Finding how many times a specific word comes up
    for word in specific_words:
        print("\nThe word {}{}{} appears {} times".format('"', word, '"', counter[word.lower()]))


if __name__ == "__main__":
    start_time = time.time()

    Check_filetype(file_path)
    Counter(Dictionary(file_path, enc))
