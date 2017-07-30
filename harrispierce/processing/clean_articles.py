
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import string


def clean_article(article):

    tokenized_article = tokenize(article)
    no_bad_tokens_article = remove_bad_tokens(tokenized_article)
    no_stop_words_article = remove_stop_words(no_bad_tokens_article)

    return no_stop_words_article


def tokenize(article):
    # import word tokenizer

    # Apply word_tokenize to each element of the list called incoming_reports
    tokenized_lines = [word_tokenize(line) for line in article]

    # View tokenized_reports
    return tokenized_lines


def remove_bad_tokens(tokenized_article):

    regex = re.compile('[%s]' % re.escape(string.punctuation))
    tokenized_article_no_punctuation = []

    for line in tokenized_article:

        new_line = []
        for token in line:
            new_token = regex.sub(u'', token)
            if not new_token == u'':
                new_line.append(new_token)

        tokenized_article_no_punctuation.append(new_line)

    return tokenized_article_no_punctuation


def remove_stop_words(no_bad_tokens_article):

    tokenized_article_no_stopwords = []
    for line in no_bad_tokens_article:
        new_term_vector = []
        for word in line:
            if word not in stopwords.words('english'):
                new_term_vector.append(word)
        tokenized_article_no_stopwords.append(new_term_vector)

    return tokenized_article_no_stopwords
