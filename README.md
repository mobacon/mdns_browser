mdns_browser
============

GUI for MDNS discovering of HTTP services in a LAN.

It is a python GUI basing on tkinter and ttk elements.

The code bases on the example code of the zeroconf project:
https://github.com/jstasiak/python-zeroconf


Installation
------------

Open a commandline, go into this folder and enter

```
python setup.py install
```

Afterwards you can start the program with typing 

```
mdns_browser
```

If you want to install it in a virtualenv do not forget to set the TCL_LIBRARY environment variable like described here:
http://stackoverflow.com/questions/15884075/tkinter-in-a-virtualenv
