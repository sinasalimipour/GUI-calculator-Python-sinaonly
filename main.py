from tkinter import *


root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35,borderwidth=5).grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):

    e.insert(0,number)
#numbers

#row3
button_1= Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1)).grid(row=3,column=0)
button_2= Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2)).grid(row=3,column=1)
button_3= Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3)).grid(row=3,column=2)
#row3 end

#row2
button_4= Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4)).grid(row=2,column=0)
button_5= Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5)).grid(row=2,column=1)
button_6= Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6)).grid(row=2,column=2)
#row2 end

#row1
button_7= Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7)).grid(row=1,column=0)
button_8= Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8)).grid(row=1,column=1)
button_9= Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9)).grid(row=1,column=2)
#row1 end

#row4
button_0= Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0)).grid(row=4,column=0)
#numbers end



#op
button_clear= Button(root,text="Clear",padx=79,pady=20,command=lambda: button_click()).grid(row=4,column=1,columnspan=3)
#row4 end

button_add= Button(root,text="+",padx=39,pady=20,command=lambda: button_click()).grid(row=5,column=0)
button_equal= Button(root,text="=",padx=91,pady=20,command=lambda: button_click()).grid(row=5,column=1,columnspan=3)
#op end





root.mainloop()