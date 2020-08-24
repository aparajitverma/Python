import tkinter
root= tkinter.Tk()
root.geometry("500x300+200+100")
root.title("CMS")
root.minsize(200,200)
root.maxsize(600,400)
btn1=tkinter.Button(root,text="Btn1",width=15,height=3,bg="red",fg='yellow',font=("Times New Roman",16,"bold"),bd=10)#bd means border width
btn1.grid(row=3,column=3)

btn2=tkinter.Button(root,text="Btn2")
btn2["bg"]="green"
btn2.config(fg="yellow")
btn2.grid(row=0,column=0)



























root.mainloop()
