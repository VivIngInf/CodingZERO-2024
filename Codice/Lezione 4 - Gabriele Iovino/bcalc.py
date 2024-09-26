import tkinter as tk
import math as m
from pynput.keyboard import Key, Listener


# --Gui Variables-- #

font = ["Helvetica 10", "Helvetica 17", "Helvetica 20"]

bg = "#404040"
fg = "#D5D5D5"

activebg = "#AFAEAE"
activefg = "#767676"

# ----------------- #


# ------Root------ #

root = tk.Tk()  # Init window
root.title("Basic Calculator  -  by Gariko") # Set window's title
root.config(bg = "#505050") #Set background
root.geometry("375x600") # Set window's size
root.resizable(0, 0) # Make window unresizable

# ---------------- #


# ----Variables---- #

mainstring = ""

# ----------------- #


# ----Functions---- #

def flash(b):
    b.after(1, lambda: b.config(bg = activebg, fg = activefg))
    b.after(100, lambda: b.config(bg = bg, fg = fg))

def on_press(key):
    try:
        if key.char == ("0"): zero.invoke(), flash(zero)
        elif key.char == ("1"): one.invoke(), flash(one)
        elif key.char == ("2"): two.invoke(), flash(two)
        elif key.char == ("3"): three.invoke(), flash(three)
        elif key.char == ("4"): four.invoke(), flash(four)
        elif key.char == ("5"): five.invoke(), flash(five)
        elif key.char == ("6"): six.invoke(), flash(six)
        elif key.char == ("7"): seven.invoke(), flash(seven)
        elif key.char == ("8"): eight.invoke(), flash(eight)
        elif key.char == ("9"): nine.invoke(), flash(nine)
        elif key.char == ("+"): plus.invoke(), flash(plus)
        elif key.char == ("-"): minus.invoke(), flash(minus)
        elif key.char == ("/"): divided.invoke(), flash(divided)
        elif key.char == ("*") or key.char == ("x"): times.invoke(), flash(times)
        elif key.char == ("("): openpar.invoke(), flash(openpar)
        elif key.char == (")"): closepar.invoke(), flash(closepar)
        elif key.char == ("="): execute.invoke(), flash(execute)
        elif key.char == ("c"): clear_button.invoke(), flash(clear_button)
        elif key.char == (".") or key.char == (","): comma.invoke(), flash(comma)

    except:
        if key == Key.backspace: canc.invoke(), flash(canc)
        elif key == Key.enter: execute.invoke(), flash(execute)


def on_release(key):
    pass

def normalize():
    global mainstring
    if mainstring.find("÷") != -1:
        mainstring = mainstring.replace("÷","/")

    if mainstring.find("x") != -1:
        mainstring = mainstring.replace("x","*")

    if mainstring.find("e") != -1:
        mainstring = mainstring.replace("e", "2.718281828459") if mainstring[mainstring.index("e")-1].isdigit() else mainstring.replace("e", "2.718281828459")

    if mainstring.find("π") != -1:
        mainstring = mainstring.replace("π", "*3.14159265359") if mainstring[mainstring.index("π")-1].isdigit() else mainstring.replace("π", "3.14159265359")

def error():
    mainlabel.config(text = "Error", fg = "red")
    mainlabel.after(1000, lambda: mainlabel.config(text = mainstring, fg = fg))

def update():
    mainlabel.config(text = mainstring)

def natlog():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = m.log(mainstring)
        update()
    except:
        error()

def loga():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = m.log10(mainstring)
        update()
    except:
        error()

def plus_minus():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = -1*mainstring
        update()
    except:
        error()

def tenpow():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = 10**mainstring
        update()
    except:
        error()

def add(c):
    global mainstring
    if len(mainstring) < 26:
        mainstring = str(mainstring)
        mainstring += c
        update()

def xsquare():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = mainstring**2
        update()
    except:
        error()

def thirdpow():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = mainstring**3
        update()
    except:
        error()

def divtwo():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = mainstring/2
        update()
    except:
        error()

def squareroot():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = mainstring**0.5
        update()
    except:
        error()

def backspace():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = mainstring[:-1]
        update()
    except:
        error()

def fact():
    global mainstring
    try:
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = m.factorial(mainstring)
        update()
    except:
        error()

def clear():
    global mainstring
    mainstring = ""
    update()

def exe():
    global mainstring
    try:
        normalize()
        mainstring = str(mainstring)
        mainstring = eval(mainstring)
        mainstring = str(mainstring)
        update()
    except:
        error()

# ----------------- #



# -----Buttons----- #

ln = tk.Button(text = "ln", command = natlog, font = font[1]) # Natural logarithm
ln.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
ln.place(x = 0, y = 525, width = 75, height = 75)

pom = tk.Button(text = "+/-", command = plus_minus, font = font[1]) # Plus / minus
pom.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
pom.place(x = 75, y = 525, width = 75, height = 75)

zero = tk.Button(text = "0", command = lambda: add("0"), font = font[1])
zero.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
zero.place(x = 150, y = 525, width = 75, height = 75)

comma = tk.Button(text = ",", command = lambda: add("."), font = font[1]) # Plus / minus
comma.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
comma.place(x = 225, y = 525, width = 75, height = 75)

execute = tk.Button(text = "=", command = exe, font = font[1])
execute.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
execute.place(x = 300, y = 525, width = 75, height = 75)

# ---------- #

