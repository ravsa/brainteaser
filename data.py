import urllib
class data():
    def __init__(self):
        self.local=0
    def get_data(self,url):
        try:
            self.store=urllib.urlopen(url)
            file=open('teaser','wb')
            file.write(self.store.read())
            file.close()
            self.local=1
        except:
            self.local=2
if __name__=='__main__':
    toy=data()
    toy.get_data('http://braingle.com/brainteasers/teaser.php?rand=1')
