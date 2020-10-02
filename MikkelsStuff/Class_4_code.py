'''
Group exercises
Part 1: Practice Problems
We want to build a naive bayes sentiment classifier using add-1 smoothing, as described in the lecture (not binary naive bayes, regular naive bayes). Here is our training corpus:
_______
Training Set:

- just totally dull 
- completely predictable and lacking energy
- no surprises and very few laughs 
+ very profound 
+ the most fun film of the summer 
_______
Test Set:

predictable with no originality 
_______
1. Compute the prior for the two classes + and -, and the likelihoods for each word given the class (leave in the form of fractions).

2. Then compute whether the sentence in the test set is of class positive or negative (you may need a computer for this final computation).

3. Would using binary multinomial Naive Bayes change anything?

4. Why do you add |V| to the denominator of add-1 smoothing, instead of just counting the words in one class?

5. What would the answer to question 2 be without add-1 smoothing?

6. Can you think of any other features (or preprocessing) that you could add that might be useful in predicting sentiment? (This will come in handy for next HW!).

7. Naive Bayes treats words as if they are independent conditioned upon the class (that is why we multiply the individual probabilities). For which (if any) of the new features you suggested does this independence assumption roughly hold?


Part 2: Challenge Problems
1. Go to the Sentiment demo at http://nlp.stanford.edu:8080/sentiment/rntnDemo.html. Come up with 5 sentences that the classifier gets wrong. Can you figure out what is causing the errors?

It is sometimes the case that more complex features (like trigrams or bigrams) perform better than simple features (like unigrams) on the training set, but perform worse than simple features on the test set. This is a particular case of the phenomenon called `overfitting' in machine learning. Discuss why this might be. Can you create a tiny training set with 2 3-word documents and a test set with one document for which this overfitting situation holds?
Binary multinomial NB seems to work better on some problems than full count NB, but full count works better on others. For what kinds of problems might binary NB be better, and why? (There is no known right answer to this question, but I'd like you to think about the possibilities.)
'''

import re
import math
from text_processor_functions import *

training_set = '''
- just totally dull 
- completely predictable and lacking energy
- no surprises and very few laughs 
+ very profound 
+ the most fun film of the summer 
'''

test_set = "predictable with no originality" 

### JUST TO GET A HANG OF IT: CALCULATION FOR "the" maximum likelihood:

#P("the"| +) = 2+1/(9+20) = 3/29 (!!!) which is what we get.

def get_words(sentences):
    return [item for sublist in tokenize(sentences) for item in sublist if item != ""]

def naive_bayes(D):
    #initialize 
    positives = 0
    negatives = 0
    positive_words = []
    negative_words = []
    split_text = re.split("[\s]*\n[\s]*", D.strip())
    total_count = len(split_text)
    all_words = get_words(split_text)
    log_likelihood = {}

    for i in split_text:
        if i[0] == "+":
            positives += 1
            text = re.split("[\s]*\n[\s]*", i.strip())
            positive_words.append(i)
        else:
            negatives += 1
            text = re.split("[\s]*\n[\s]*", i.strip())
            negative_words.append(i)


    log_prior = {"+": positives/total_count, "-": negatives/total_count}
    
    positive_words = get_words(positive_words)
    negative_words = get_words(negative_words)

    counts_total = token_frequencies(all_words)
    counts_positive = token_frequencies(positive_words)
    counts_negative = token_frequencies(negative_words)

    cardinal = len(counts_total)
    sum_pos = sum(counts_positive.values())
    sum_neg = sum(counts_negative.values())

    pos_dict = {}
    neg_dict = {}

    for word in all_words:
        if counts_positive.get(word) != None:
            pos_freq = counts_positive[word]
        else: 
            pos_freq = 0
        if counts_negative.get(word) != None:
            neg_freq = counts_negative[word]
        else:
            neg_freq = 0
        pos_dict[word] = (pos_freq+1)/(sum_pos + cardinal)
        neg_dict[word] = (neg_freq+1)/(sum_neg + cardinal)


    return (log_prior, pos_dict, neg_dict, list(counts_total.keys()))


def test_naive_bayes(testdoc, logprior, log_like_pos, log_like_neg, V):
    positive,negative = logprior.values()
    tokenized_test = tokenize(sentence_segment(testdoc))
    
    for i in tokenized_test[0]:
        if i in V:
                positive = positive * log_like_pos.get(i)
                negative = negative * log_like_neg.get(i)

    if positive > negative:
        return ("positive", positive)
    else:
        return ("negative", negative)

log_prior, log_like_pos, log_like_neg, V = naive_bayes(training_set)


test_naive_bayes(test_set, log_prior, log_like_pos, log_like_neg, V)