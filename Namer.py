import random
import sys
import tkinter as tk

text = "Press Generate To Create A Name"

name1 = []
name2 = []
name3 = []
name4 = []

FACTIONS = ["Space Wolves", "Dark Eldar", "Chaos", "Tau", "Eldar", "Imperial Guard"]
faction = "none"

def fileLocator():
    if (faction == "Space Wolves"):
        fileLoc = "data/SpaceWolves.txt"
    elif (faction == "Dark Eldar"):
        fileLoc = "data/DarkEldar.txt"
    elif (faction == "Chaos"):
        fileLoc = "data/Chaos_General.txt" 
    else:
        fileLoc = "data/Test.txt"
    return fileLoc

def dataLoad(fileLoc):
    if (faction != "Chaos"):
        fullList = [line.strip() for line in open(fileLoc)]
        i = 0;
        q = len(fullList)
        while(i < q):
            word = fullList[i]
            firstChar = word[0]
            if (firstChar == (">")):
                word = word.replace(">", "", 1)
                name2.append(word)
            elif (firstChar == ("-")):
                word = word.replace("-", "", 1)
                word = word
                name3.append(word)
            else:
                name1.append(word)
            i = i+1
    else:
        firstNames = [line.strip() for line in open(fileLoc)]
        if (gdvar.get() == "Nurgle"):
            surnames = [line.strip() for line in open("data/Chaos_Nurgle.txt")]
        else:
            surnames = [line.strip() for line in open("data/Chaos_Khorne.txt")]
        fullList = firstNames + surnames
        print(firstNames)
        i = 0;
        q = len(fullList)
        while(i < q):
            word = fullList[i]
            firstChar = word[0]
            if (firstChar == (">")):
                word = word.replace(">", "", 1)
                name2.append(word)
            elif (firstChar == ("-")):
                word = word.replace("-", "", 1)
                word = word
                name3.append(word)
            elif (firstChar == ("#")):
                word = word.replace("#", "", 1)
                word = word
                name4.append(word)
            else:
                name1.append(word)
            i = i+1

def nameCreator():
    print("name 1 = ", name1)
    print("name 2 = ", name2)
    print("name 3 = ", name3)
    print("name 4 = ", name4)
    if (faction == "Space Wolves"):
        f = random.choice(name1)
        if (len(name1) > 1):
            name1.remove(f)
        else:
            dataLoad(fileLocator())
        name = f + " " + random.choice(name2) + random.choice(name3).lower()
    elif (faction == "Dark Eldar"):
        t = random.choice(name3)
        if (len(name3) > 1):
            name3.remove(t)
        else:
            dataLoad(fileLocator())
        name = random.choice(name1) +  random.choice(name2) + " the " + t
    elif (faction == "Chaos"):
        firstname = random.choice(name1) + random.choice(name4)
        if (gdvar.get() == "Nurgle"):
            surname = " the " + random.choice(name3)
        else:
            surname = random.choice(name2) + random.choice(name3).lower()
        name = firstname + " " + surname
    print("I am running")
    return name

def mainLaunch():
    fact.destroy()

def killPop():
    godPop.destroy()

def textSet():
    print("TextSet is being called")
    text = nameCreator()
    output.config(text = text)


##First Menu
fact = tk.Tk()
fact.title("Faction Picker")
fact.geometry("400x320")
mainframe = tk.Frame(fact)
mainframe.grid(column=0,row=0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 80, padx = 100)

tkvar = tk.StringVar(fact)

choices = FACTIONS
tkvar.set(choices[0]) 

popupMenu = tk.OptionMenu(mainframe, tkvar, *choices)
tk.Label(mainframe, text="Choose a faction").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
fill = tk.Label(fact, text= "", wraplength = 400, font=("Helvetica", 10))
fill.pack()



def change_dropdown(*args):
    print( tkvar.get() )


tkvar.trace('w', change_dropdown)
fill2 = tk.Label(fact, text= "", wraplength = 400, font=("Helvetica", 14))
fill2.pack()
submit = tk.Button(fact, text='Accept', width=25, command=mainLaunch)
submit.pack()


fact.mainloop()
#First Menu#

#Chaos Pop Up#
faction = tkvar.get()
if (faction == "Chaos"):
    godPop = tk.Tk()
    godPop.geometry("400x200")
    godPop.title("God Selector")
    gdvar = tk.StringVar(godPop)
    gods = ["Unmarked", "Khorne", "Nurgle", "Tzeech", "Slaanesh"]
    gdvar.set(gods[0]) 

    popupMenu = tk.OptionMenu(godPop, gdvar, *gods)
    gods = tk.Label(godPop, text = "Choose a Mark of Chaos")
    gods.pack()
    popupMenu.pack()
    fill2 = tk.Label(godPop, text= "", wraplength = 400, font=("Helvetica", 70))
    fill2.pack()
    submit = tk.Button(godPop, text='Accept', width=25, command=killPop)
    submit.pack()

    godPop.mainloop()


#Main Screen#
print (faction)
root = tk.Tk()
root.geometry("400x200")
windName = faction
if (faction == "Chaos"):
    windName = (faction + "(" + gdvar.get() + ")")
root.title(windName + " Name Generator")
dataLoad(fileLocator())
fill = tk.Label(root, text= "", wraplength = 400, font=("Helvetica", 10))
fill.pack()
output = tk.Label(root, text = text, wraplength = 400, font=("Impact", 16))
output.pack()
fill2 = tk.Label(root, text= "", wraplength = 400, font=("Helvetica", 16))
fill2.pack()

button = tk.Button(root, text = 'GENERATE', width=25, command = textSet,font=("Futura"))
button.pack()

root.mainloop()
                    
