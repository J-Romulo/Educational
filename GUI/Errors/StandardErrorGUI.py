import tkinter

class StandardErrorGUI:
    def __init__(self, msg, master=None):
        self.master = master
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.messageLabel = tkinter.Label(self.mainWidget, text="{}".format(msg))
        self.messageLabel.pack()

        self.button = tkinter.Button(self.mainWidget, text="Ok")
        self.button.pack()
        self.button["command"] = self.destroyFrame

    def destroyFrame(self):
        self.master.destroy()