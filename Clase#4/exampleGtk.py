import gi
gi.require_version('Gtk', '3.0')                # Esta libreria hay que bajarla mediante el buscador de pycharm
from gi.repository import Gtk

class MyWindow(Gtk.Window):                     # Defino mi clase MyWindow

    def __init__(self):                         # Defino el metodo constructor de mi clase mediante init

        Gtk.Window.__init__(self, title="Hello World")  # Llamo al metodo constructor de la clase Gtk (Herencia)

        self.button = Gtk.Button(label="Click Here")    # Utilizo los metodos de mi libreria Gtk

        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

"""Defino el evento que ocurrue cuando presiono el boton como parte de mi clase"""

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()