from tkinter import *
import random


root = Tk()
root.title("Random japanese word generator")

glob_word_list = [
    ("ureshii", "happy"),
    ("kanashii", "sad"),
    ("nagai", "long"),
    ("nagaimo", "mountain yam"),
    ("nagaisa", "length"),
    ("taskeru", "to help"),
    ("tetsudau", "to assist"),
    ("kaeru", "to return (home)"),
    ("kaesu", "to return and object"),
    ("kasu", "to lend"),
    ("kesu", "to erase"),
    ("hare", "sunny"),
    ("kumo", "cloud"),
    ("taiyou", "sun"),
    ("ame", "rain"),
    ("shokubutsu", "plant"),
    ("doubutsu", "animal"),
    ("seibutsu", "living thing"),
    ("ki", "tree"),
    ("michi", "path/road"),
    ("migi", "right"),
    ("hidari", "left"),
    ("magaru", "turn"),
    ("mado", "window"),
    ("uchi/ie", "house"),
    ("iriguchi", "entrance"),
    ("deguchi", "exit"),
    ("kudasai", "please"),
    ("arigatou (gozaimasu)", "thankyou"),
    ("ao(i)", "blue"),
    ("aka(i)", "red"),
    ("shiro(i)", "white"),
    ("kuro(i)", "black"),
    ("chyairo(i)", "brown"),
    ("midori", "green"),
    ("ki(iro)", "yellow"),
    ("tsukue", "desk"),
    ("me", "eye"),
    ("atama", "head"),
    ("kata", "shoulders"),
    ("ude", "arm"),
    ("kubi", "neck"),
    ("mune", "chest"),
    ("ashi", "leg"),
    ("hana", "nose"),
    ("mimi", "ear"),
    ("hiza", "knee"),
    ("te", "hand"),
    ("nichiyoubi", "Sunday"),
    ("getsuyoubi", "Monday"),
    ("kayoubi", "Tuesday"),
    ("suiyoubi", "Wednesday"),
    ("mokuyoubi", "Thursday"),
    ("kinyoubi", "Friday"),
    ("doyoubi", "Saturday"),
    ("kyou", "today"),
    ("ashita", "tomorrow"),
    ("asate", "the day after tomorrow"),
    ("kinou", "yesterday"),
    ("ototoi", "day before yesterday")
]


japanese_label = Label(root)
english_label = Label(root)

row = NONE


def clear_widget(widget):
    widget.destroy()


def random_word(word_list):
    global japanese_label

    clear_widget(japanese_label)
    clear_widget(english_label)

    list_length = len(word_list)
    global row
    row = random.randint(0, list_length-1)
    japanese_word = word_list[row][0]

    japanese_label = Label(text=japanese_word)
    japanese_label.grid(column=0, row=1)


def english_word(word_list):
    global english_label

    clear_widget(english_label)

    eng_word = word_list[row][1]
    english_label = Label(text=eng_word)
    english_label.grid(column=1, row=1)


jap_button = Button(root, text="Get a random japanese word", command=lambda: random_word(glob_word_list))

english_button = Button(root, text="Get the english translation", command=lambda: english_word(glob_word_list))

jap_button.grid(column=0, row=0)
english_button.grid(column=1, row=0)

root.mainloop()
