from importlib.machinery import WindowsRegistryFinder
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Tic Tac Toe")
isXTurn = True
count = 0
scoreX = 0
scoreO = 0


def checkIfWin():
    global winner 
    global scoreX,scoreO
    winner = False
    if b1["text"] == b2["text"] == b3["text"] == "X":
        b1.config(bg = "red")
        b2.config(bg = "red")
        b3.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
        
    elif b4["text"] == b5["text"] == b6["text"] == "X":
        b4.config(bg = "red")
        b5.config(bg = "red")
        b6.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b7["text"] == b8["text"] == b9["text"] == "X":
        b7.config(bg = "red")
        b8.config(bg = "red")
        b9.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b1["text"] == b4["text"] == b7["text"] == "X":
        b1.config(bg = "red")
        b4.config(bg = "red")
        b7.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b2["text"] == b5["text"] == b8["text"] == "X":
        b2.config(bg = "red")
        b5.config(bg = "red")
        b8.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b3["text"] == b6["text"] == b9["text"] == "X":
        b3.config(bg = "red")
        b6.config(bg = "red")
        b9.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b1["text"] == b5["text"] == b9["text"] == "X":
        b1.config(bg = "red")
        b5.config(bg = "red")
        b9.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b3["text"] == b5["text"] == b7["text"] == "X":
        b3.config(bg = "red")
        b5.config(bg = "red")
        b7.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe",f"Congratulations X wins")
        scoreX+=1
        resetUi()
    elif b1["text"] == b2["text"] == b3["text"] == "O":
        b1.config(bg = "red")
        b2.config(bg = "red")
        b3.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b4["text"] == b5["text"] == b6["text"] == "O":
        b4.config(bg = "red")
        b5.config(bg = "red")
        b6.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b7["text"] == b8["text"] == b9["text"] == "O":
        b7.config(bg = "red")
        b8.config(bg = "red")
        b9.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b1["text"] == b4["text"] == b7["text"] == "O":
        b1.config(bg = "red")
        b4.config(bg = "red")
        b7.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b2["text"] == b5["text"] == b8["text"] == "O":
        b2.config(bg = "red")
        b5.config(bg = "red")
        b8.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b3["text"] == b6["text"] == b9["text"] == "O":
        b3.config(bg = "red")
        b6.config(bg = "red")
        b9.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b1["text"] == b5["text"] == b9["text"] == "O":
        b1.config(bg = "red")
        b5.config(bg = "red")
        b9.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif b3["text"] == b5["text"] == b7["text"] == "O":
        b3.config(bg = "red")
        b5.config(bg = "red")
        b7.config(bg = "red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Congratulations O wins")
        scoreO+=1
        resetUi()
    elif count==9:
        messagebox.showinfo("Tic Tac Toe","Its a Draw")
        scoreO+=0.5
        scoreX+=0.5
        resetUi()
    
    






def onButtonClick(b):
    global isXTurn,count

    if b["text"] == " " and isXTurn:
        b["text"] = "X"
        isXTurn = False
        count+=1
        checkIfWin()
    elif b["text"] == " " and not isXTurn:
        b["text"] = "O"
        isXTurn = True
        count+=1
        checkIfWin()
    else:
        messagebox.showerror("Tic Tac Toe","The Box is already been selected")

def resetUi():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global isXTurn,count
    isXTurn = True
    count = 0
    scorex = Label(root,font = ("Helvetica",20),text = f"X = {scoreX}")
    scoreo = Label(root,font = ("Helvetica",20),text = f"O = {scoreO}")
    score = Label(root,font = ("Helvetica",20),text = "Score")
    b1 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b1)
    )
    b2 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b2)
    )
    b3 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b3)
    )
    b4 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b4)
    )
    b5 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b5)
    )
    b6 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b6)
    )
    b7 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b7)
    )
    b8 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b8)
    )
    b9 = Button(
        root,
        text=" ",
        font = ("Helvetica",20),
        height = 3 ,
        width = 6,
        bg = "SystemButtonFace",
        command = lambda:onButtonClick(b9)
    )
    b1.grid(
        row = 0,column = 0
    )
    b2.grid(
        row = 0,column = 1
    )
    b3.grid(
        row = 0,column = 2
    )
    b4.grid(
        row = 1,column = 0
    )
    b5.grid(
        row = 1,column = 1
    )
    b6.grid(
        row = 1,column = 2
    )
    b7.grid(
        row = 2,column = 0
    )
    b8.grid(
        row = 2,column = 1
    )
    b9.grid(
        row = 2,column = 2
    )
    score.grid(
        row = 3,column = 0
    )
    scorex.grid(
        row = 3,column = 1
    )
    scoreo.grid(
        row = 3,column = 2
    )




resetUi()

root.mainloop()