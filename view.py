import gobject
import pango
import gtk
import thread
from data import data
from puzzle import myclass as pz
category,difficulty,puzzle,answer,hint='','','','','',
def load():
    global category,difficulty,puzzle,answer,hint
    pop=pz()
    file=open('teaser','r')
    pop.feed(file.read())
    category=pop.category
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
class view():
    def __init__(self):
        """TODO: to be defined1. """
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
#spinner
        self.spin_cont=gtk.VBox()
        self.spin_cont.set_size_request(100,100)
        self.spin=gtk.Spinner()
        self.spin.set_size_request(50,50)
        self.spin_cont.pack_start(self.spin,True,False,0)
        self.view1.add(self.spin_cont)
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
        self.details()
        
        self.question()
        self.main_window.show_all()
        self.update()
        self.view2.hide()
        self.action()
        self.vbox_one.hide()
        self.spin_cont.hide()
        gtk.main()
    def opn(self,etc,url):
        dt=data()
        thread.start_new_thread(dt.get_data,(url,))
        thread.start_new_thread(self.spinning,('',))
        def spin_stop(self):
            if dt.local!=0:
                self.spin.stop()
                #self.spin_cont.hide()
                return False
            return True
        gobject.timeout_add(1,spin_stop,self)
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
    def spinning(self,etc):
        self.spin_cont.show()
        self.spin.start()
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
        self.diff_lab=gtk.Label('{  '+str(difficulty)+'  }')
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
        self.rand_but=gtk.Button('Next Random')
        self.rand_but.modify_bg(gtk.STATE_NORMAL,self.rand_but.get_colormap().alloc_color('dark gray'))
        self.rand_but.set_size_request(200,33)
        self.rand_hori.pack_start(self.rand_but,True)
        self.same_hori=gtk.HBox()
        self.same_but=gtk.Button('Next Same')
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
    def action(self):
        if self.rand_but.connect('clicked',self.opn,self.default_add+'/teaser.php?rand=1'):
            print "fine"
        else:
            print "not Fine"
            
if __name__=='__main__':
    x=view()
