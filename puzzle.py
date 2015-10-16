from HTMLParser import HTMLParser as hp

class myclass(hp):
    def __init__(self):
        """constructer"""
        hp.__init__(self)
        self.category=''
        self.cat_count=9 
        self.difficulty=''
        self.puz_count=False
        self.puzzle=''
        self.answer=''
        self.hint=''
        self.temp=0
        self.temp1=True
    def handle_starttag(self, tag,attr):
        """"""
        if str(tag) == 'div' :
            if 'hint_s' in [j for i in attr for j in i]:
                self.temp=1
            if 'ans_s' in [j for i in attr for j in i]:
                self.temp=2
        if str(tag) == 'span':
            if 'textblock' in [j for i in attr for j in i]:
                if self.temp==1 and self.hint =='':
                    self.puz_count=3
                if self.temp==2 and self.answer=='':
                    self.puz_count=1
        if str(tag) == 'div' :
            if  'textblock' in [j for i in attr for j in i] and self.puzzle=='':
                self.puz_count=2
        if str(tag) == 'td':
                self.cat_count-=1
    def handle_endtag(self, tag):
        if str(tag) == 'span':
            self.temp=0
    def handle_data(self, data=None):
        """handle data"""
        if  self.puz_count ==  1 :
            for i in (data.split('\n')):
                if i.find('Hide') != -1:
                    self.temp1=False
                    break
                elif self.temp1:
                    self.answer+=i+'\n'
        if  self.puz_count ==  2 :
            self.puzzle+=data
        if  self.puz_count ==  3 :
            self.hint+=data
        if  self.cat_count ==  0 :
            self.category+=data
        if  self.cat_count ==  2:
            self.difficulty+=data
if __name__ =="__main__":
        my=myclass()
        file=open('test.html','r')
        my.feed(file.read())
        my.filt_call()
        my.category
