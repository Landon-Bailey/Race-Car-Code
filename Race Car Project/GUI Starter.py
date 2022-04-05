from tkinter import *
main_window = Tk()

#Labels
Label(main_window, text = "Row 0 - Column 0").grid(row = 0, column = 0)

Label(main_window, text = "Row 1 - Column 0").grid(row = 1, column = 0)


#Text Input 

Entry(main_window, width = 50, borderwidth = 5).grid(row = 0, column = 1)

Entry(main_window, width = 50, borderwidth = 5).grid(row = 1, column = 1)

def on_click():
  print("Button Pressed")

#Buttons

Button(main_window, text = "Reset", command = on_click).grid(row = 3, column = 0)



main_window.mainloop()