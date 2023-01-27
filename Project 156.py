# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:09:14 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import *
from PIL import ImageTk , Image

root = Tk()
root.title("Endless pokemon game")
root.geometry("400x400")
root.configure(background="orange")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))

player_1 =  Label(root , text="Player 1" , bg = "red" )
player_1.place(relx=0.1 , rely=0.3 , anchor=CENTER)

player_2 =  Label(root , text="Player 2" , bg = "red" )
player_2.place(relx=0.9 , rely=0.3 , anchor=CENTER)

player_1_score_label =  Label(root , bg = "navy blue")
player_1_score_label.place(relx=0.1 , rely=0.4 , anchor=CENTER)

player_2_score_label =  Label(root , bg = "navy blue")
player_2_score_label.place(relx=0.9 , rely=0.4 , anchor=CENTER)

random_pc_label =  Label(root , bg = "white" )
random_pc_label.place(relx=0.5 , rely=0.5 , anchor=CENTER)

root.mainloop()