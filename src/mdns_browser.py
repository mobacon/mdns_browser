from zeroconf import ServiceBrowser, Zeroconf
from Tkinter import *
import ttk
import socket
import logo 

class MainApplication(object):
    """Builds up and handles the Tkinter application frame."""
    
    def __init__(self):
        """Constructor."""
        self._root = Tk() # create a top-level window
        
        # Create logo.
        logo.constructor(self._root)
        
        self._root.title('Scanning for MDNS devices with HTTP service') # title for top-level window       
        self._tree = ttk.Treeview(self._root, height="10", show="headings", padding=3, selectmode="browse")
        
        # Init scrollbars
        ysb = ttk.Scrollbar(orient='vertical', command=self._tree.yview)
        xsb = ttk.Scrollbar(orient='horizontal', command=self._tree.xview)
        self._tree.configure(yscroll=ysb.set, xscroll=xsb.set)

        # Prepare tree columns.
        self._tree["columns"]=("A","B","C","D")
        self._tree.column("A", width=300)
        self._tree.column("B", width=200)
        self._tree.column("C", width=100)
        self._tree.column("D", width=30)
        self._tree.heading("A", text="Service name", anchor=W)
        self._tree.heading("B", text="Hostname (.local)", anchor=W)
        self._tree.heading("C", text="IP-Address", anchor=W)
        self._tree.heading("D", text="Port", anchor=W)

        # Prepare right click action
        self._tree.bind("<Button-3>", self._popup)

        # Prepare context menu.
        self._context_menu = Menu(self._root, tearoff=0)
        self._context_menu.add_command(label="IP address -> clipboard", 
                                       command=self._copy_ip_address)
        self._context_menu.add_command(label="Hostname -> clipboard", 
                                       command=self._copy_hostname)
        
        self._tree.grid(row=0, column=0, sticky='nsew')
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')

    def _copy_ip_address(self):
        """Copies the IP address of the current in tree selected device to 
           clipboard."""
        self._root.clipboard_clear()
        item_id = self._tree.selection()
        if item_id:
            ip_address = self._tree.item(item_id[0])['values'][2]
            self._root.clipboard_append(ip_address)

    def _copy_hostname(self):
        """Copies the hostname of the current in tree selected device to 
           clipboard."""
        self._root.clipboard_clear()
        item_id = self._tree.selection()
        if item_id:
            hostname = "%s.local" % self._tree.item(item_id[0])['values'][1]
            self._root.clipboard_append(hostname)
        
    def _popup(self, event):
        """Select row under mouse on right mouse click."""      
        iid = self._tree.identify_row(event.y)
        if iid:
            # mouse pointer over item
            self._tree.selection_set(iid)
            self._context_menu.post(event.x_root, event.y_root)           
    
    def mainloop(self):
        """Entry tkinter mainloop."""
        self._root.mainloop()

    def get_control(self):
        """Get access to tree control."""
        return self._tree

    def __del__(self):
        """Called on destruction of the frame."""
        logo.destructor()

        

class MyListener(object):
    """Thread class for fetching MDNS events"""
    def __init__(self, control):
        """Constructor. Takes frames tree control for inserting/removing items."""
        self._control = control
        self._services = {}
        
    def removeService(self, zeroconf, type, name):
        """Called when service is gone."""
        print("Service %s removed" % (name,))
        try:
            self._services.pop(name, None)
            self._updateList()
        except KeyError:
            pass
            
    def addService(self, zeroconf, type, name):
        """Called when service is added."""
        info = zeroconf.getServiceInfo(type, name)
        print("Service %s added, service info: %s" % (name, info))      
        self._services[name] = info
        self._updateList()

    def _updateList(self):
        """Update the frames tree control with items currently stored in 
           _services dictionary."""
        for i in self._control.get_children():
            self._control.delete(i)
        sorted_names = sorted(self._services.iterkeys())
        for name in sorted_names:
            info = self._services[name]
            self._control.insert("" , 'end', text=name, 
                values=(name[0:name.rfind("._http._tcp.local.")], 
                        info.getServer()[0:info.getServer().rfind(".local")],
                        str(socket.inet_ntoa(info.getAddress())),
                        info.getPort()))

           
def main():
    """Main entry point."""
    main = MainApplication()
    zeroconf = Zeroconf()
    listener = MyListener(main.get_control())
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    try:
        main.mainloop()
    finally:
        zeroconf.close()

        
# start the app
if __name__ == "__main__":
    main()

    
    