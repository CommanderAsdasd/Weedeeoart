# -*- coding: utf-8 -*-
# /venv/Scripts/Python.exe
import recorder
from tkinter import filedialog
from tkinter import *

class VideoProcess():

    def __init__(self):
        self.Clip = None
        # self.clipPath = None


    def main(self):
        write_data = time.strftime("%I%M%S")
        self.Clip = MpEditor.VideoFileClip(self.clipPath)
        self.Clip = self.Clip.fl_image(self.image_adaptor)
        out_string = str(self.clipPath).rsplit(".")[0] + "__CAS-{}".format(write_data) + ".mp4"
        print(out_string)
        self.Clip.write_videofile(out_string, codec='libx264', audio_codec='aac')



class GUI(VideoProcess):
    """make the GUI version of this command that is run if no options are
    provided on the command line"""
    def __init__(self):
        self.lowerBound = None
        self.lowerBound = None
        VideoProcess.__init__(self)
        self.main_window()

    def Entry1_Callback(self, event):
        self.insert_bound1.selection_range(0, END)

    def Entry2_Callback(self, event):
        self.insert_bound2.selection_range(0, END)



    def button_go_callback(self):

        # try:
        #     self.lowerBound = int(min(self.insert_bound1.get(), self.insert_bound2.get()))
        #     self.upperBound = int(max(self.insert_bound1.get(), self.insert_bound2.get()))
        # except ValueError:
        #     print('Non integer range input, use default 4 and 5')
        #     self.insert_bound1.delete(0, 'end')
        #     self.insert_bound1.insert(END, '4')
        #     self.insert_bound2.delete(0, 'end')
        #     self.insert_bound2.insert(END, '5')
        #     self.lowerBound = int(min(self.insert_bound1.get(), self.insert_bound2.get()))
        #     self.upperBound = int(max(self.insert_bound1.get(), self.insert_bound2.get()))
        # self.clipPath = self.entry.get()
        # self.main()


    def button_browse_callback(self):
        """ What to do when the Browse button is pressed """
        filename = tkFileDialog.askopenfilename()
        self.entry.delete(0, END)
        self.entry.insert(0, filename)

    def main_window(self):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        statusText = StringVar(root)
        statusText.set("Working")

        label = Label(root, text="Path for audio: ")
        label.pack()
        self.insert_iterations = Entry(root, width=10)
        self.insert_length = Entry(root, width=10)
        self.insert_iterations.insert(END, 'lower bound')
        self.insert_length.insert(END, 'higher bound')
        self.insert_iterations.bind("<FocusIn>", self.Entry1_Callback)
        self.insert_length.bind("<FocusIn>", self.Entry2_Callback)
        self.entry = Entry(root, width=50)
        self.entry.pack()
        separator = Frame(root, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        button_go = Button(root,
                        text="Record",
                        command=self.button_go_callback)
        button_browse = Button(root,
                            text="Browse",
                            command=self.button_browse_callback)
        button_exit = Button(root,
                            text="Exit",
                            command=sys.exit)
        self.insert_iterations.pack()
        self.insert_length.pack()
        button_go.pack()
        button_browse.pack()
        button_exit.pack()

        separator = Frame(root, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        self.message = Label(root, textvariable=statusText)
        self.message.pack()
        mainloop()

if __name__ == "__main__":
    RescalerInstance = GUI()