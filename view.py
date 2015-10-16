import gobject
import warnings
import Queue 
import pango
import gtk
import threading
from data import data
from puzzle import myclass as pz
category, difficulty, puzzle, answer, hint = '', '', '', '', '',

gobject.threads_init()

def load():
    global category, difficulty,puzzle,answer,hint
    pop=pz()
    file=open('teaser','r')
    pop.feed(file.read())
    category=pop.category
    category=category.replace(' ','')
    category=category.replace('\r','')
    category=category.replace('\n','').upper()
    difficulty=pop.difficulty.replace('\n','')
    difficulty=difficulty.replace('(','')
    difficulty=float(difficulty.replace(')',''))
    puzzle=pop.puzzle.replace('\n\n\n','') 
    puzzle=puzzle.replace('\r','')
    puzzle=puzzle.replace('Hint','')
    puzzle=puzzle.replace('Answer','')+'\n'
    answer=pop.answer
    answer=answer.replace('\n\n\n','\n') 
    answer=answer.replace('\n\n','\n') 
    answer=answer.replace('\r','') 
    answer='[Answer:]\n\n'+answer+'\n\n'
    hint=pop.hint
    hint=hint.replace('\n\n\n','') 
    hint=hint.replace('Hide','')
    hint=hint.replace('Show Hint','')
    hint=hint.replace('Answer','')
class view(threading.Thread):
    def __init__(self):
        """TODO: to be defined1. """
        warnings.filterwarnings('ignore')
        self.main_window=gtk.Window()
        self.main_window.connect('destroy',lambda x:gtk.main_quit())
        self.main_window.set_default_size(gtk.gdk.screen_width()-100,gtk.gdk.screen_height()-100)
        self.main_hbox=gtk.HBox()
        self.side=True
        self.default_add='http://braingle.com/brainteasers/'
#Three vertical boxes
        self.vbox_one=gtk.VBox()
        self.vbox_two=gtk.VBox()
        self.vbox_three=gtk.VBox()
#scroll window
        self.view1=gtk.ScrolledWindow()
        self.view2=gtk.ScrolledWindow()
        self.view1.set_border_width(4)
        self.view2.set_border_width(4)
#loader
        self.loader_cont=gtk.VBox()
        self.loader=gtk.Label()
        self.loader.set_markup('<span color="green" size="16000">Loading....</span>')
        self.loader_cont.pack_start(self.loader,True)
