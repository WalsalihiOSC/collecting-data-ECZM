"""This program is about collecting data from users and whether or not they have a mobile phone"""

from tkinter import *

class CollectingData:
    
    def __init__(self, parent):
        """Collecting person's data"""

        global name, age, answer

        self.person_data = []

        name = 0
        age = 0
        answer = 0
        self.data = Data(name, age, answer)
  
        self.f1 = Frame(parent, height = 450, width = 450)
        self.f1.grid(column = 0, row = 0)
        self.f1.grid_propagate(0)

        self.f2 = Frame(self.f1, height = 100, width = 450, bg = "#5FB7CF")
        self.f2.grid(column = 0, row = 0)
        self.f2.grid_propagate(0)

        self.f3 = Frame(self.f1, height = 130, width = 450, bg = "#AEE4ED")
        self.f3.grid(column = 0, row = 1)
        self.f3.grid_propagate(0)

        self.f4 = Frame(self.f1, height = 120, width = 450, bg = "#AEE4ED")
        self.f4.grid(column = 0, row = 2)
        self.f4.grid_propagate(0)

        self.f5 = Frame(self.f1, height = 100, width = 450, bg = "#AEE4ED")
        self.f5.grid(column = 0, row = 3)
        self.f5.grid_propagate(0)
        
        label1 = Label(self.f2, text = "Collecting Person Data", bg = "#5FB7CF", font = ("", 20))
        label1.grid(column = 0, row = 0, padx = 30, pady = 30)

        button1 = Button(self.f2, text = "Show All", height = 2, width = 10, command = self.change_to_DisplayPersonData)
        button1.grid(column = 1, row = 0, padx = 30)

        label2 = Label(self.f3, text = "First Name:", bg = "#AEE4ED")
        label2.grid(sticky = W, column = 0, row = 0, padx = 30, pady = 30)

        label3 = Label(self.f3, text = "Age", bg = "#AEE4ED")
        label3.grid(sticky = W, column = 0, row = 1, padx = 30)

        name = Entry(self.f3, width = 20)
        name.grid(column = 1, row = 0)

        age = Entry(self.f3, width = 20)
        age.grid(column = 1, row = 1)

        label3 = Label(self.f4, text = "Do you have a mobile phone?", bg = "#AEE4ED")
        label3.grid(column = 0, row = 0, padx = 30, pady = 20)

        button2 = Button(self.f5, text = "Enter Data", command = self.clear_data)
        button2.grid(column = 0, row = 0, padx = 175)

        self.label4 = Label(self.f3, text = "", fg = "red", bg = "#AEE4ED")
        self.label4.grid(sticky = W, column = 2, row = 0, padx = 30, pady = 30)

        self.label5 = Label(self.f3, text = "", fg = "red", bg = "#AEE4ED")
        self.label5.grid(sticky = W, column = 2, row = 0, padx = 30)

        self.label4 = Label(self.f3, text = "", fg = "red", bg = "#AEE4ED")
        self.label4.grid(sticky = W, column = 2, row = 0, padx = 30, pady = 30)

        self.label5 = Label(self.f3, text = "", fg = "red", bg = "#AEE4ED")
        self.label5.grid(sticky = W, column = 2, row = 0, padx = 30)

        answer = StringVar()
        answer.set("0")
        rb1 = Radiobutton(self.f4, variable = answer, value = "has a mobile phone", text = "Yes", bg = "#AEE4ED")
        rb2 = Radiobutton(self.f4, variable = answer, value = "does not has a mobile phone", text = "No", bg = "#AEE4ED")

        rb1.grid(column = 1, row = 0)
        rb2.grid(column = 1, row = 1)

        self.person_data.append(Data(name.get(), str(age.get()), answer.get()))

        
        """Display Person Data"""
        self.xf1 = Frame(parent, height = 450, width = 450)
        self.xf1.grid_propagate(0)

        self.xf2 = Frame(self.xf1, height = 100, width = 450, bg = "#5FB7CF")
        self.xf2.grid(column = 0, row = 0)
        self.xf2.grid_propagate(0)

        self.xf3 = Frame(self.xf1, height = 130, width = 450, bg = "#AEE4ED")
        self.xf3.grid(column = 0, row = 1)
        self.xf3.grid_propagate(0)

        self.xf4 = Frame(self.xf1, height = 120, width = 450, bg = "#AEE4ED")
        self.xf4.grid(column = 0, row = 2)
        self.xf4.grid_propagate(0)

        self.xf5 = Frame(self.xf1, height = 100, width = 450, bg = "#AEE4ED")
        self.xf5.grid(column = 0, row = 3)
        self.xf5.grid_propagate(0)

        xlabel1 = Label(self.xf2, text = "Display Person Data", bg = "#5FB7CF", font = ("", 20))
        xlabel1.grid(column = 0, row = 0, padx = 30, pady = 30)

        xbutton1 = Button(self.xf2, text = "Add New Person", height = 2, width = 15, command = self.change_to_CollectPersonData)
        xbutton1.grid(column = 1, row = 0, padx = 30)

        xlabel2 = Label(self.xf3, text = "First Name:", bg = "#AEE4ED")
        xlabel2.grid(sticky = W, column = 0, row = 0, padx = 30, pady = 30)

        xlabel3 = Label(self.xf3, text = "Age:", bg = "#AEE4ED")
        xlabel3.grid(sticky = W, column = 0, row = 1, padx = 30)

        self.xlabel4 = Label(self.xf3, text = self.person_data[0].name, bg = "#AEE4ED")
        self.xlabel4.grid(column = 1, row = 0)

        self.xlabel5 = Label(self.xf3, text = str(self.person_data[0].age), bg = "#AEE4ED")
        self.xlabel5.grid(column = 1, row = 1)

        self.xlabel6 = Label(self.xf4, text = self.person_data[0].name + self.person_data[0].answer, bg = "#AEE4ED")
        self.xlabel6.grid(column = 0, row = 0, padx = 30)

        xbutton2 = Button(self.xf5, text = "Previous")
        xbutton2.grid(sticky = W, column = 0, row = 0, padx = 30)

        xbutton3 = Button(self.xf5, text = "Next")
        xbutton3.grid(sticky = E, column = 1, row = 0, padx  = 250)
    

    def change_to_DisplayPersonData(self):
        """Takes to the Display Person frame"""
        self.xf1.grid(column = 0, row = 0)
        self.f1.grid_forget()

    def change_to_CollectPersonData(self):
        """Takes to the Collect Person frame"""
        self.f1.grid(column = 0, row = 0)
        self.xf1.grid_forget()

    def clear_data(self):
        """Clears data"""
        name.delete(0, 'end')
        age.delete(0, 'end')
        
    
class Data:
    def __init__(self, name, age, answer):
        self.name = name
        self.age = age
        self.answer = answer




#Main Routine
if __name__ == "__main__":
    root = Tk()
    cd = CollectingData(root)
    root.title("Collecting Data")
    root.mainloop()
    

