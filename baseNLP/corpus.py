from baseNLP.word import Word

class Corpus:
    def __init__(self, word_list, n_gram):
        self.word_list = word_list
        self.n_gram = n_gram    
    
