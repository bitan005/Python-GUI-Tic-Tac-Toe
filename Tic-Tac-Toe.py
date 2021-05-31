from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.geometry('550x340')
root.configure(background='aqua')
root.resizable(False, False)


clk = True

def btnclick(btn):
    global clk, move
    if btn['text']=="" and clk==True:
        btn['text'] = "X"
        clk = False
        move +=1
    elif btn['text']=="" and clk==False:
        btn['text'] = "O"
        clk = True
        move +=1
    
    checkwin()


move = 0
player1_score = IntVar()
player2_score = IntVar()
player1_score.set(0)
player2_score.set(0)

def checkwin():
    global move, player1_score, player2_score
    player1_wins = (btn_1['text']=="X" and btn_2['text']=="X" and btn_3['text']=="X" or\
                    btn_4['text']=="X" and btn_5['text']=="X" and btn_6['text']=="X" or\
                    btn_7['text']=="X" and btn_8['text']=="X" and btn_9['text']=="X" or\
                    btn_1['text']=="X" and btn_4['text']=="X" and btn_7['text']=="X" or\
                    btn_2['text']=="X" and btn_5['text']=="X" and btn_8['text']=="X" or\
                    btn_3['text']=="X" and btn_6['text']=="X" and btn_9['text']=="X" or\
                    btn_1['text']=="X" and btn_5['text']=="X" and btn_9['text']=="X" or\
                    btn_3['text']=="X" and btn_5['text']=="X" and btn_7['text']=="X" )
    
    player2_wins = (btn_1['text']=="O" and btn_2['text']=="O" and btn_3['text']=="O" or\
                    btn_4['text']=="O" and btn_5['text']=="O" and btn_6['text']=="O" or\
                    btn_7['text']=="O" and btn_8['text']=="O" and btn_9['text']=="O" or\
                    btn_1['text']=="O" and btn_4['text']=="O" and btn_7['text']=="O" or\
                    btn_2['text']=="O" and btn_5['text']=="O" and btn_8['text']=="O" or\
                    btn_3['text']=="O" and btn_6['text']=="O" and btn_9['text']=="O" or\
                    btn_1['text']=="O" and btn_5['text']=="O" and btn_9['text']=="O" or\
                    btn_3['text']=="O" and btn_5['text']=="O" and btn_7['text']=="O" )



    if player1_wins:
        messagebox.showinfo("Tic Tac Toe", "Player 1 won")
        p1_s = int(player1_score.get())
        p1_s+=1
        player1_score.set(p1_s)
        reset()
        move = 0
    elif player2_wins:
        messagebox.showinfo("Tic Tac Toe", "Player 2 won")
        p2_s = int(player2_score.get())
        p2_s+=1
        player2_score.set(p2_s)
        move = 0
        reset()
    elif move==9:
        messagebox.showinfo("Tic Tac Toe", "Its a tie")
        move = 0
        reset()


def reset():
    global move
    move = 0
    btn_1['text']=""
    btn_2['text']=""
    btn_3['text']=""
    btn_4['text']=""
    btn_5['text']=""
    btn_6['text']=""
    btn_7['text']=""
    btn_8['text']=""
    btn_9['text']=""
    
def newgame():
    global player1_score, player2_score
    reset()
    player1_score.set(0)
    player2_score.set(0)


btn = StringVar()

frame_playbuttons = Frame(root, height=6, width=18, highlightcolor='black', highlightbackground='black', highlightthickness=5, bd=0)
frame_playbuttons.configure(background='chartreuse')
frame_playbuttons.grid(row=0, column=0, padx=10, pady=10)

btn_1 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_1), bg='aquamarine')
btn_1.grid(row=0, column=0, padx=5, pady=5)

btn_2 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_2), bg='aquamarine')
btn_2.grid(row=0, column=1, padx=5, pady=5)

btn_3 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_3), bg='aquamarine')
btn_3.grid(row=0, column=2, padx=5, pady=5)

btn_4 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_4), bg='aquamarine')
btn_4.grid(row=1, column=0, padx=5, pady=5)

btn_5 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_5), bg='aquamarine')
btn_5.grid(row=1, column=1, padx=5, pady=5)

btn_6 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_6), bg='aquamarine')
btn_6.grid(row=1, column=2, padx=5, pady=5)

btn_7 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_7), bg='aquamarine')
btn_7.grid(row=2, column=0, padx=5, pady=5)

btn_8 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_8), bg='aquamarine')
btn_8.grid(row=2, column=1, padx=5, pady=5)

btn_9 = Button(master=frame_playbuttons, text="", height=2, width=6, font=('calibri', 16, 'bold'), relief='ridge', command=lambda:btnclick(btn_9), bg='aquamarine')
btn_9.grid(row=2, column=2, padx=5, pady=5)

frame_info = Frame(root, height=300, width=200)
frame_info.grid(row=0, column=1)


frame_score = Frame(master=frame_info, height=150, width=200)
frame_score.grid(row=0, column=0)

lbl_player1 = Label(master=frame_score, text="Player 1: ", font=('arial rounded mt', 10))
lbl_player1.grid(row=0, column=0, padx=5)
entry_player1_score = Entry(master=frame_score, textvariable=player1_score,  font=('arial rounded mt', 10), width=2, state=DISABLED)
entry_player1_score.grid(row=0, column=1)

lbl_player2 = Label(master=frame_score, text="Player 2: ", font=('arial rounded mt', 10))
lbl_player2.grid(row=1, column=0, padx=5)
entry_player2_score = Entry(master=frame_score, textvariable=player2_score,  font=('arial rounded mt', 10), width=2, state=DISABLED)
entry_player2_score.grid(row=1, column=1)


frame_buttons=Frame(master=frame_info, height=150, width=200)
frame_buttons.grid(row=1, column=0)
button_reset = Button(master=frame_buttons, text="Reset", font=('arial rounded mt', 10), relief='ridge', command=lambda:reset())
button_reset.grid(row=2, column=0, padx=2, pady=15)
button_newgame = Button(master=frame_buttons, text="New Game", font=('arial rounded mt', 10 ), relief='ridge', command=lambda:newgame())
button_newgame.grid(row=2, column=1, padx=2, pady=15)
button_quit = Button(master=frame_buttons, text="Quit", font=('arial rounded mt', 10 ), relief='ridge', command=root.destroy)
button_quit.grid(row=2, column=2, padx=2, pady=15)

root.mainloop()