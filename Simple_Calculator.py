#Importing Everything From The tkinter Module 
from tkinter import *

#Creating a Basic Window For the Calculator 
win =Tk()
win.geometry ("450x750") # for the size of Window 

win.title("Simple Calculator") #Title of the Calculator
win.maxsize(450,750) # Maxsixe of the Window 
win.minsize(450,750)# Minimum size of the window




# Defining the Function for the Calculator To operates operation 
def click(event): 

    #Global Expression
    global scvalue 
    text = event.widget.cget("text") #To Get the actual value from the widget 
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())  


            #Defining the errors while operating 

            except Exception as e:
                print(e)
                value = "Error"

                
        scvalue.set(value)   
        screen.update() 

    elif text == "C": # For Clearing the screen 
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text )
        screen.update()                         #Updates the screen 





# Creating A Basic Screen for the Calculator 

scvalue = StringVar() 
scvalue.set("")
screen = Entry (win, textvariable = scvalue , font = " lucida 40 bold", relief = SUNKEN)
screen.pack(pady = 15, fill =  X, ipadx = 10 , padx = 10 )



#Creating the Frame for Buttons in First Row 
frame1 =Frame (win, bg = "grey")
frame1.pack()

#Buttons in the First Row 

button9 = Button (frame1, text = "9", font = "Lucida 35 bold")
button9.pack(side = LEFT,padx= 18,pady = 18)                          
button9.bind("<Button-1>", click)                                        # Binding event with the Button 
button8 = Button (frame1, text = "8", font = "Lucida 35 bold")
button8.pack(side = LEFT,padx= 18,pady = 18 )
button8.bind("<Button-1>", click)                                       # Binding event with the Button 
button7 = Button (frame1, text = "7", font = "Lucida 35 bold")
button7.pack(side = LEFT,padx= 18, pady = 18)
button7.bind("<Button-1>", click)                                          # Binding event with the Button 
button1 = Button (frame1, text = "-", font = "Lucida 35 bold")
button1.pack(side = LEFT,padx= 18, pady = 18,ipadx= 0)
button1.bind("<Button-1>", click)



#creating the Frames  fro the button in second Row 
frame2 = Frame (win, bg = "grey")
frame2.pack()

#Buttons in the Second Row 
button6 = Button (frame2, text = "6", font = "Lucida 35 bold")
button6.pack(side = LEFT,padx= 16, pady = 18)
button6.bind("<Button-1>", click)                                           # Binding event with the Button 
button5 = Button (frame2, text = "5", font = "Lucida 35 bold")
button5.pack(side = LEFT,padx= 17, pady = 18)
button5.bind("<Button-1>", click)                                             # Binding event with the Button 
button4 = Button (frame2, text = "4", font = "Lucida 35 bold")
button4.pack(side = LEFT,padx= 16, pady = 16)
button4.bind("<Button-1>", click)                                            # Binding event with the Button 
button3 = Button(frame2, text = "+", font = "lucida 35 bold")
button3.pack(side = LEFT , padx= 17 , pady = 18)
button3.bind("<Button-1>", click)                                               # Binding event with the Button 




#Creating the Frame for third Row
frame3 = Frame(win,bg = "grey")
frame3.pack()

# Buttons in third Row 
button3 = Button (frame3, text = "3", font = "Lucida 35 bold")
button3.pack(side = LEFT,padx= 18, pady = 18)
button3.bind("<Button-1>", click)                                             # Binding event with the Button 
button2 = Button (frame3, text = "2", font = "Lucida 35 bold")
button2.pack(side = LEFT,padx= 18, pady = 18)
button2.bind("<Button-1>", click)                                             # Binding event with the Button 
button1 = Button (frame3, text = "1", font = "Lucida 35 bold")
button1.pack(side = LEFT,padx= 18, pady = 18)
button1.bind("<Button-1>", click)                                                 # Binding event with the Button 
button4 = Button(frame3 , text ="*",font= "lucida 35 bold")
button4.pack(side = LEFT,padx= 16, pady = 18)
button4.bind("<Button-1>", click)                                             # Binding event with the Button 



#Creating the frame for fourth Row 
frame4 = Frame(win,bg = "grey")
frame4.pack()

#creating the button in fourth Row 
button1 = Button (frame4, text = "=", font = "Lucida 35 bold")
button1.pack(side = LEFT,padx= 20, pady = 18)
button1.bind("<Button-1>", click)                 # Binding event with the Button 
button2 = Button (frame4, text = "0", font = "Lucida 35 bold")
button2.pack(side = LEFT,padx= 18, pady = 18)
button2.bind("<Button-1>", click)               # Binding event with the Button 
button3 = Button (frame4, text = ".", font = "Lucida 35 bold")
button3.pack(side = LEFT,padx= 18, pady = 18)
button3.bind("<Button-1>", click)             # Binding event with the Button 
button4 = Button (frame4, text = "/", font = "Lucida 35 bold")
button4.pack(side = LEFT,padx= 22, pady = 18)
button4.bind("<Button-1>", click)            # Binding event with the Button 



#Frame and BUtton in  Fifth Row 
frame5 = Frame(win,bg = "grey")
frame5.pack()
button1 = Button (frame5, text = "C", font = "Lucida 35 bold")
button1.pack(padx= 23, pady = 23)
button1.bind("<Button-1>", click)      #Binding Event with the Button 


#Starting The Window 
win.mainloop()                                                




                                                   #Thank You 