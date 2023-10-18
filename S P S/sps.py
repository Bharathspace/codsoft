import tkinter as tk
from tkinter import PhotoImage
import random

class mygui:
    def __init__(self, my_window):
        self.root = my_window
        self.root.title("Rock-Paper-Scissor")
        self.root.geometry("500x600")
        my_window.config(bg='#78F5FF')

        # Image
        self.image1 = PhotoImage(file="1.png")
        self.image2 = PhotoImage(file="2.png")
        self.image3 = PhotoImage(file="3.png")

        # desired size for the button
        desired_width = 100
        desired_height = 100

        desired_width1 = 130
        desired_height1 = 130

        #asnwer label

        #font style for png
        self.Pfstyle = ("Comic Sans MS", 20, "bold")

        #font style for answer label
        self.lfstyle = ("Snap ITC", 20, "bold")

        self.user_get = tk.Label(self.root,text="",bg='#78F5FF',font=self.lfstyle)       #user press sps
        self.user_get.grid(row = 0, column = 1,sticky=tk.N)

        self.computer_sps = tk.Label(self.root, text = "",bg='#78F5FF',font=self.lfstyle) #computer random get
        self.computer_sps.grid(row=1,column=1,sticky=tk.N)

        '''The scores from the user wins
            and computer wins
        '''
        self.score_com_wins = tk.Label(self.root, text = "Computer score: ", font=self.lfstyle,bg='#78F5FF',fg='#F241FA')
        self.score_com_wins.place(x=20,y=450)

        self.score_user_wins = tk.Label(self.root, text = "User score: ", font=self.lfstyle,bg='#78F5FF',fg='#F241FA')
        self.score_user_wins.place(x=20,y=490)

        #score count label of computer choice
        self.com_count = tk.Label(self.root, text='0',font=self.lfstyle,bg='#78F5FF')
        self.com_count.place(x=300,y=450)

        ##score count label of user choice
        self.user_count = tk.Label(self.root, text='0',font=self.lfstyle,bg='#78F5FF')
        self.user_count.place(x=300,y=490)

        #Result Label
        self.result = tk.Label(self.root, text = "Results: ",font=self.lfstyle,bg='#78F5FF',fg='#F241FA') 
        self.result.place(x=160, y=350)

        #output for win, lose, draw
        self.l = tk.Label(self.root,text="",bg='#78F5FF',font=self.lfstyle) 
        self.l.place(x=160, y=400)

        self.win_count = 0     #count assingn for user wins
        self.com_win_count = 0 #count for computer wins

        #heading for computer choice and users choice
        self.user_choice = tk.Label(self.root, text = "USER Choice: ", font = self.lfstyle,bg='#78F5FF',fg='#F241FA')
        self.user_choice.grid(row=0, column=0,sticky=tk.N)

        self.computer_choice = tk.Label(self.root, text = "COMPUTER Choice: ", font = self.lfstyle,bg='#78F5FF',fg='#F241FA')
        self.computer_choice.grid(row = 1, column = 0,sticky=tk.N)

        # Resize to fix for button

        #image 1
        width_ratio = self.image1.width() // desired_width
        height_ratio = self.image1.height() // desired_height

        #2
        width_ratio1 = self.image2.width() // desired_width
        height_ratio1 = self.image2.height() // desired_height

        #3
        width_ratio2 = self.image3.width() // desired_width1
        height_ratio2 = self.image3.height() // desired_height1

        # Buttonn
        self.rock = tk.Button(self.root, 
                               text="Rock",
                               font=self.Pfstyle,
                               fg='black', 
                               width=desired_width, 
                               height=desired_height, 
                               image=self.image1, 
                               compound="center",
                               relief='flat',
                               padx= 10, pady=10,
                               bg='#78F5FF',
                               command=self.click_rock
                               )
        self.rock.place(x=50, y=100)

        
        self.paper = tk.Button(my_window,
                               text="Paper",
                               font=self.Pfstyle,
                               fg='black', 
                               width=desired_width, 
                               height=desired_height, 
                               image=self.image3, 
                               compound="center",
                               relief='flat',
                               padx= 10, pady=10,
                               bg='#78F5FF',
                               command=self.click_paper
                               )
        self.paper.place(x=300, y=100)
        
        self.scissor = tk.Button(my_window,
                               width=desired_width1, 
                               height=desired_height1, 
                               image=self.image2, 
                               compound="center",
                               relief='flat',
                               padx= 10,
                               bg='#78F5FF',
                               command=self.click_scissor
                               )
        self.scissor.place(x=150, y=220)

        # Resize the image
        self.resized_image = self.image1.subsample(width_ratio, height_ratio)
        self.rock.config(image=self.resized_image, compound="center")

        self.resized_image1 = self.image3.subsample(width_ratio1, height_ratio1)
        self.paper.config(image=self.resized_image1, compound="center")

        self.resized_image2 = self.image2.subsample(width_ratio2, height_ratio2)
        self.scissor.config(image=self.resized_image2, compound="center")
    
    # button action


    def click_rock(self):
        self.user_get.config(text="Rock")
        res = self.sps()
        self.computer_sps.config(text = res)
        if 'rock' == res:
            self.l_output = "Match Draw"
            self.l.config(text = self.l_output)
                    
        elif ('rock' and res == 'scissor'):
            self.l_output ='You win'
            self.l.config(text = self.l_output)
            self.win_count += 1
            self.user_count.config(text=self.win_count)
                    
        else:
            self.l_output ="Computer Wins"
            self.l.config(text = self.l_output)
            self.com_win_count += 1
            self.com_count.config(text=self.com_win_count)
                    

    def click_paper(self):

        self.user_get.config(text="Paper")
        res = self.sps()
        self.computer_sps.config(text = res)
        if 'paper' == res:
            self.l_output = "Match Draw"
            self.l.config(text = self.l_output)
                    
        elif ('paper' and res == 'rock'):
            self.l_output ='You win'
            self.l.config(text = self.l_output)
            self.win_count += 1
            self.user_count.config(text=self.win_count)
                    
        else:
            self.l_output ="Computer Wins"
            self.l.config(text = self.l_output)
            self.com_win_count += 1
            self.com_count.config(text=self.com_win_count)
            

    def click_scissor(self):

        self.user_get.config(text="Scissor")
        res = self.sps()
        self.computer_sps.config(text = res)
        if 'scissor' == res:
            self.l_output = "Match Draw"
            self.l.config(text = self.l_output)
                    
        elif ('scissor' and res == 'paper'):
            self.l_output ='You win'
            self.l.config(text = self.l_output)
            self.win_count += 1
            self.user_count.config(text=self.win_count)
                    
        else:
            self.l_output ="Computer Wins"
            self.l.config(text = self.l_output)
            self.com_win_count += 1
            self.com_count.config(text=self.com_win_count)
    
    #random s p s
    def sps(self):
        self.ran = ['rock', 'paper', 'scissor']
        self.rval = random.choice(self.ran)
        return self.rval


if __name__ == "__main__":
    my_window = tk.Tk()
    display = mygui(my_window)
    my_window.mainloop()
