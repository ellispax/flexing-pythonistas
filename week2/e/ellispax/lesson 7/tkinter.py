import tkinter

class Application(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.label = tkinter.Label(self, text="Hello, world!")
        self.label.pack()

        self.button = tkinter.Button(self, text="Quit", command=self.quit)
        self.button.pack()

def main():
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()