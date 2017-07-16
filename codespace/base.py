import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject

class ProjectWindow(Gtk.Window):
    def __init__(self, projectID):
        Gtk.Window.__init__(self)

        label = Gtk.Label(projectID)
        self.add(label)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

class SelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_border_width(10)
        self.set_size_request(850, 300)
        self.set_title("Codespace - Projects")

        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
        stack.set_transition_duration(1000)
        
        createItems = self.build_create_items()
        stack.add_titled(createItems, "Start a new project", "Create")

        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "Recent Projects")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, False, True, 0)
        vbox.pack_start(stack, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def build_create_items(self):
        box = Gtk.Box()

        entry = Gtk.Entry()
        box.pack_start(entry, True, True, 0)


        return box


class CodeSpace(object):
    def __init__(self, config):
        print(config)

    def run(self):
        mw = SelectionWindow()
        Gtk.main()
