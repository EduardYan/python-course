"""
A UI with tkinter module
"""
from tkinter import Tk,Label,Entry,LabelFrame, Button

class UI():
    # this is a calculator
    def __init__(self, window):
        self.wind = window
        self.wind.title('Calculator')

        # creating a frame conteiner
        frame = LabelFrame(self.wind ,text='Calculator')
        frame.grid(row=0,column=0)

        entry = Entry(frame)
        entry.grid(row=0,column=1, padx=10, pady=10)

        # ----- Buttons ------
        Button(frame, text='+').grid(row=1,column=0)




if __name__ == '__main__':
    window = Tk()
    # pasando la ventana al clase UI
    UI(window)
    # ejecutando la ventana
    window.mainloop()
