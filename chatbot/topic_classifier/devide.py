__author__ = 'Oded  Hupert'

import os
import codecs

print("Importing data from folder...")

# for root, dirs, files in os.walk("./data"):
#     for file in files:
#         if file.endswith(".txt"):
#              file = unicode(file, "utf-8")


count = 0
for file in os.listdir("./data/movies"):
    if file.endswith(".txt"):
            with codecs.open("./data/movies/" + str(file), 'r', encoding='utf8') as f:
                lines = f.readlines()
                for line in lines:
                    if line is "":
                        continue
                    with codecs.open("./data/movies/" + str(count) + ".txt", 'w', encoding='utf8') as f1:
                        f1.write(line)
                        count += 1

# here we create a Bunch object ['target_names', 'data', 'target', 'DESCR', 'filenames']