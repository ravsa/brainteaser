import pygtk
import gobject

import gtk
category='logic'
class view():

    """"""
    def __init__(self):
        """TODO: to be defined1. """
        self.main_window=gtk.Window()
        self.main_window.connect('destroy',lambda x:gtk.main_quit())
        self.main_window.set_default_size(gtk.gdk.screen_width()-100,gtk.gdk.screen_height()-100)
        self.main_hbox=gtk.HBox()
        self.side=True
#Three vertical boxes
        self.vbox_one=gtk.VBox()
        self.vbox_two=gtk.VBox()
        self.vbox_three=gtk.VBox()
#pack three boxes in window into main Horizontal box
        self.wid_one=0
        self.wid_two=200
        self.main_window.add(self.main_hbox)
        self.main_hbox.pack_start(self.vbox_one,False)
        self.main_hbox.pack_start(self.vbox_two,False)
        self.vbox_two.set_size_request(self.wid_two,gtk.gdk.screen_height()-100)
        self.vbox_one.set_size_request(self.wid_one,gtk.gdk.screen_height()-100)
        self.main_hbox.pack_start(self.vbox_three,True)
        self.sidebar()
        self.details()
        self.question()
        self.main_window.show_all()
        self.vbox_one.hide()
        gtk.main()
    def sidebar(self):
        self.language=gtk.Button('Language')
        self.language.set_size_request(200,33)
        self.language.modify_bg(gtk.STATE_NORMAL,self.language.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.language,False)
        self.logic=gtk.Button('Logic')
        self.logic.set_size_request(200,33)
        self.logic.modify_bg(gtk.STATE_NORMAL,self.logic.get_colormap().alloc_color('dark gray'))
        self.vbox_one.pack_start(self.logic,False)
        self.logic_grid=gtk.Button('Logic-grid')
        self.logic_grid.set_size_request(200,33)
        self.logic.modify_bg(gtk.STATE_NORMAL,self.logic.get_colormap().alloc_color('dark gray'))
        self.logic_grid.modify_bg(gtk.STATE_NORMAL,self.logic_grid.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.logic_grid,False)
        self.math=gtk.Button('Math')
        self.math.set_size_request(200,33)
        self.math.modify_bg(gtk.STATE_NORMAL,self.math.get_colormap().alloc_color('dark gray'))
        self.vbox_one.pack_start(self.math,False)
        self.situation=gtk.Button('Situation')
        self.situation.set_size_request(200,33)
        self.vbox_one.pack_start(self.situation,False)
        self.situation.modify_bg(gtk.STATE_NORMAL,self.situation.get_colormap().alloc_color('black'))
        self.rebus=gtk.Button('Rebus')
        self.rebus.set_size_request(200,33)
        self.vbox_one.pack_start(self.rebus,False)
        self.rebus.modify_bg(gtk.STATE_NORMAL,self.rebus.get_colormap().alloc_color('dark gray'))
        self.riddle=gtk.Button('Riddle')
        self.riddle.set_size_request(200,33)
        self.vbox_one.pack_start(self.riddle,False)
        self.riddle.modify_bg(gtk.STATE_NORMAL,self.riddle.get_colormap().alloc_color('black'))
        self.trick=gtk.Button('Trick')
        self.trick.set_size_request(200,33)
        self.trick.modify_bg(gtk.STATE_NORMAL,self.trick.get_colormap().alloc_color('dark gray'))
        self.vbox_one.pack_start(self.trick,False)
        self.probability=gtk.Button('Probability')
        self.probability.set_size_request(200,33)
        self.probability.modify_bg(gtk.STATE_NORMAL,self.probability.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.probability,False)
        self.trivia=gtk.Button('Trivia')
        self.trivia.set_size_request(200,33)
        self.trivia.modify_bg(gtk.STATE_NORMAL,self.trivia.get_colormap().alloc_color('dark gray'))
        self.vbox_one.pack_start(self.trivia,False)
        self.series=gtk.Button('Series')
        self.series.set_size_request(200,33)
        self.series.modify_bg(gtk.STATE_NORMAL,self.series.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.series,False)
        self.mystery=gtk.Button('Mystery')
        self.mystery.set_size_request(200,33)
        self.mystery.modify_bg(gtk.STATE_NORMAL,self.mystery.get_colormap().alloc_color('dark gray'))
        self.vbox_one.pack_start(self.mystery,False)
        self.letter_equation=gtk.Button('Letter-equation')
        self.letter_equation.set_size_request(200,33)
        self.letter_equation.modify_bg(gtk.STATE_NORMAL,self.letter_equation.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.letter_equation,False)
        self.crypto=gtk.Button('Cryptography')
        self.crypto.set_size_request(200,33)
        self.crypto.modify_bg(gtk.STATE_NORMAL,self.crypto.get_colormap().alloc_color('dark gray'))
        self.vbox_one.pack_start(self.crypto,False)
        self.science=gtk.Button('Science')
        self.science.set_size_request(200,33)
        self.science.modify_bg(gtk.STATE_NORMAL,self.science.get_colormap().alloc_color('black'))
        self.vbox_one.pack_start(self.science,False)
        self.back=gtk.Button('BACK')
        self.back.set_size_request(200,33)
        self.back.modify_bg(gtk.STATE_NORMAL,self.back.get_colormap().alloc_color('dark red'))
        self.vbox_one.pack_start(self.back,False)
    def motion(self,argv):
        """TODO: Docstring for motion.
        :returns: TODO

        """
                                  
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
                        return False
                return True
        gobject.timeout_add(1,action,self)
    def question(self):
        self.view1=gtk.ScrolledWindow()
        self.view=gtk.TextView()
        self.buffer=self.view.get_buffer()
        file=open('puzzel.py','r')
        self.buffer.set_text(file.read())
        self.view1.add(self.view)
        self.vbox_three.pack_start(self.view1,True)
        self.view1.set_border_width(2)
        self.view2=gtk.ScrolledWindow()
        self.view2.set_border_width(2)
        self.vbox_three.pack_start(self.view2,False)
    def details(self):
        self.cat_hori=gtk.HBox()
        self.cat_lab=gtk.Button('Category')
        self.cat_lab.connect('clicked',self.motion)
        self.cat_lab.set_size_request(200,33)
        self.cat_hori.pack_start(self.cat_lab,True)
        self.vbox_two.pack_start(self.cat_hori,False)



iiy=view()
