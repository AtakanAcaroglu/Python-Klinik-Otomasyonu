from tkinter import *
import pymysql.cursors
from tkinter import ttk

db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='',
                     db='dis_hekimi_veritabani',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.Cursor)

cursor = db.cursor()
win = Tk()
win.title("Hasta Kayıt - Stok Takip Programı")
win.geometry("400x300")
kAdi = "Atakan"
sifre = "12345"
sonucLabel = Label(win, text="", font=25)


def giris():
    if kAdiEntry.get() == kAdi and sifreEntry.get() == sifre:
        win.destroy()
        anaSayfa = Tk()
        anaSayfa.geometry("400x300")
        anaSayfa.title("Ana Sayfa")

# ---

        def stok_takip():
            stokSayfasi = Tk()
            stokSayfasi.title("Stok İşlemleri")
            stokSayfasi.geometry("400x300")

            ImplantStokEntry = Entry(stokSayfasi, width=16)
            DolguStokEntry = Entry(stokSayfasi, width=16)
            frezStokEntry = Entry(stokSayfasi, width=16)

            def implant_guncelle():
                cursor.execute("UPDATE stok SET malzeme_adedi =%s WHERE malzeme_id =%s ", (ImplantStokEntry.get(), 1))
                db.commit()
                print("İmplant Stoğu Güncellendi")
                cursor.execute("SELECT malzeme_adedi FROM stok where malzeme_id = 1")

            def dolgu_guncelle():
                cursor.execute("UPDATE stok SET malzeme_adedi =%s WHERE malzeme_id =%s ", (DolguStokEntry.get(), 2))
                db.commit()
                print("Dolgu Stoğu Güncellendi")

            def frez_guncelle():
                cursor.execute("UPDATE stok SET malzeme_adedi =%s WHERE malzeme_id =%s ", (frezStokEntry.get(), 3))
                db.commit()
                print("Frez Stoğu Güncellendi")

            ImplantStokArttir = Button(stokSayfasi, text="Implant Stok Güncelle", command=implant_guncelle, width=17)
            DolguStokArttir = Button(stokSayfasi, text="Dolgu Stok Güncelle", command=dolgu_guncelle, width=17)
            FrezStokArttir = Button(stokSayfasi, text="Frez Stok Güncelle", command=frez_guncelle, width=17)

            ImplantStokEntry.grid(row=0, column=1)
            DolguStokEntry.grid(row=1, column=1)
            frezStokEntry.grid(row=2, column=1)

            ImplantStokArttir.grid(row=0, column=2)
            DolguStokArttir.grid(row=1, column=2)
            FrezStokArttir.grid(row=2, column=2)

            kolonlar = ["İmplant", "Dolgu", "Frez"]
            kayitlar = ttk.Treeview(stokSayfasi, columns=kolonlar, show='headings', height=3)
            for i in kolonlar:
                kayitlar.heading(i, text=i)
            kayitlar.grid(row=0, column=0, sticky=NW, rowspan=13)

            kayitlar.column(0, width=56)
            kayitlar.column(1, width=56)
            kayitlar.column(2, width=56)
            # Tablodaki veriler sorgularla çekiliyor
            cursor.execute("SELECT malzeme_adedi FROM stok where malzeme_id = 1")
            implantt = cursor.fetchall()

            cursor.execute("SELECT malzeme_adedi FROM stok where malzeme_id = 2")
            dolguu = cursor.fetchall()

            cursor.execute("SELECT malzeme_adedi FROM stok where malzeme_id = 3")
            frezz = cursor.fetchall()

            for i in range(0, 1):
                tempList = [[implantt[i], dolguu[i], frezz[i]]]
                for (implant, dolgu, frez) in tempList:
                    kayitlar.insert("", "end", values=(implant, dolgu, frez))

            stokSayfasi.mainloop()

