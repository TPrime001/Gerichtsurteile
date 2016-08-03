from tkinter import *



integer23=0
answer=""
AZ=["bla","balbla"]
urls=["www.google.de","www.bing.de"]
fenster= Tk()
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

    nextresult()

knopf1= Button(fenster,text="Suchen",command=such)
knopf1.pack()
lable2.pack()
def nextresult():
    global integer23
    integer23+=1
    global answer
    answer = AZ[integer23 -1]
    lable2.configure(text=answer)
knopf2=Button(fenster,text="nächstes Ergebnis",command=nextresult)
knopf2.pack()
def gotourl():
    import webbrowser
    url=urls[integer23-1]

    webbrowser.open_new_tab(url)
knopf3=Button(fenster,text="Zum Urteil gehen",command=gotourl)
knopf3.pack()

mainloop()