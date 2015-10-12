import pygtk
import gtk
class view():

    """"""

    def __init__(self):
        """TODO: to be defined1. """
        self.main_window=gtk.Window()
        self.main_window.connect('destroy',lambda x:gtk.main_quit())
        self.main_window.set_default_size(gtk.gdk.screen_width()-100,gtk.gdk.screen_height()-100)
        self.main_window.show_all()
        gtk.main()



y=view()
