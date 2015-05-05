from collections import Counter
import string
import math
import numpy as np
mydoclist = ['Julie loves me more than Linda loves me',
'Jane likes me more than Julie loves me',
'He likes basketball more than baseball']


def l2_normalizer(vec):
    denom = np.sum([el**2 for el in vec])
    return [(el/math.sqrt(denom)) for el in vec]

def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term,document):
    return freq(term,document)

def freq(term,document):
    return document.split().count(term)

def numDocsContaining(word,doclist):
    doccount = 0
    for doc in doclist:
        if freq(word,doc) > 0:
            doccount += 1
    return doccount

def idf(word,doclist):
    n_samples = len(doclist)
    df = numDocsContaining(word,doclist)
    return np.log(n_samples/1.+df)

def build_idf_matrix(idf_vector):
    idf_mat = np.zeros((len(idf_vector),len(idf_vector)))
    np.fill_diagonal(idf_mat,idf_vector)
    return idf_mat

if __name__ == '__main__':
    '''
    for doc in mydoclist:
        tf = Counter()
        for word in doc.split():
            tf[word] += 1
        print tf.items()
    '''
    vocabulary = build_lexicon(mydoclist)
    doc_term_matrix = []
    print 'Our vocabulary vector is [' + ','.join(list(vocabulary)) + ']'
    for doc in mydoclist:
        print 'The doc is "' + doc + '"'
        tf_vector = [tf(word,doc) for word in vocabulary]
        tf_vector_string = ','.join(format(freq,'d') for freq in tf_vector)
        print 'The tf vector for Document %d is [%s]' % (mydoclist.index(doc) + 1,
                                                         tf_vector_string)
        doc_term_matrix.append(tf_vector)
        print 'All combined, here is our master document term matrix: '
        print doc_term_matrix
    doc_term_matrix_l2 = []
    for vec in doc_term_matrix:
        doc_term_matrix_l2.append(l2_normalizer(vec))
    print 'A regular old document term matrix: '
    print np.matrix(doc_term_matrix)
    print '\nA document term matrix with row-wise L2 norms of 1:'
    print np.matrix(doc_term_matrix_l2)

    my_idf_vector = [idf(word,mydoclist) for word in vocabulary]
    print  my_idf_vector
    print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'
    print 'The inverse document frequency vector is [' + ', '.join(format(freq, 'f') for freq in my_idf_vector) + ']'
    print build_idf_matrix(my_idf_vector)