#pack three boxes in window into main Horizontal box
        self.wid_one=0
        self.wid_two=200
        self.main_window.add(self.main_hbox)
        self.main_hbox.pack_start(self.vbox_one,False)
        self.main_hbox.pack_start(self.vbox_two,False)
        self.vbox_two.set_size_request(self.wid_two,gtk.gdk.screen_height()-100)
        self.vbox_one.set_size_request(self.wid_one,gtk.gdk.screen_height()-100)
        self.main_hbox.pack_start(self.vbox_three,False)
        self.sidebar()
        load()
        self.details()
        self.question()
        self.main_window.show_all()
        self.update()
        self.view2.hide()
        self.action()
        self.loader_cont.hide()
        self.vbox_one.hide()
        gtk.main()
    def refresh(self):
        self.cat_lab.set_text(category)
        self.diff_lab.set_text('{  '+str(difficulty)+'  }')
        self.text_buffer1.set_text(puzzle)
        self.update()
    def opn(self,etc,url):
        queue=Queue.Queue()
        self.loader_cont.show()
        dt=data()
        data_thread=threading.Thread(target=dt.get_data,args=(url,queue))
        data_thread.start()
        def idont(self):
            xor=queue.get()
            if xor == 1 or xor == 2:
                store=xor
            else:
                store=0
            if store == 2:
                self.loader_cont.hide()
                self.temp_cont=gtk.HBox()
                self.temp_lab=gtk.Label()
                self.temp_lab.set_markup('<span size="20000" color="red">ERROR: Connection failed</span>')
                self.temp_cont.pack_start(self.temp_lab,True)
                self.view1.add(self.temp_cont)
                self.view1.show_all()
                return False
            if store == 1:
                load()
                self.vbox_two.show_all()
                self.refresh()
                self.loader_cont.hide()
                return False
            return True
        gobject.timeout_add(1,idont,self)
    def sidebar(self):
        self.language=gtk.Button('Language')
        self.language.set_size_request(200,33)
        self.language.modify_bg(gtk.STATE_NORMAL,self.language.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.language,False)
        self.logic=gtk.Button('Logic')
        self.logic.set_size_request(200,33)
        self.logic.modify_bg(gtk.STATE_NORMAL,self.logic.get_colormap().alloc_color('light gray'))
        self.vbox_one.pack_start(self.logic,False)
        self.logic_grid=gtk.Button('Logic-grid')
        self.logic_grid.set_size_request(200,33)
        self.logic_grid.modify_bg(gtk.STATE_NORMAL,self.logic_grid.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.logic_grid,False)
        self.math=gtk.Button('Math')
        self.math.set_size_request(200,33)
        self.math.modify_bg(gtk.STATE_NORMAL,self.math.get_colormap().alloc_color('light gray'))
        self.vbox_one.pack_start(self.math,False)
        self.situation=gtk.Button('Situation')
        self.situation.set_size_request(200,33)
        self.vbox_one.pack_start(self.situation,False)
        self.situation.modify_bg(gtk.STATE_NORMAL,self.situation.get_colormap().alloc_color('black'))
        self.rebus=gtk.Button('Rebus')
        self.rebus.set_size_request(200,33)
        self.vbox_one.pack_start(self.rebus,False)
        self.rebus.modify_bg(gtk.STATE_NORMAL,self.rebus.get_colormap().alloc_color('light gray'))
        self.riddle=gtk.Button('Riddle')
        self.riddle.set_size_request(200,33)
        self.vbox_one.pack_start(self.riddle,False)
        self.riddle.modify_bg(gtk.STATE_NORMAL,self.riddle.get_colormap().alloc_color('black'))
        self.trick=gtk.Button('Trick')
        self.trick.set_size_request(200,33)
        self.trick.modify_bg(gtk.STATE_NORMAL,self.trick.get_colormap().alloc_color('light gray'))
        self.vbox_one.pack_start(self.trick,False)
        self.probability=gtk.Button('Probability')
        self.probability.set_size_request(200,33)
        self.probability.modify_bg(gtk.STATE_NORMAL,self.probability.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.probability,False)
        self.trivia=gtk.Button('Trivia')
        self.trivia.set_size_request(200,33)
        self.trivia.modify_bg(gtk.STATE_NORMAL,self.trivia.get_colormap().alloc_color('light gray'))
        self.vbox_one.pack_start(self.trivia,False)
        self.series=gtk.Button('Series')
        self.series.set_size_request(200,33)
        self.series.modify_bg(gtk.STATE_NORMAL,self.series.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.series,False)
        self.mystery=gtk.Button('Mystery')
        self.mystery.set_size_request(200,33)
        self.mystery.modify_bg(gtk.STATE_NORMAL,self.mystery.get_colormap().alloc_color('light gray'))
        self.vbox_one.pack_start(self.mystery,False)
        self.letter_equation=gtk.Button('Letter-equation')
        self.letter_equation.set_size_request(200,33)
        self.letter_equation.modify_bg(gtk.STATE_NORMAL,self.letter_equation.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.letter_equation,False)
        self.crypto=gtk.Button('Cryptography')
        self.crypto.set_size_request(200,33)
        self.crypto.modify_bg(gtk.STATE_NORMAL,self.crypto.get_colormap().alloc_color('light gray'))
        self.vbox_one.pack_start(self.crypto,False)
        self.science=gtk.Button('Science')
        self.science.set_size_request(200,33)
        self.science.modify_bg(gtk.STATE_NORMAL,self.science.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.science,False)
        self.back=gtk.Button('BACK')
        self.back.set_size_request(200,33)
        self.back.modify_bg(gtk.STATE_NORMAL,self.back.get_colormap().alloc_color('red'))
        self.vbox_one.pack_start(self.back,False)
    def motion(self,argv):
        """TODO: Docstring for motion.
        :returns: TODO

        """
        self.update()                          
        def action(self):
            """TODO: Docstring for action.
            :returns: TODO

             """
            if self.side:
                if self.wid_one<=2:
                    self.wid_two-=5
                self.vbox_two.set_size_request(self.wid_two,gtk.gdk.screen_height()-100)
                if self.wid_two<=0:
                    self.vbox_two.hide()
                    self.vbox_one.show()
                if self.wid_two<=2:
                    self.wid_one+=5
                    self.vbox_one.set_size_request(self.wid_one,gtk.gdk.screen_height()-100)
                    if self.wid_one>=200:
                        self.side=False
                        return False
                return True
            else:
                if self.wid_two<=2:
                    self.wid_one-=5
                self.vbox_one.set_size_request(self.wid_one,gtk.gdk.screen_height()-100)
                if self.wid_one<=0:
                    self.vbox_one.hide()
                    self.vbox_two.show()
                if self.wid_one<=2:
                    self.wid_two+=5
                    self.vbox_two.set_size_request(self.wid_two,gtk.gdk.screen_height()-100)
                    if self.wid_two>=200:
                        self.side=True
                        return False
                return True
        gobject.timeout_add(1,action,self)
    def question(self):
        self.text_view1=gtk.TextView()
        self.text_view1.modify_font(pango.FontDescription('monospace regular 13'))
        self.text_view1.set_wrap_mode(True)
        self.text_view1.set_editable(False)
        self.text_view1.set_left_margin(20)
        self.text_view2=gtk.TextView()
        self.text_view2.modify_font(pango.FontDescription('monospace regular 13'))
        self.text_view2.set_editable(False)
        self.text_view2.set_wrap_mode(True)
        self.text_view2.set_left_margin(20)
        self.text_buffer1=self.text_view1.get_buffer()
        self.text_buffer1.set_text(puzzle)
        self.view1.set_size_request(gtk.gdk.screen_width()-210,gtk.gdk.screen_height())
        self.view1.add(self.text_view1)
        self.view2.add(self.text_view2)
        self.vbox_three.pack_start(self.view1,True)
        self.vbox_three.pack_start(self.view2,False)
    def ans(self,etc):
        if answer!='':
            self.view2.show()
        self.text_buffer2=self.text_view2.get_buffer()
        self.view1.set_size_request(gtk.gdk.screen_width()-210,gtk.gdk.screen_height()/2)
        self.view2.set_size_request(gtk.gdk.screen_width()-210,gtk.gdk.screen_height()/2)
        self.text_buffer2.set_text(answer)
    def hint_field(self,etc):
        self.view2.show()
        self.text_buffer2=self.text_view2.get_buffer()
        self.view1.set_size_request(gtk.gdk.screen_width()-210,gtk.gdk.screen_height()/2)
        self.view2.set_size_request(gtk.gdk.screen_width()-210,gtk.gdk.screen_height()/2)
        self.text_buffer2.set_text(hint)

    def details(self):
        self.det_hori=gtk.HBox()
        self.det_hori.set_size_request(200,33)
        self.cat_lab=gtk.Label(category)
        self.cat_lab.modify_fg(gtk.STATE_NORMAL,self.cat_lab.get_colormap().alloc_color('dark blue'))
        self.diff_lab=gtk.Label('{ '+str(difficulty)+' }')
        self.det_hori.pack_start(self.cat_lab,False,False,13)
        self.det_hori.pack_start(self.diff_lab,False,True,0)
        self.cat_hori=gtk.HBox()
        self.cat_but=gtk.Button('Category')
        self.cat_but.connect('clicked',self.motion)
        self.back.connect('clicked',self.motion)
        self.cat_but.modify_bg(gtk.STATE_NORMAL,self.cat_but.get_colormap().alloc_color('light gray'))
        self.cat_but.set_size_request(200,33)
        self.cat_hori.pack_start(self.cat_but,True)
        self.ans_hori=gtk.HBox()
        self.ans_but=gtk.Button('Answer')
        self.ans_but.connect('clicked',self.ans)
        self.ans_but.modify_bg(gtk.STATE_NORMAL,self.ans_but.get_colormap().alloc_color('light gray'))
        self.ans_but.set_size_request(200,33)
        self.ans_hori.pack_start(self.ans_but,True)
        self.rand_hori=gtk.HBox()
        self.rand_but=gtk.Button('Next (Random)')
        self.rand_but.modify_bg(gtk.STATE_NORMAL,self.rand_but.get_colormap().alloc_color('dark gray'))
        self.rand_but.set_size_request(200,33)
        self.rand_hori.pack_start(self.rand_but,True)
        self.same_hori=gtk.HBox()
        self.same_but=gtk.Button('Next (Same)')
        self.same_but.modify_bg(gtk.STATE_NORMAL,self.same_but.get_colormap().alloc_color('dark gray'))
        self.same_but.set_size_request(200,33)
        self.same_hori.pack_start(self.same_but,True)
        self.hint_hori=gtk.HBox()
        self.hint_but=gtk.Button('Hint')
        self.hint_but.connect('clicked',self.hint_field)
        self.hint_but.modify_bg(gtk.STATE_NORMAL,self.hint_but.get_colormap().alloc_color('black'))
        self.hint_but.set_size_request(200,33)
        self.hint_hori.pack_start(self.hint_but,True)
        self.vbox_two.pack_start(self.det_hori,False)
        self.vbox_two.pack_start(self.cat_hori,False)
        self.vbox_two.pack_start(self.hint_hori,False)
        self.vbox_two.pack_start(self.ans_hori,False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(self.rand_hori,False)
        self.vbox_two.pack_start(self.same_hori,False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(gtk.HSeparator(),False)
        self.vbox_two.pack_start(self.loader_cont,False)       
    def update(self):
        """Update difficulty color label"""
        global hint
        if hint == '':
            hint='[Hint]:\n\n:'+hint
            self.hint_hori.hide()
        if difficulty<0.90:
            self.diff_lab.modify_fg(gtk.STATE_NORMAL,self.diff_lab.get_colormap().alloc_color('green'))
        elif difficulty<1.70:
            self.diff_lab.modify_fg(gtk.STATE_NORMAL,self.diff_lab.get_colormap().alloc_color('orange'))
        else:
            self.diff_lab.modify_fg(gtk.STATE_NORMAL,self.diff_lab.get_colormap().alloc_color('red'))
    def next_same(self,etc):
        store={'LOGIC':'Logic','LOGIC-GRID':'Logic-Grid','CRYPTOGRAPHY':'Cryptography','SCIENCE':'Science','LETTER-EQUATION':'Letter-Equations','RIDDLE':'Riddle','TRICK':'Trick','RIBUS':'Ribus','LANGUAGE':'Language','MYSTERY':'Mystery','SITUATION':'Situation','TRIVIA':'Trivia','PROBABILITY':'Probability','SERIES':'Series','MATH':'Math'}
        self.same_but.connect('clicked',self.opn,self.default_add+'/teaser.php?similar='+store[category])
    def action(self):
        self.rand_but.connect('clicked',self.opn,self.default_add+'/teaser.php?rand=1')
        self.same_but.connect('clicked',self.next_same)
        self.crypto.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Cryptography')
        self.science.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Science')
        self.logic.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Logic')
        self.letter_equation.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Letter-Equations')
        self.rebus.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Rebus')
        self.riddle.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Riddle')
        self.trick.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Trick')
        self.language.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Language')
        self.logic_grid.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Logic-Grid')
        self.math.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Math')
        self.mystery.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Mystery')
        self.situation.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Situation')
        self.trivia.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Trivia')
        self.probability.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Probability')
        self.series.connect('clicked',self.opn,self.default_add+'/teaser.php?similar=Series')
            
if __name__=='__main__':
    x=view()
