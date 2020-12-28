from utils import no_accent_vietnamese

class Word: 
    def __init__(self, name, content, category):
        self.name = name
        self.content = content
        self.category = category

    def setName(self, contents):
        self.name = no_accent_vietnamese(contents)
