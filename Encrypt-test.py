

from tkinter import*

mainWindow=Tk()

mainWindow.title("Encryption/Decryption Program")

mainWindow.geometry("500x500")

frame1=LabelFrame(mainWindow,text="Encryption Mod",padx=10, pady=10)
frame1.grid(row=5, column=5, rowspan=10, columnspan=10)

frame2=LabelFrame(mainWindow,text="Decryption Mod",padx=10, pady=10)
frame2.grid(row=5, column=55, rowspan=10, columnspan=10)

#frame3=LabelFrame(mainWindow,padx=20,pady=20)
#frame3.grid(row=150, column=30, rowspan=5, columnspan=5)

ename1=Label(frame1,text="Encrypt:")
ename1.grid(row=8, column=10)
ename2=Label(frame2,text="Decrypt:")
ename2.grid(row=8, column=58)

enter1=Entry(frame1, width=25)
enter1.grid(row=8, column=15)
enter2=Entry(frame2, width=25)
enter2.grid(row=8, column=63)

ebutton=Button(frame1, text="Encrypt")
ebutton.grid(row=25, column=15)
dbutton=Button(frame2, text="Decrypt")
dbutton.grid(row=25, column=63)
#rbutton=Button(frame3, text="Reset")
#rbutton.grid(row=53, column=33)



mainWindow.mainloop()
