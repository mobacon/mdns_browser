from zeroconf import ServiceBrowser, Zeroconf
from Tkinter import *
from ttk import *


class MainApplication(object):

    def __init__(self):

        self._root = Tk() # create a top-level window

        self._master = Frame(self._root, name='master') # create Frame in "root"
        self._master.pack(fill=BOTH) # fill both sides of the parent

        self._root.title('Scanning for MDNS devices with HTTP service') # title for top-level window
        # quit if the window is deleted
        self._root.protocol("WM_DELETE_WINDOW", self._master.quit)
        
        self._listbox = Listbox(self._master, width=50, height=10)
        self._listbox.pack()

    def mainloop(self):
        self._master.mainloop()

    def get_listbox(self):
        return self._listbox


class MyListener(object):

    def __init__(self, listbox):
        self._list = listbox
        self._services = {}
        
    def removeService(self, zeroconf, type, name):
        print("Service %s removed" % (name,))
        try:
            self._services.pop(name, None)
            self.updateList()
        except KeyError:
            pass
            
    def addService(self, zeroconf, type, name):
        info = zeroconf.getServiceInfo(type, name)
        print("Service %s added, service info: %s" % (name, info))
        
        self._services[name] = info
        self.updateList()

    def updateList(self):
        self._list.delete(0, END)
        sorted_names = sorted(self._services.iterkeys())
        for name in sorted_names:
            s = "%s %s" % (name[0:name.rfind("._http._tcp.local.")], self._address(self._services[name]))
            self._list.insert(END, s)

    def _address(self, info):
        add = []
        for byte in info.getAddress():
            add.append(ord(byte))
        add_str = "%d.%d.%d.%d:%d" % (add[0], add[1], add[2], add[3], info.getPort())
        return add_str
            
def main():
    main = MainApplication()
    zeroconf = Zeroconf()
    listener = MyListener(main.get_listbox())
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    try:
        main.mainloop()
    finally:
        zeroconf.close()

        
# start the app
if __name__ == "__main__":
    main()

    
    