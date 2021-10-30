# String Toolkit
# author: Liran Libster

from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from ttkthemes import themed_tk as tk
from tkinter import filedialog
from collections import Counter
from PyDictionary import PyDictionary
from tkinter import simpledialog
from textatistic import Textatistic
from pynput.keyboard import Controller
from googletrans import Translator
import gtts
from playsound import playsound
import TKlighter
import re
import os
import random

root = tk.ThemedTk()
root.get_themes()
root.set_theme("arc")
root.title('String Toolkit')
root.iconbitmap(r'pencil.ico')
root.geometry("500x500")
image = Image.open("background.png")
image = ImageTk.PhotoImage(image)
bg_label = ttk.Label(root, image=image)
bg_label.place(x=0, y=0)
bg_label.image = image
translator = Translator()
prev = " "
prev_text = " "


# print how many words and how many letters in the text
def key_pressed(event):
    counter = Label(root, text="Words: " + count_words() + " Characters: " + count_chars())
    counter.place(x=10, y=450)


# update the function above if we open text file
def press_space():
    keyboard = Controller()
    key = " "
    keyboard.press(key)
    keyboard.release(key)


# open text file
def open_txt():
    global prev_text
    my_text.delete(1.0, END)
    cwd = os.getcwd()
    text_file = filedialog.askopenfilename(initialdir=format(cwd), title="Open Text File",
                                           filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'r', encoding='utf-8')
    stuff = text_file.read()
    prev_text = stuff
    my_text.insert(END, stuff)
    press_space()
    text_file.close()


# save text file
def save_txt():
    text_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if text_file is None:
        return
    text2save = str(my_text.get(1.0, END))
    text_file.write(text2save)
    text_file.close()


# count how many words in the text
def calc_txt():
    result = my_text.get(1.0, "end-1c")
    result = result.replace(",", '')
    temp = str(Counter(result.split()))
    my_text.delete(1.0, END)
    temp = temp[9:]
    temp = temp[:-2]
    print(temp)
    temp = temp.replace(",", '\n')
    my_text.insert(END, temp)


# arrange the text
def arrange_txt():
    result = str(my_text.get(1.0, "end-1c"))
    result = ' '.join(filter(None, result.split(' ')))
    result = '.'.join(filter(None, result.split('.')))
    result = ','.join(filter(None, result.split(',')))
    my_text.delete(1.0, END)
    my_text.insert(END, result)


# count how many words in the text
def count_words():
    result = str(my_text.get(1.0, "end-1c"))
    result = ' '.join(filter(None, result.split(' ')))
    length = str(len(result.split()))
    return length


# count how many characters in the text
def count_chars():
    result = str(my_text.get(1.0, "end-1c"))
    length = str(len(result))
    return length


# get the definition of a word
def dict_word():
    result = simpledialog.askstring("Definition", "Enter Word:")
    my_dict = PyDictionary(result)
    my_text.delete(1.0, END)
    result = str(my_dict.getMeanings())
    result = result[2:]
    result = result[:-2]

    # remove unnecessary characters
    result = re.sub("'|}|{|\[|\]", "", result)

    press_space()
    my_text.insert(END, result)


# rate the text readability by scores with flesch, gunningfog and dale-chall methods
def read_test():
    result = str(my_text.get(1.0, "end-1c"))
    if result.count(".") == 0:
        result = result + "."
    readability_scores = Textatistic(result).scores
    flesch = str(readability_scores['flesch_score'])
    gunningfog = str(readability_scores['gunningfog_score'])
    dale_chal = str(readability_scores['dalechall_score'])
    result = "Flesch: " + flesch + "\nGunningfog: " + gunningfog + "\nDale-Chall: " + dale_chal
    if result != "":
        open_img()
    my_text.delete(1.0, END)
    my_text.insert(END, result)


