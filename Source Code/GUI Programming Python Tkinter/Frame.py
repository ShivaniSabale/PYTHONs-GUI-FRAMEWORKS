import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
window.geometry("100x100") 
frame = tkinter.Frame(window) 
frame.grid(row=0, column=0) 
bottomframe = tkinter.Frame(window) 
bottomframe.grid(row=1, column=0) 
redbutton = tkinter.Button(frame, text = 'Red', fg ='red') 
redbutton.grid(row=0, column=0) 
greenbutton = tkinter.Button(frame, text = 'Brown', fg='brown') 
greenbutton.grid(row=0, column=3) 
bluebutton = tkinter.Button(frame, text ='Blue', fg ='blue') 
bluebutton.grid(row=1, column=2) 
blackbutton = tkinter.Button(bottomframe, text ='Black', fg ='black') 
blackbutton.grid(row=0, column=0) 
window.mainloop() 