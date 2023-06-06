from tkinter import *
window=Tk()
window.title("BMI calculator ")
window.minsize(width=1000,height=500)

def calculator():
    boy=entry.get()
    kilo=entry2.get()
    indeks=float(kilo)/float(boy)**2
    if indeks < 18.5:
        label.config(text=f"Vücut kitle indeksiniz: {indeks}  normalin altındasınız")
    if indeks >= 18.5 and indeks <= 24.9:
        label.config(text=f"Vücut kitle indeksiniz: {indeks}  normal kilodasınız")
    if indeks >= 25 and indeks <= 29.9:
        label.config(text=f"Vücut kitle indeksiniz: {indeks}   kilolusunuz")
    if indeks >= 30 and indeks <= 34.9:
        label.config(text=f"Vücut kitle indeksiniz: {indeks}   obezsiniz")
    if indeks >= 35:
        label.config(text=f"Vücut kitle indeksiniz: {indeks}  morbin obezsiniz")


label=Label(window)
label.config(text="",font=("Arial",20))
label.place(x=20,y=30)

label2=Label(window)
label2.config(text="boyunuzu giriniz:",font=("Arial",10))
label2.place(x=400,y=90)

label3=Label(window)
label3.config(text="kilonuzu giriniz:",font=("Arial",10))
label3.place(x=400,y=130)

entry=Entry(window)
entry.place(x=400,y=110)

entry2=Entry(window)
entry2.place(x=400,y=150)


button=Button(window)
button.config(text="Hesapla",bg="black",fg="white",command=calculator)
button.place(x=400,y=180)

window.mainloop()