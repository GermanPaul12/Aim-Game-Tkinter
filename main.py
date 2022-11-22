from tkinter import *
from tkinter import messagebox 
import customtkinter
import random
import numpy as np

root = customtkinter.CTk()

root.title('Farbige Boxen')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.geometry("1200x600")
root.configure(bg='black')

color='red'
points = 0
timer = 60

random_x = np.arange(0, 1170)
random_y = np.arange(115, 470)




def start_game():
    global timer
    root.after(1000, start_game)
    timer -= 1
    title_label.configure(text=f"Points= {points}                  Aim Game                    Time= {timer}")
    if timer <= 0:
        messagebox.showinfo("Game Over", f"Your score is {points}")
        root.destroy()   

def new_loc():
    global points
    button_1.place(x=random.choice(random_x), y=random.choice(random_y))
    points += 1
    if points == 1:
        start_game()
    title_label.configure(text=f"Points= {points}                  Aim Game                    Time= {timer}")
     
         
            
game_frame = customtkinter.CTkFrame(master=root,
                               width=1200,
                               height=600,
                               corner_radius=10,
                               bg='black',
                               fg_color='black',)

title_label = customtkinter.CTkLabel(root, text=f"Points= {points}                  Aim Game                    Time= 60", 
                                width=1200,
                               height=100,
                               fg_color=("white", "white"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 35, 'bold'),
                               bg_color='black',
                               text_color='black')

button_1 = customtkinter.CTkButton(root, command=new_loc, width=30,
                                height=30,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )




#Packing them on the screen

game_frame.place(x=0, y=0)
title_label.place(x=0, y=0)
button_1.place(x=100, y=100)



root.mainloop()