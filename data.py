import urllib
import subprocess as sp
import Queue

home_dir=(sp.Popen('echo ~',shell=True,stdout=sp.PIPE).communicate()[0])[:-1]
class data():

    def get_data(self, url, queue):
        try:
            self.store = urllib.urlopen(url)
            file = open(home_dir+'/.brainteaser/teaser', 'wb')
            file.write(self.store.read())
            file.close()
            queue.put(1)
        except Exception,e:
            print e
            queue.put(2)

if __name__ == '__main__':
    toy = data()
    q=Queue.Queue()
    toy.get_data('http://braingle.com/brainteasers/teaser.php?rand=1',q)