# ---

        def hasta_takip():
            hastaSayfasi = Tk()
            hastaSayfasi.title("Hasta İşlemleri")
            hastaSayfasi.geometry("400x300")

            # Gerekli labeller oluşturuluyor
            idLabeli = Label(hastaSayfasi, text="ID :")
            isimLabeli = Label(hastaSayfasi, text="İsim :")
            soyisimLabeli = Label(hastaSayfasi, text="Soyisim :")
            telefonLabeli = Label(hastaSayfasi, text="Telefon No :")

            # Gerekli entryler oluşturuluyor
            idEntry = Entry(hastaSayfasi, width=15)
            isimEntry = Entry(hastaSayfasi, width=15)
            soyisimEntry = Entry(hastaSayfasi, width=15)
            telefonEntry = Entry(hastaSayfasi, width=15)

            # Datagridview oluşturuluyor
            kolonlar = ["ID", "İsim", "Soyisim", "Telefon"]
            kayitlar = ttk.Treeview(hastaSayfasi, columns=kolonlar, show='headings')
            for i in kolonlar:
                kayitlar.heading(i, text=i)
            kayitlar.grid(row=4, column=0, columnspan=18)

            kayitlar.column(0, width=55)
            kayitlar.column(1, width=115)
            kayitlar.column(2, width=115)
            kayitlar.column(3, width=115)

            # Tablodaki veriler sorgularla çekiliyor
            cursor.execute("SELECT hasta_id  FROM hastalar ")
            idleri = cursor.fetchall()

            cursor.execute("SELECT hasta_adi FROM hastalar ")
            isim = cursor.fetchall()

            cursor.execute("SELECT hasta_soyadi FROM hastalar ")
            soyisim = cursor.fetchall()

            cursor.execute("SELECT hasta_telefon_no FROM hastalar ")
            telefon = cursor.fetchall()

            for i in range(0, len(telefon)):
                tempList = [[idleri[i], isim[i], soyisim[i], telefon[i]]]
                for (idler, isimler, soyisimler, telefonlar) in tempList:
                    kayitlar.insert("", "end", values=(idler, isimler, soyisimler, telefonlar))

            def hasta_kaydet():
                sonuc = cursor.execute('INSERT INTO HASTALAR VALUES(%s,%s,%s,%s)',
                                       (None, isimEntry.get(), soyisimEntry.get(), telefonEntry.get()))
                db.commit()
                print(str(sonuc) + " kayıt eklendi")

            def hasta_sil():
                sonuc = cursor.execute("DELETE FROM hastalar WHERE hasta_id =%s", (idEntry.get()))
                db.commit()
                print(str(sonuc) + " kayıt silindi")

            def hasta_guncelle():
                sonuc = cursor.execute("UPDATE hastalar SET hasta_telefon_no =%s WHERE hasta_id =%s ",
                                       (telefonEntry.get(), idEntry.get()))
                db.commit()
                print(str(sonuc) + " kayıt güncellendi")

            ekleButonu = Button(hastaSayfasi, text="Ekle", command=hasta_kaydet, width=6)
            silButonu = Button(hastaSayfasi, text="Sil", command=hasta_sil, width=6)
            guncelleButonu = Button(hastaSayfasi, text="Güncelle", command=hasta_guncelle, width=6)

            idLabeli.grid(row=0, column=0, sticky=W)
            isimLabeli.grid(row=1, column=0, sticky=W)
            soyisimLabeli.grid(row=2, column=0, sticky=W)
            telefonLabeli.grid(row=3, column=0, sticky=W)

            idEntry.grid(row=0, column=1, sticky=W)
            isimEntry.grid(row=1, column=1, sticky=W)
            soyisimEntry.grid(row=2, column=1, sticky=W)
            telefonEntry.grid(row=3, column=1, sticky=W)

            ekleButonu.grid(row=0, column=3, sticky=W)
            silButonu.grid(row=1, column=3, sticky=W)
            guncelleButonu.grid(row=2, column=3, sticky=W)

            hastaSayfasi.mainloop()

