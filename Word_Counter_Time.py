import collections
import re
import os
import time

# Write the file path
file_path = "Shakespeare - A book of Homage 10 times.txt"

# Write the specific word(s) to find in the text
specific_words = ["Elizabeth"]

# Write the number of most common words to be found
number_most_common = 10

# Specifying the encoding
enc = "UTF-8"

# Check to see if the file is .txt, if not terminate
extension = os.path.splitext(file_path)[-1].lower()
if extension != ".txt":
    print("The imported file is not .txt")
    quit()


def WordCounter(path, common_words, spec_words):

    # Read file
    file = open(path, encoding=enc)
    a = file.read()
    a = a.lower()

    # Finds all the words and reacts to words split by hyphen as one word
    # You can set a minimum character length (currently set as 0, meaning that it counts all words)
    words = re.findall(r'\w{0}[a-zA-Z_\-]+', a)

    # Making a dictionary containing all the words and their count
    counter = collections.Counter(words)
    most_common_counter = collections.Counter(words).most_common(common_words)

    # Printing the top common words and their count
    print("The {} most common words are {}: ".format(common_words, most_common_counter))

    # Printing the specified words and their count
    for word in spec_words:

        print("\nThe {}{}{} appears {} times".format('"', word, '"', counter[word.lower()]))

    # Close the file
    file.close()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    start_time = time.time()
    WordCounter(file_path, number_most_common, specific_words)