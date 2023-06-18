#gerekli kütüphaneleri ekliyorum
import tkinter as tk
from tkinter import *
import random


window = tk.Tk() #pencere oluşturuyorum
window.title("çekiliş")
window.geometry("800x400")
window['background']='#fffdd0'
label = Label(window, text="Çekilişe katılacak isimleri aralarında virgül olacak şekilde yazın", font=('Arial', 15)) #ekranda gözükecek etiketi yazıyorum
label.pack(pady=20) #etiketi yerleştiriyorum
label.config(bg= "#fffdd0", fg= "#654321") #etiket arka plan rengi ve font rengini belirliyorum
text1 = Text(window, height=5)
text1.pack()

def belirle(t): #kazananı belirleyeceğim fonksiyon

        try:
            global kazanan_etiket #kazananı yazacağım etiket
            global kazanan_kisi
            kazanan_kisi = random.choice(t) # herkes içinden kazanan kişi random olarak belirlenir.
            print(kazanan_kisi)
            m = "Kazanan: " + kazanan_kisi
            kazanan_etiket = Label(window, text=m, font=('Arial', 15)) #kazanan kişinin ekrana yazılacağı etiketi oluşturuyorum.
            kazanan_etiket.pack(pady=0)
            kazanan_etiket.config(bg="#fffdd0", fg="#800000")
            EkleButton['state'] = DISABLED
            '''burada ekle butonunu disable hale getiriyorum çünkü aynı kişiler arasından
            yeni bir kişi belirlemek istediğimde başka bir buton kullancağım.'''

        except IndexError:
            '''tüm kişileri seçtikten sonra index error alıyorum çünkü seçilen kişiyi listeden siliyorum ve en son
            liste boş kaldı.Index error için excepti kullanıp ekrana "kişi kalmadı" yazıyorum '''

            bitti = Label(window, text="Kişi kalmadı", font=('Arial', 15))
            bitti.config(bg="#fffdd0", fg="#ff0000")
            bitti.pack(pady=0)


def yenibelirle(a):
    #yeni bir kişi belirleme fonksiyonu
    a.remove(kazanan_kisi) #daha önce seçilen kişiyi tekrar seçmemek için listeden atıyorum.
    belirle(a) #yeni listeyi tekrar belirliyorum.


def yenieklebutton(): #YeniEkle butonunun yapacağı fonksiyon
    kazanan_etiket.destroy() #üst üste yazılmaması için etiketi yok ediyorum
    try:
        yenibelirle(l)
    except:
        pass

def yazdir():
    x = text1.get("1.0", "end-1c") #Kullanıcıdan kişileri virgülle ayırarak alıyorum.
    global l
    l = x.split(',') #Kullanıcıdan aldığım kişileri virgülle ayırıp l listesine atıyorum.
    belirle(l) #kazananı belirleyeceğim fonksiyon

EkleButton = Button(window, text="Ekle", command=yazdir) #Ekle butonu oluşturuyorum command kısmında ise butonun yapacağı işlem bulunmakta
EkleButton.pack(pady=0)
YeniekleButton=Button(window,text="Başka bir seçim yap",command=yenieklebutton)
YeniekleButton.pack(pady=0)

window.mainloop()