# ---

        def hasta_gecmisi_ekle():
            gecmisEkleSayfasi = Tk()
            gecmisEkleSayfasi.title("Hasta Geçmişine Kayıt Ekleme")
            gecmisEkleSayfasi.geometry("400x400")
            hastaIDLabeli = Label(gecmisEkleSayfasi, text="Hasta ID :")
            doktorIDLabeli = Label(gecmisEkleSayfasi, text="Doktor ID :")
            islemIDLabeli = Label(gecmisEkleSayfasi, text="İşlem ID :")
            tarihLabeli = Label(gecmisEkleSayfasi, text="İşlem Tarihi :")
            hastaIDEntry = Entry(gecmisEkleSayfasi, width=10)
            doktorIDEntry = Entry(gecmisEkleSayfasi, width=10)
            islemIDEntry = Entry(gecmisEkleSayfasi, width=10)
            tarihEntry = Entry(gecmisEkleSayfasi, width=10)
            bolum = Label(gecmisEkleSayfasi, text="================================================")
            hastaIDgoruntulemeLabeli = Label(gecmisEkleSayfasi,
                                             text="ID sini öğrenmek istediğiniz hastanın telefon numarasını giriniz :")
            hastaIDgosterLabeli = Label(gecmisEkleSayfasi, text="")
            hastaIDogrenmeEntry = Entry(gecmisEkleSayfasi, width=30)
            doktor_idOgrenmeLabeli = Label(gecmisEkleSayfasi,
                                           text="ID sini öğrenmek istediğiniz doktorun telefon numarasını giriniz :")
            doktor_idgosterLabeli = Label(gecmisEkleSayfasi, text="")
            doktorIDogrenmeEntry = Entry(gecmisEkleSayfasi, width=30)
            islemIDogrenmeLabeli = Label(gecmisEkleSayfasi,
                                         text="ID sini öğrenmek istediğiniz işlemin ismini giriniz :")
            islemIDgosterLabeli = Label(gecmisEkleSayfasi, text="")
            islemIDogrenmeEntry = Entry(gecmisEkleSayfasi, width=30)
            def gecmis_kaydet():
                sonuc = cursor.execute('INSERT INTO randevu VALUES(%s,%s,%s,%s,%s)',
                                       (None, hastaIDEntry.get(), doktorIDEntry.get(), islemIDEntry.get(),
                                        tarihEntry.get()))
                db.commit()
                print(str(sonuc) + " kayıt eklendi")
            def id_ogren():
                sonuc = cursor.execute("SELECT "
                                       "hasta_id,hasta_adi,hasta_soyadi "
                                       "FROM hastalar "
                                       "WHERE hasta_telefon_no =%s ", (hastaIDogrenmeEntry.get(),))
                sorgu = cursor.fetchall()
                for i in sorgu:
                    hastaIDgosterLabeli["text"] = i
                    print(i)
                print(str(sonuc) + " adet hasta verisi getirildi")
                sonuc2 = cursor.execute("SELECT "
                                        "doktor_id,doktor_adi,doktor_soyadi "
                                        "FROM doktorlar "
                                        "WHERE doktor_telefon_no =%s ", (doktorIDogrenmeEntry.get()))
                sorgu2 = cursor.fetchall()
                for i in sorgu2:
                    doktor_idgosterLabeli["text"] = i
                    print(i)
                print(str(sonuc2) + " adet doktor verisi getirildi")
                sonuc3 = cursor.execute("SELECT * FROM islemler where islem_adi =%s", islemIDogrenmeEntry.get())
                sorgu3 = cursor.fetchall()
                for i in sorgu3:
                    print(i)
                    islemIDgosterLabeli["text"] = i
                print(str(sonuc3) + " adet işlem verisi getirildi")
            ekleButonu = Button(gecmisEkleSayfasi, text="Ekle", command=gecmis_kaydet, width=6)
            ogrenButonu = Button(gecmisEkleSayfasi, text="Göster", command=id_ogren, width=6)
            hastaIDLabeli.grid(row=0, column=0, sticky=W)
            hastaIDEntry.grid(row=0, column=1, sticky=W)
            ekleButonu.grid(row=0, column=2, sticky=W)
            doktorIDLabeli.grid(row=1, column=0, sticky=W)
            doktorIDEntry.grid(row=1, column=1, sticky=W)
            islemIDLabeli.grid(row=2, column=0, sticky=W)
            islemIDEntry.grid(row=2, column=1, sticky=W)
            tarihLabeli.grid(row=3, column=0, sticky=W)
            tarihEntry.grid(row=3, column=1, sticky=W)
            bolum.grid(row=4, column=0, columnspan=10)
            ogrenButonu.grid(row=5, column=8, sticky=E)
            hastaIDgoruntulemeLabeli.grid(row=5, column=0, columnspan=6)
            hastaIDogrenmeEntry.grid(row=6, column=0, columnspan=6)
            hastaIDgosterLabeli.grid(row=7, column=0, columnspan=6)
            doktor_idOgrenmeLabeli.grid(row=9, column=0, columnspan=6)
            doktorIDogrenmeEntry.grid(row=10, column=0, columnspan=6)
            doktor_idgosterLabeli.grid(row=11, column=0, columnspan=6)
            islemIDogrenmeLabeli.grid(row=12, column=0, columnspan=6)
            islemIDogrenmeEntry.grid(row=13, column=0, columnspan=6)
            islemIDgosterLabeli.grid(row=14, column=0, columnspan=6)
            gecmisEkleSayfasi.mainloop()

