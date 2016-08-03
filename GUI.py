from tkinter import *
from tkinter import messagebox
from Query import info

info()
from tkinter import PhotoImage

integer23=0
answer=""
title=["blabla","blablabla","blablablabla"]
AZ=["bla","balbla","blablabla"]
urls=["www.google.de","www.bing.de","www.yahoo.de"]
fenster= Tk()
background_image=PhotoImage(file="image.png")
background_label = Label(fenster, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
fenster.configure(background="light cyan")
fenster.title("Urteils Suche")
fenster.geometry("500x500")

lable1= Label(fenster,text="Geben sie bitte eine Suchanfrage ein")
lable1.pack()
eingabe=Entry(fenster)
eingabe.pack()
lable2= Label(fenster, text="")
def such():

    q=eingabe.get()
    #suche mit q
    #get AZ and Url
    global answer
    global integer23
    integer23=0
    knopf4.place(x="0", y=200)
    knopf2.place(x="400", y="200")
    knopf3.place(x="200", y="200")
    lableinfo.place(x="200", y="400")
    lableinfo.pack_configure(side="right")
    nextresult()

knopf1= Button(fenster,text="Suchen",command=such)


def nextresult():
    global integer23
    integer23+=1
    global answer
    try:
        answer ="\n"+ AZ[integer23 -1]+"\n"+title[integer23 -1]
        lableinfo.configure(text="")
    except:
        integer23-=1
        lableinfo.configure(text="error: Kein weiteres Ergebnis gefunden")
        if integer23== 0:
            lableinfo.configure(text="error: Geben sie eine neue Suche ein ")
    lable2.configure(text=answer)
knopf2=Button(fenster,text="nächstes Ergebnis",command=nextresult)

def gotourl():
    import webbrowser
    url=urls[integer23-1]

    messagebox.showinfo(title="Sie werden weiter geleitet zum Urteil", message='Dürcken sie "Str + p" zum drucken')
    webbrowser.open_new_tab(url)

knopf3=Button(fenster,text="Zum Urteil gehen",command=gotourl)
knopf1.pack()

knopf1.configure(background="blue")
knopf3.configure(background="green")


def back():
    global integer23
    lableinfo.configure(text="error: Kein weiteres Ergebnis gefunden")
    if integer23>1:
        integer23-=2
        nextresult()
        lableinfo.configure(text="")
knopf4 =Button(text="vorherigen Ergebnis",command=back)

lableinfo= Label(fenster,text="")

lable2.configure(background="light cyan")
lableinfo.configure(background="light cyan")
lable1.configure(background="light cyan")
knopf2.configure(background="turquoise")
knopf4.configure(background="turquoise")



mainloop()

