
# from tkinter import *
# import pandas
# import random
# BACKGROUND_COLOR = "#B1DDC6"

# current_card= {}
# to_learn= {}

# try:
#     data= pandas.read_csv('data/words_to_learn.csv')
# except FileNotFoundError:
#     original_data= pandas.read_csv('data/frenh_words.csv')
#     to_learn= original_data.to_dict(orient= 'records')
# else:
#     to_learn= data.to_dict(orient= 'records')


# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card= random.choice(to_learn)
#     canvas.itemconfig(card_background, image= card_front_img)
#     canvas.itemconfig(card_title, text= 'French', fill= 'black')
#     canvas.itemconfig(card_word, text= current_card['French'], fill= 'black')
#     flip_timer= window.after(3000, flip_card)

# def flip_card():
#     canvas.itemconfig(card_background, image= card_back_img)
#     canvas.itemconfig(card_title, text= 'English', fill= 'white')
#     canvas.itemconfig(card_word, text= current_card['English'], fill= 'white')


# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data= pandas.DataFrame(to_learn)
#     data.to_csv('data/words_to_learn.csv', index= False)
#     next_card()


# window= Tk()
# window.title('Flashy')
# window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

# flip_timer= window.after(3000, flip_card)


# canvas= Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
# card_front_img= PhotoImage(file= 'images/card_front.png')
# card_back_img= PhotoImage(file= 'images/card_back.png')
# card_background= canvas.create_image(400,262, image= card_front_img)
# card_title= canvas.create_text(400, 150, text= '', font= ('Arial', 40, 'italic'))
# card_word= canvas.create_text(400, 263, text=  '', font= ('Arial', 60, 'bold'))
# canvas.grid(column= 0, row= 0, columnspan= 2)


# cross_img= PhotoImage(file= 'images/wrong.png')
# unknown_button= Button(image= cross_img, highlightthickness= 0, command= next_card)
# unknown_button.grid(column= 1, row= 1)

# check_img= PhotoImage(file= 'images/right.png')
# known_button= Button(image= check_img, highlightthickness= 0, command= is_known)
# known_button.grid(column= 0, row= 1)

# next_card()

# window.mainloop()



# -------------------------------------------------------scratch------------------------------#

# from tkinter import *
# import pandas
# import random

# BACKGROUND_COLOR = "#B1DDC6"
# current_card= {}
# to_learn= {}


# try:
#     data= pandas.read_csv('data/words_to_learn.csv')
# except FileNotFoundError:
#     original_data= pandas.read_csv('data/french_words.csv')
#     to_learn= original_data.to_dict(orient= 'records')
# else:
#     to_learn= data.to_dict(orient= 'records')


# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card= random.choice(to_learn)
#     canvas.itemconfig(card_background, image= card_front_img)
#     canvas.itemconfig(card_title, text= 'French', fill= 'black')
#     canvas.itemconfig(card_word, text= current_card['French'], fill= 'black')
#     flip_timer= window.after(3000, flip_card)


# def flip_card():
#     canvas.itemconfig(card_background, image= card_back_img)
#     canvas.itemconfig(card_title, text= 'English', fill= 'white')
#     canvas.itemconfig(card_word, text= current_card['English'], fill= 'white')

# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data= pandas.DataFrame(to_learn)
#     data.to_csv('data/words_to_learn.csv', index= False)
#     next_card()

# window= Tk()
# window.title('Flashy')
# window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

# flip_timer= window.after(3000, flip_card)

# canvas= Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
# card_back_img= PhotoImage(file= 'images/card_back.png')
# card_front_img= PhotoImage(file= 'images/card_front.png')
# card_background= canvas.create_image(400,262, image= card_front_img)
# card_title= canvas.create_text(400, 150, text= '', font= ('Arial', 40, 'italic'))
# card_word= canvas.create_text(400, 265, text= '',font= ('Arial', 60, 'bold'))
# canvas.grid(column= 0, row= 0, columnspan= 2)


# cross_img= PhotoImage(file= 'images/wrong.png')
# unknown_button= Button(image= cross_img, highlightthickness= 0, command= next_card)
# unknown_button.grid(column= 0, row= 1)

# check_img= PhotoImage(file= 'images/right.png')
# known_button= Button(image= check_img, highlightthickness= 0, command= is_known)
# known_button.grid(column= 1, row= 1)

# next_card()

# window.mainloop()



import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card= {}
to_learn= {}

try:
    data= pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data= pandas.read_csv('data/french_words.csv')
    to_learn= original_data.to_dict(orient= 'records')
else:
    to_learn= data.to_dict(orient= 'records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    canvas.itemconfig(card_background, image= card_front_img)
    canvas.itemconfig(card_title, text= 'French', fill= 'black')
    canvas.itemconfig(card_word, text= current_card['French'], fill= 'black')
    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image= card_back_img)
    canvas.itemconfig(card_title, text= 'English', fill= 'white')
    canvas.itemconfig(card_word, text= current_card['English'], fill= 'white')


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data= pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv')
    next_card()


window= Tk()
window.title('Flashy')
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

flip_timer= window.after(3000, flip_card)

canvas= Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front_img= PhotoImage(file= 'images/card_front.png')
card_back_img= PhotoImage(file= 'images/card_back.png')
card_background= canvas.create_image(400, 262, image= card_front_img)
card_title= canvas.create_text(400, 150, text= '', font= ('Arial', 40, 'italic'))
card_word= canvas.create_text(400, 265, text= '', font= ('Arial', 60, 'bold'))
canvas.grid(column= 0, row= 0, columnspan= 2)

check_img= PhotoImage(file= 'images/right.png')
known_button= Button(image= check_img, highlightthickness= 0, command= is_known)
known_button.grid(column= 1, row= 1)

cross_img= PhotoImage(file= 'images/wrong.png')
unknown_button= Button(image= cross_img, highlightthickness= 0, command= next_card)
unknown_button.grid(column= 0, row= 1)

next_card()


window.mainloop()