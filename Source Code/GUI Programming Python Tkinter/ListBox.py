import tkinter
window = tkinter.Tk()
window.title("My GUI")
window.configure(background="white") 
window.geometry("210x150") 
List_box = tkinter.Listbox(window) 
List_box.insert(1, 'Apple') 
List_box.insert(2, 'Mango') 
List_box.insert(3, 'Grape') 
List_box.insert(4, 'Any other') 
List_box.grid(row=0, column=0) 
window.mainloop()