__author__ = 'Oded  Hupert'

from sklearn import datasets
from sklearn import feature_extraction
from sklearn import preprocessing
from sklearn import svm
from sklearn import feature_selection
from sklearn.neighbors import KNeighborsClassifier
import os
import codecs


class classifier(object):
    movies_topic = "movies"
    blather_topic = "blather"
    politics_topic = "politics"
    sport_topic = "sport"

    def classify(self, msg):
        try:
            print("Importing data from folder...")

            # for root, dirs, files in os.walk("./data"):
            #     for file in files:
            #         if file.endswith(".txt"):
            #              file = unicode(file, "utf-8")


            # count = 0
            # for file in os.listdir("./data/politics"):
            #     if file.endswith(".txt"):
            #             with codecs.open("./data/politics/" + str(file), 'r', encoding='utf8') as f:
            #                 lines = f.readlines()
            #                 for line in lines:
            #                     if line is "":
            #                         continue
            #                     with codecs.open("./data/politics/" + str(count) + ".txt", 'w', encoding='utf8') as f1:
            #                         f1.write(line)
            #                         count += 1

            # here we create a Bunch object ['target_names', 'data', 'target', 'DESCR', 'filenames']
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            raw_bunch = datasets.load_files(path, description=None, categories=None, load_content=True,
                                            shuffle=True, encoding='utf-8')
            print("Done!")

            print("Processing text to data...")
            print("     extracting features (no feature selection)...")
            vectorizer = feature_extraction.text.CountVectorizer(input=u'content', encoding=u'utf-8',
                                                                 strip_accents=None, lowercase=True,
                                                                 preprocessor=None, tokenizer=None,
                                                                 # trying with enabled parameters
                                                                 stop_words=None,
                                                                 token_pattern=r'(?u)\b\w\w+\b',
                                                                 ngram_range=(1, 2),
                                                                 analyzer=u'word', max_df=1.0, min_df=3, max_features=None,
                                                                 vocabulary=None, binary=False,
                                                                 dtype='f')
            raw_documents = raw_bunch['data']

            document_feature_matrix = vectorizer.fit_transform(raw_documents)
            feature_names = vectorizer.get_feature_names()

            print("     Done!")
            print("     scaling ...")
            scaler = preprocessing.StandardScaler(copy=True, with_mean=False, with_std=True).fit(document_feature_matrix)
            # We are using sparse matrix so we have to define with_mean=False
            # Scaler can be used later for new objects
            document_feature_matrix = scaler.fit_transform(document_feature_matrix)
            print("     Done!")
            print("Done!")

            print("Building a classifier...")
            print("     selecting features ...")
            # var = feature_selection.VarianceThreshold(threshold=(0.2 * (1 - 0.2)))
            # document_feature_matrix = var.fit_transform(document_feature_matrix)
            # k_best = feature_selection.SelectKBest(k=100)
            # document_feature_matrix = k_best.fit_transform(document_feature_matrix, raw_bunch['target'])
            print("     training...")
            clf = svm.SVC(C=0.1, kernel="linear")
            # clf = KNeighborsClassifier(n_neighbors=2)
            clf.fit(document_feature_matrix, raw_bunch['target'])
            print("Done!")

            print("---------------------------------------")

            print("classification:")

            # with open("./test.txt", "r") as new_obj:
            #     new_obj = new_obj.read().replace('\n', '')
            new_obj = msg
            # new_obj = unicode(new_obj, "utf-8")
            new_obj = vectorizer.transform([new_obj])  # Extracts features
            new_obj = scaler.transform(new_obj)  # scales
            # new_obj = var.transform(new_obj)  # feature selection - var
            # new_obj = k_best.transform(new_obj)  # feature selection - k best

            print("class is: " + raw_bunch['target_names'][clf.predict(new_obj)])
            return raw_bunch['target_names'][clf.predict(new_obj)]
        except Exception as e:
            print(e)
