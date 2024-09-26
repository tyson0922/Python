from tkinter import *
from tkinter.filedialog import *

#함수 선언 부분
window = Tk()
window.geometry("400x400")

label1 = Label(window, text = "선택된 파일 이름")
label1.pack()

saveFp = asksaveasfile(parent= window, mode= "w",
                       defaultextension=".jpg",
                       filetypes=(("JPG 파일", "*.jpg;*.jpeg"),
                                  ("모든 파일", "*.*")))

label1.configure(text = saveFp)
saveFp.close()

window.mainloop()