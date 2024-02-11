from tkinter import *


class Convertor:

     def __init__(self):

         #  Set up GUI Frame
         self.temp_frame = Frame()
         self.temp_frame.grid()

         self.temp_heading = Label(self.temp_frame,
                                   text="Temperature Convertor",
                                   font=("Arial", "16", "bold")
                                   )
         self.temp_heading.grid(row=0)

         intstructions = "Please enter a temperatre below and " \
                         "then press one of the butttons to convert " \
                         "it from centigrade to Fahrenheit."
         self.temp_instructions = Label(self.temp_frame,
                                        text=intstructions,
                                        wrap=250, width=40,
                                        justify="left")

         self.temp_instructions.grid(row=1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    Convertor()
    root.mainloop()