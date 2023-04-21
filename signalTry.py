import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib
import time

mainloop = None
class Counter(dbus.service.Object):
    def __init__(self, bus):
        self.object_path = '/com/example/TestService/counter'
        self.c = 0
        dbus.service.Object.__init__(self, bus, self.object_path)
    def increment(self):
        self.c = self.c + 1
        print(self.c)
    @dbus.service.signal('com.example.TestService')
    def CounterSignal(self, counter):
        # nothing else to do so...
        pass
    @dbus.service.method('com.example.TestService')
    def emitCounterSignal(self):
        self.CounterSignal(self.c)

if __name__=='__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    name = dbus.service.BusName('com.example.TestService', bus)
    counter = Counter(bus)
    mainloop = GLib.MainLoop()
    print("Running example signal")
    mainloop.run()