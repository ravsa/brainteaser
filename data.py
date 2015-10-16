import urllib

class data():

    def get_data(self, url, queue):
        try:
            self.store = urllib.urlopen(url)
            file = open('teaser', 'wb')
            file.write(self.store.read())
            file.close()
            queue.put(1)
        except:
            queue.put(2)

if __name__ == '__main__':
    toy = data()
    toy.get_data('http://braingle.com/brainteasers/teaser.php?rand=1')
