from HTMLParser import HTMLParser as hp

class myclass(hp):
    def __init__(self):
        """constructer"""
        hp.__init__(self)
        self.category=''
        self.cat_count=9 
        self.difficulty=''
        self.puz_count=False
        self.puzzel=''
        self.answer=''
        self.hint=''
        self.temp=0
        self.temp1=True