# ---

        def hasta_gecmisi_ara():
            gecmisSayfasi = Tk()
            gecmisSayfasi.title("Hastanın Geçmişini Kontrol Et")
            gecmisSayfasi.geometry("700x250")

            idLabeli = Label(gecmisSayfasi, text="Hasta ID :")
            idEntry = Entry(gecmisSayfasi)

            kolonlar = ["Randevu ID", "Hasta ID", "İsim", "Soyisim", "Doktor İsmi", "İşlem Tarihi", "İşlem"]
            kayitlar = ttk.Treeview(gecmisSayfasi, columns=kolonlar, show='headings')
            for i in kolonlar:
                kayitlar.heading(i, text=i)
            kayitlar.grid(row=4, column=0, columnspan=18)

            kayitlar.column(0, width=70)
            kayitlar.column(1, width=60)
            kayitlar.column(2, width=115)
            kayitlar.column(3, width=115)
            kayitlar.column(4, width=115)
            kayitlar.column(5, width=115)
            kayitlar.column(6, width=115)

            def ara():
                # Tablodaki veriler sorgularla çekiliyor
                cursor.execute("SELECT randevu_id "
                               "FROM randevu,hastalar "
                               "WHERE randevu.hasta_id = hastalar.hasta_id AND "
                               "hastalar.hasta_id =%s", idEntry.get())
                randevu_id = cursor.fetchall()

                cursor.execute("SELECT randevu.hasta_id "
                               "FROM randevu,hastalar "
                               "WHERE randevu.hasta_id = hastalar.hasta_id AND "
                               "hastalar.hasta_id = %s", idEntry.get())
                idleri = cursor.fetchall()

                cursor.execute("SELECT hastalar.hasta_adi "
                               "FROM randevu,hastalar "
                               "WHERE randevu.hasta_id = hastalar.hasta_id AND "
                               "hastalar.hasta_id =%s", idEntry.get())
                isim = cursor.fetchall()

                cursor.execute("SELECT hastalar.hasta_soyadi "
                               "FROM randevu,hastalar "
                               "WHERE randevu.hasta_id = hastalar.hasta_id AND "
                               "hastalar.hasta_id =%s", idEntry.get())
                soyisim = cursor.fetchall()

                cursor.execute("SELECT doktorlar.doktor_adi "
                               "FROM randevu,doktorlar,hastalar "
                               "WHERE doktorlar.doktor_id = randevu.doktor_id AND "
                               "randevu.hasta_id = hastalar.hasta_id AND "
                               "hastalar.hasta_id =%s", idEntry.get())
                doktor_adi = cursor.fetchall()

                cursor.execute("SELECT randevu.islem_tarihi "
                               "FROM randevu,hastalar,doktorlar "
                               "WHERE doktorlar.doktor_id = randevu.doktor_id AND "
                               "randevu.hasta_id = hastalar.hasta_id AND "
                               "hastalar.hasta_id =%s ", idEntry.get())
                tarih = cursor.fetchall()

                cursor.execute("SELECT islemler.islem_adi "
                               "FROM randevu,hastalar,doktorlar,islemler "
                               "WHERE doktorlar.doktor_id = randevu.doktor_id AND "
                               "randevu.hasta_id = hastalar.hasta_id AND "
                               "randevu.islem_id = islemler.islem_id AND "
                               "hastalar.hasta_id =%s", idEntry.get())
                islem_adi = cursor.fetchall()

                for i in range(0, len(islem_adi)):
                    tempList = [[randevu_id[i], idleri[i], isim[i], soyisim[i], doktor_adi[i], tarih[i], islem_adi[i]]]
                    for (randevu_idsi, idler, isimler, soyisimler, doktor_isim, tarihi, islem_ismi) in tempList:
                        kayitlar.insert("", "end", values=(
                            randevu_idsi, idler, isimler, soyisimler, doktor_isim, tarihi, islem_ismi))

            idLabeli.grid(row=0, column=0, sticky=W)
            idEntry.grid(row=0, column=1, sticky=W)
            araButonu = Button(gecmisSayfasi, text="Ara", command=ara)
            araButonu.grid(row=0, column=2, sticky=W)

            gecmisSayfasi.mainloop()

