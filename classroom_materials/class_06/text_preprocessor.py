"""
This script is just intended as a placeholder for your own text preprocessing
script
"""

from collections import Counter


def nltk_tokenizer(txt, lemmatize = False):
    import nltk

    if lemmatize:
        LemmatizerObject = nltk.stem.WordNetLemmatizer()
        tokenized_text = [LemmatizerObject.lemmatize(x) for x in nltk.word_tokenize(txt)]
        return tokenized_text

    return nltk.word_tokenize(txt)


def keras_tokenizer(txt):
    from tensorflow.keras.preprocessing.text import text_to_word_sequence

    return text_to_word_sequence(
        txt, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=False, split=" "
    )


class Text:
    def __init__(self, txt):
        self.txt = txt

    def tokenize(self, method="keras", lemmatize = False):
        if method == "keras":
            self.tokens = keras_tokenizer(self.txt)
        elif method == "nltk" and lemmatize == False:
            self.tokens = nltk_tokenizer(self.txt)
        elif method == "nltk" and lemmatize:
            self.tokens = nltk_tokenizer(self.txt, lemmatize=True)

    def get_frequencies(self):
        return Counter(self.tokens)

    def get_tokens(self):
        return self.tokens
