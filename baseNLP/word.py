from utils import no_accent_vietnamese

class Word: 
    def __init__(self, name, content, category, ngram, agr):
        self.name = name
        self.content = content
        self.category = category
        self.agr = agr

    def setName(self, contents):
        self.name = no_accent_vietnamese(contents)