log = tk.Button(text = "log", command = loga, font = font[1]) # logarithm
log.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
log.place(x = 0, y = 450, width = 75, height = 75)

seven = tk.Button(text = "7", command = lambda: add("7"), font = font[1])
seven.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
seven.place(x = 75, y = 450, width = 75, height = 75)

eight = tk.Button(text = "8", command = lambda: add("8"), font = font[1])
eight.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
eight.place(x = 150, y = 450, width = 75, height = 75)

nine = tk.Button(text = "9", command = lambda: add("9"), font = font[1])
nine.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
nine.place(x = 225, y = 450, width = 75, height = 75)

plus = tk.Button(text = "+", command = lambda: add("+"), font = font[1])
plus.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
plus.place(x = 300, y = 450, width = 75, height = 75)

# ---------- #

ten_pow = tk.Button(text = "10ⁿ", command = tenpow, font = font[1])
ten_pow.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
ten_pow.place(x = 0, y = 375, width = 75, height = 75)

four = tk.Button(text = "4", command = lambda: add("4"), font = font[1])
four.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
four.place(x = 75, y = 375, width = 75, height = 75)

five = tk.Button(text = "5", command = lambda: add("5"), font = font[1])
five.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
five.place(x = 150, y = 375, width = 75, height = 75)

six = tk.Button(text = "6", command = lambda: add("6"), font = font[1])
six.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
six.place(x = 225, y = 375, width = 75, height = 75)

minus = tk.Button(text = "-", command = lambda: add("-"), font = font[1])
minus.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
minus.place(x = 300, y = 375, width = 75, height = 75)

# ---------- #

x_pow = tk.Button(text = "𝑥 ᵞ", command = lambda: add("**"), font = font[1])
x_pow.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
x_pow.place(x = 0, y = 300, width = 75, height = 75)

three = tk.Button(text = "3", command = lambda: add("3"), font = font[1])
three.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
three.place(x = 75, y = 300, width = 75, height = 75)

two = tk.Button(text = "2", command = lambda: add("2"), font = font[1])
two.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
two.place(x = 150, y = 300, width = 75, height = 75)

one = tk.Button(text = "1", command = lambda: add("1"), font = font[1])
one.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
one.place(x = 225, y = 300, width = 75, height = 75)

times = tk.Button(text = "x", command = lambda: add("x"), font = font[1])
times.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
times.place(x = 300, y = 300, width = 75, height = 75)

# ---------- #

square_root = tk.Button(text = "√𝑥", command = squareroot, font = font[1])
square_root.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
square_root.place(x = 0, y = 225, width = 75, height = 75)

openpar = tk.Button(text = "(", command = lambda: add("("), font = font[1])
openpar.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
openpar.place(x = 75, y = 225, width = 75, height = 75)

closepar = tk.Button(text = ")", command = lambda: add(")"), font = font[1])
closepar.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
closepar.place(x = 150, y = 225, width = 75, height = 75)

factorial = tk.Button(text = "n!", command = fact, font = font[1])
factorial.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
factorial.place(x = 225, y = 225, width = 75, height = 75)

divided = tk.Button(text = "÷", command = lambda: add("÷"), font = font[1])
divided.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
divided.place(x = 300, y = 225, width = 75, height = 75)

# ---------- #

square = tk.Button(text = "𝑥²", command = xsquare, font = font[1])
square.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
square.place(x = 0, y = 150, width = 75, height = 75)

div_two = tk.Button(text = "½", command = divtwo, font = font[1])
div_two.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
div_two.place(x = 75, y = 150, width = 75, height = 75)

xmodular = tk.Button(text = "| 𝑥 |", command = lambda: add(")"), font = font[1])
xmodular.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
xmodular.place(x = 150, y = 150, width = 75, height = 75)

exp = tk.Button(text = "exp", command = lambda: add("e "), font = font[1])
exp.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
exp.place(x = 225, y = 150, width = 75, height = 75)

mod = tk.Button(text = "mod", command = lambda: add("%"), font = font[1])
mod.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
mod.place(x = 300, y = 150, width = 75, height = 75)

# ---------- #

third_pow = tk.Button(text = "𝑥³", command = thirdpow, font = font[1])
third_pow.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
third_pow.place(x = 0, y = 75, width = 75, height = 75)

pi = tk.Button(text = "π", command = lambda: add("π"), font = font[1])
pi.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
pi.place(x = 75, y = 75, width = 75, height = 75)

el = tk.Button(text = "e", command = lambda: add("e"), font = font[1])
el.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
el.place(x = 150, y = 75, width = 75, height = 75)

clear_button = tk.Button(text = "C", command = clear, font = font[1])
clear_button.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
clear_button.place(x = 225, y = 75, width = 75, height = 75)

canc = tk.Button(text = "🡐", command = backspace, font = font[1])
canc.config(bg = bg, fg = fg, relief = "flat", bd = 1, activebackground = activebg, activeforeground = activefg, overrelief = "flat")
canc.place(x = 300, y = 75, width = 75, height = 75)

# ----------------- #


# ----MainLabel---- #


mainlabel = tk.Label(text = mainstring, font = font[1])
mainlabel.config(bg = "#505050", fg = fg, anchor = "e")
mainlabel.place(x = 10, y = 0, width = 355, height = 75)

# ----------------- #



# ----MainLoop---- #

if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        root.mainloop()
        listener.join()

# ---------------- #