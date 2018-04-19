from Weedeeo import *
import preset
from tkinter import filedialog
from tkinter import *


class GUI(Weedeeo):
    """make the GUI version of this command that is run if no options are
    provided on the command line"""
    def __init__(self):
        self.lowerBound = None
        self.lowerBound = None
        self.main_window()

    def times_entry_Callback(self, event):
        self.times_entry.selection_range(0, END)

    def button_go_callback(self):
        try:
            times = int(self.times_entry.get())
        #     self.iterations = int(min(self.insert_bound1.get(), self.insert_bound2.get()))
        #     self.upperBound = int(max(self.insert_bound1.get(), self.insert_bound2.get()))
        except ValueError:
            times = 1
        #     print('Non integer times count, default 1')
        #     self.insert_bound1.delete(0, 'end')
        #     self.insert_bound1.insert(END, '4')
        #     self.insert_bound2.delete(0, 'end')
        #     self.insert_bound2.insert(END, '5')
        #     self.lowerBound = int(min(self.insert_bound1.get(), self.insert_bound2.get()))
        #     self.upperBound = int(max(self.insert_bound1.get(), self.insert_bound2.get()))
        self.clipPath = self.entry.get()
        
        # try:
            # audio_preset(editor1)
        preset.preset_manager(self.clipPath, times=times)
        # except Exception as e:
        #     pass
        


    def button_browse_callback(self):
        """ What to do when the Browse button is pressed """
        filename = filedialog.askopenfilename()
        self.entry.delete(0, END)
        self.entry.insert(0, filename)

    def main_window(self):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        statusText = StringVar(root)
        statusText.set("Working")

        label = Label(root, text="Video file: ")
        label.pack()
        self.times_entry = Entry(root, width=10)
        self.times_entry.bind("<FocusIn>", self.times_entry_Callback)
        self.times_entry.insert(END, 'iterations')
        self.entry = Entry(root, width=50)
        self.entry.pack()
        separator = Frame(root, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        button_go = Button(root,
                        text="Go",
                        command=self.button_go_callback)
        button_browse = Button(root,
                            text="Browse",
                            command=self.button_browse_callback)
        button_exit = Button(root,
                            text="Exit",
                            command=sys.exit)
        self.times_entry.pack()
        # self.insert_bound2.pack()
        button_go.pack()
        button_browse.pack()
        button_exit.pack()

        separator = Frame(root, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        self.message = Label(root, textvariable=statusText)
        self.message.pack()
        mainloop()

if __name__ == "__main__":
    WeedeeoGui = GUI()