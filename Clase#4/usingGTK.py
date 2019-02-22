import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


window  = Gtk.Window()
button1 = Gtk.Button(label="Ok")
button2 = Gtk.Button(label="No")

window.add(button1)

window.connect("delete-event", Gtk.main_quit)

window.show_all()
Gtk.main()
