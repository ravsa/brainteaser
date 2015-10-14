import urllib
import thread
class data():
    def get_data(self,url):
        try:
            self.store=urllib.urlopen(url)
            file=open('teaser','wb')
            file.write(self.store.read())
            file.close()
            self.local=1
        except:
            self.local=2
    def set_data(self,url):
        self.local=0
        thread.start_new_thread(self.get_data,(url,))
        while self.local==0:
            pass
if __name__=='__main__':
    toy=data()
    toy.set_data('http://braingle.com/brainteasers/teaser.php?rand=1')
