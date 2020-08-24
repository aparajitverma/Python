import time
from tkinter import *
#def btnSubmit_Click():
 #   print("i am clicked")
#def btnHello_Click():
  #  print('button hello is clicked')
def moveWindow():
    global count
    if count==1000:
        count=0
    else:
        count+=10
    root.geometry("200x200+%d+100" % count)
    time.sleep(0.1)
    root.after(100,moveWindow)

root=Tk()
root["bg"]="red"
count=0
moveWindow()

#btnSubmit=Button(master=root,text="Submit",command=btnSubmit_Click)
#btnSubmit.pack()

#btnHello=Button(master=root,text="hello",command=btnHello_Click)
#btnHello.pack()







root.mainloop()