import pygtk
import gtk
class view():

    """"""

    def __init__(self):
        """TODO: to be defined1. """
        self.main_window=gtk.Window()
        self.main_window.connect('destroy',lambda x:gtk.main_quit())
        self.main_window.set_default_size(gtk.gdk.screen_width()-100,gtk.gdk.screen_height()-100)
        self.main_hbox=gtk.HBox()
#Three vertical boxes
        self.vbox_one=gtk.VBox()
        self.vbox_two=gtk.VBox()
        self.vbox_three=gtk.VBox()
#pack three boxes in window into main Horizontal box
        self.main_window.add(self.main_hbox)
        self.main_hbox.pack_start(self.vbox_one,False)
        self.main_hbox.pack_start(self.vbox_two,False)
        self.main_hbox.pack_start(self.vbox_three,False)

        self.main_window.show_all()
        gtk.main()

y=view()