# translate words or full text
def trans():
    res = str(my_text.get(1.0, "end-1c"))
    result2 = simpledialog.askstring("Translate", "Enter Language:")
    dict = {"afrikaans": "af",
            "albanian": "sq",
            "amharic": "am",
            "arabic": "ar",
            "armenian": "hy",
            "azerbaijani": "az",
            "basque": "eu",
            "belarusian": "be",
            "bengali": "bn",
            "bosnian": "bs",
            "bulgarian": "bg",
            "catalan": "ca",
            "cebuano": "ceb",
            "chichewa": "ny",
            "chinese (simplified)": "zh-cn",
            "chinese (traditional)": "zh-tw",
            "corsican": "co",
            "croatian": "hr",
            "czech": "cs",
            "danish": "da",
            "dutch": "nl",
            "english": "en",
            "esperanto": "eo",
            "estonian": "et",
            "filipino": "tl",
            "finnish": "fi",
            "french": "fr",
            "frisian": "fy",
            "galician": "gl",
            "georgian": "ka",
            "german": "de",
            "greek": "el",
            "gujarati": "gu",
            "haitian creole": "ht",
            "hausa": "ha",
            "hawaiian": "haw",
            "hebrew": "he",
            "hindi": "hi",
            "hmong": "hmn",
            "hungarian": "hu",
            "icelandic": "is",
            "igbo": "ig",
            "indonesian": "id",
            "irish": "ga",
            "italian": "it",
            "japanese": "ja",
            "javanese": "jw",
            "kannada": "kn",
            "kazakh": "kk",
            "khmer": "km",
            "korean": "ko",
            "kurdish (kurmanji)": "ku",
            "kyrgyz": "ky",
            "lao": "lo",
            "latin": "la",
            "latvian": "lv",
            "lithuanian": "lt",
            "luxembourgish": "lb",
            "macedonian": "mk",
            "malagasy": "mg",
            "malay": "ms",
            "malayalam": "ml",
            "maltese": "mt",
            "maori": "mi",
            "marathi": "mr",
            "mongolian": "mn",
            "myanmar (burmese)": "my",
            "nepali": "ne",
            "norwegian": "no",
            "odia": "or",
            "pashto": "ps",
            "persian": "fa",
            "polish": "pl",
            "portuguese": "pt",
            "punjabi": "pa",
            "romanian": "ro",
            "russian": "ru",
            "samoan": "sm",
            "scots gaelic": "gd",
            "serbian": "sr",
            "sesotho": "st",
            "shona": "sn",
            "sindhi": "sd",
            "sinhala": "si",
            "slovak": "sk",
            "slovenian": "sl",
            "somali": "so",
            "spanish": "es",
            "sundanese": "su",
            "swahili": "sw",
            "swedish": "sv",
            "tajik": "tg",
            "tamil": "ta",
            "telugu": "te",
            "thai": "th",
            "turkish": "tr",
            "ukrainian": "uk",
            "urdu": "ur",
            "uyghur": "ug",
            "uzbek": "uz",
            "vietnamese": "vi",
            "welsh": "cy",
            "xhosa": "xh",
            "yiddish": "yi",
            "yoruba": "yo",
            "zulu": "zu"}
    result2 = dict[result2]
    out = translator.translate(res, dest=result2)
    my_text.delete(1.0, END)
    my_text.insert(END, out.text)


# open the legend for the read_test function
def open_img():
    global pop
    pop = Toplevel(root)
    pop.title("Legend")
    pop.iconbitmap(r'pencil.ico')
    pop.geometry("1302x728")

    global legend
    legend = PhotoImage(file="img.png")

    pop_lable = Label(pop)
    pop_lable.pack(pady=10)

    my_frame = Frame(pop)
    my_frame.pack(pady=5)

    pic = Label(my_frame, image=legend, borderwidth=0)
    pic.grid(row=0, column=0, padx=10)


# find letter in the text and highlights
def find():
    global prev
    TKlighter.custom_h(my_text, prev, 'black')
    result = str(simpledialog.askstring("Find", "Enter Word:"))

    text_content = str(my_text.get(1.0, "end-1c"))
    found_result = text_content.lower().find(result.lower())
    if found_result < 0:
        return

    word_transformed = text_content[found_result:found_result + len(result)]

    TKlighter.custom_h(my_text, word_transformed, 'red')
    prev = word_transformed
    my_text.bind('<key>', find)


# replace substrings in string
def replace():
    text = str(my_text.get(1.0, "end-1c"))
    result = str(simpledialog.askstring("Replace", "To Replace:"))
    result2 = str(simpledialog.askstring("Replace", "New Word:"))
    new = re.sub(result, result2, text)
    my_text.delete(1.0, END)
    my_text.insert(END, new)


# load previous page
def previous():
    my_text.delete(1.0, END)
    my_text.insert(END, prev_text)


def play():
    text = str(my_text.get(1.0, "end-1c"))
    tts = gtts.gTTS(text)
    h = random.randint(1, 10000000)
    audio_file = str(h) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)


my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)

photo = PhotoImage(file=r"find.png")
photo1 = PhotoImage(file=r"return.png")
photo2 = PhotoImage(file=r"play.png")
photo_image = photo.subsample(3, 3)
photo_image1 = photo1.subsample(3, 3)
photo_image2 = photo2.subsample(3, 3)
open_button = ttk.Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=5)
save_button = ttk.Button(root, text="Save File", command=save_txt)
save_button.place(x=297, y=289)
calc_button = ttk.Button(root, text="Calculate Words Frequency", command=calc_txt)
calc_button.pack(pady=1)
arrange_button = ttk.Button(root, text="Text Arrange", command=arrange_txt)
arrange_button.place(x=115, y=289)
definition = ttk.Button(root, text="Definition", command=dict_word)
definition.pack(pady=2)
readability = ttk.Button(root, text="Readability Test", command=read_test)
readability.pack(pady=1)
translate = ttk.Button(root, text="Translate", command=trans)
translate.pack(pady=1)
find = ttk.Button(root, image=photo_image, command=find)
find.place(x=380, y=288)
replace = ttk.Button(root, text="Replace", command=replace)
replace.pack(pady=1)
previous = ttk.Button(root, image=photo_image1, command=previous)
previous.place(x=70, y=288)
play = ttk.Button(root, image=photo_image2, command=play)
play.place(x=30, y=288)

root.bind("<Key>", key_pressed)

root.mainloop()