# ---

        def doktor_takip():
            doktorSayfasi = Tk()
            doktorSayfasi.title("Doktor İşlemleri")
            doktorSayfasi.geometry("400x300")
            # Gerekli labeller oluşturuluyor
            idLabeli = Label(doktorSayfasi, text="ID :")
            isimLabeli = Label(doktorSayfasi, text="İsim :")
            soyisimLabeli = Label(doktorSayfasi, text="Soyisim :")
            telefonLabeli = Label(doktorSayfasi, text="Telefon No :")
            # Gerekli entryler oluşturuluyor
            idEntry = Entry(doktorSayfasi, width=15)
            isimEntry = Entry(doktorSayfasi, width=15)
            soyisimEntry = Entry(doktorSayfasi, width=15)
            telefonEntry = Entry(doktorSayfasi, width=15)
            # Datagridview oluşturuluyor
            kolonlar = ["ID", "İsim", "Soyisim", "Telefon"]
            kayitlar = ttk.Treeview(doktorSayfasi, columns=kolonlar, show='headings')
            for i in kolonlar:
                kayitlar.heading(i, text=i)
            kayitlar.grid(row=4, column=0, columnspan=18)

            kayitlar.column(0, width=55)
            kayitlar.column(1, width=115)
            kayitlar.column(2, width=115)
            kayitlar.column(3, width=115)
            # Tablodaki veriler sorgularla çekiliyor
            cursor.execute("SELECT doktor_id  FROM doktorlar ")
            idleri = cursor.fetchall()

            cursor.execute("SELECT doktor_adi FROM doktorlar ")
            isim = cursor.fetchall()

            cursor.execute("SELECT doktor_soyadi FROM doktorlar ")
            soyisim = cursor.fetchall()

            cursor.execute("SELECT doktor_telefon_no FROM doktorlar ")
            telefon = cursor.fetchall()

            for i in range(0, len(telefon)):
                tempList = [[idleri[i], isim[i], soyisim[i], telefon[i]]]
                for (idler, isimler, soyisimler, telefonlar) in tempList:
                    kayitlar.insert("", "end", values=(idler, isimler, soyisimler, telefonlar))

            def doktor_kaydet():
                sonuc = cursor.execute('INSERT INTO doktorlar VALUES(%s,%s,%s,%s)',
                                       (None, isimEntry.get(), soyisimEntry.get(), telefonEntry.get()))
                db.commit()

                print(str(sonuc) + " kayıt eklendi")

            def doktor_sil():
                sonuc = cursor.execute("DELETE FROM doktorlar WHERE doktor_id=%s", (idEntry.get()))
                db.commit()

                print(str(sonuc) + " kayıt silindi")

            def doktor_guncelle():
                sonuc = cursor.execute("UPDATE doktorlar SET doktor_telefon_no =%s WHERE doktor_id =%s ",
                                       (telefonEntry.get(), idEntry.get()))
                db.commit()

                print(str(sonuc) + " kayıt güncellendi")

            ekleButonu = Button(doktorSayfasi, text="Ekle", command=doktor_kaydet, width=6)
            silButonu = Button(doktorSayfasi, text="Sil", command=doktor_sil, width=6)
            guncelleButonu = Button(doktorSayfasi, text="Güncelle", command=doktor_guncelle, width=6)

            idLabeli.grid(row=0, column=0, sticky=W)
            isimLabeli.grid(row=1, column=0, sticky=W)
            soyisimLabeli.grid(row=2, column=0, sticky=W)
            telefonLabeli.grid(row=3, column=0, sticky=W)

            idEntry.grid(row=0, column=1, sticky=W)
            isimEntry.grid(row=1, column=1, sticky=W)
            soyisimEntry.grid(row=2, column=1, sticky=W)
            telefonEntry.grid(row=3, column=1, sticky=W)

            ekleButonu.grid(row=0, column=3, sticky=W)
            silButonu.grid(row=1, column=3, sticky=W)
            guncelleButonu.grid(row=2, column=3, sticky=W)

            doktorSayfasi.mainloop()

        secimLabeli = Label(anaSayfa, text="Lütfen Seçim Yapınız ", font=45)
        hasta_kayit_butonu = Button(text="Hasta Kaydı", command=hasta_takip, font=45, width=15)
        stok_takip_butonu = Button(text="Stoklar", command=stok_takip, font=35, width=15)
        hasta_gecmisi_butonu = Button(text="Hasta Geçmişi Ara", command=hasta_gecmisi_ara, font=35, width=15)
        doktor_kayit_butonu = Button(text="Doktor Kaydı", command=doktor_takip, font=35, width=15)
        hasta_gecmis_ekle_butonu = Button(text="Hasta Geçmişi Ekle", command=hasta_gecmisi_ekle, font=35, width=15)

        secimLabeli.grid(row=0, column=0)
        hasta_kayit_butonu.grid(row=1, column=2)
        hasta_gecmis_ekle_butonu.grid(row=2, column=2)
        hasta_gecmisi_butonu.grid(row=3, column=2)
        doktor_kayit_butonu.grid(row=4, column=2)
        stok_takip_butonu.grid(row=5, column=2)

        anaSayfa.mainloop()

    elif kAdiEntry.get() != kAdi and sifreEntry.get() == sifre:
        sonucLabel["text"] = "Kullanıcı Adınız Hatalı"
    elif kAdiEntry.get() == kAdi and sifreEntry.get() != sifre:
        sonucLabel["text"] = "Şifreniz Hatalı"
    elif kAdiEntry.get() != kAdi and sifreEntry.get() != sifre:
        sonucLabel["text"] = "Tüm Bilgileriniz Hatalıdır"


sekilLabelleri = Label(win, bg="cyan", text="Hasta Kayıt", font=("Arial", 18))

kAdiLabel = Label(win, text="Kullanıcı Adınız : ", font=100)
kAdiEntry = Entry(win, fg="black", width=15, borderwidth=5, font=10)
kAdiEntry.insert(0, "Atakan")

sifreLabel = Label(win, text="Şifreniz : ", font=100)
sifreEntry = Entry(win, fg="black", width=15, borderwidth=5, font=10, show="*")
sifreEntry.insert(0, "12345")

girisButton = Button(win, text="Giriş Yap", command=giris, font=15)
sekilLabelleri2 = Label(win, bg="cyan", text="Ve Stok Takip Programı", font=("Arial", 18))

sekilLabelleri.grid(row=0, column=1, sticky=W)
kAdiLabel.grid(row=1, column=0, sticky=W)
sifreLabel.grid(row=2, column=0, sticky=W)
kAdiEntry.grid(row=1, column=1, sticky=W)
sifreEntry.grid(row=2, column=1, sticky=W)
girisButton.grid(row=3, column=0)
sonucLabel.grid(row=3, column=1)
sekilLabelleri2.grid(row=4, column=1)

win.mainloop()
