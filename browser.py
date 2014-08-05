#!/usr/bin/env python
 
import gtk
import webkit
import gobject
 
gobject.threads_init()
win = gtk.Window()
bro = webkit.WebView()
bro.open("file:///home/vfuentes/Escritorio/Prototipos/Proyecto%20SIGEM/index.html")
win.add(bro)
win.show_all()
 
gtk.main()
