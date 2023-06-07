#acil durum menüsü
def govde():
    j=1
    while True:
        j += 1
        print("a-Deprem acil durum bildirimi için 1 i tuşlayınız.\n")
        print("b-Depremzede yakını veya kayıp hayvan bildirimi için 2 yi tuşlayınız.\n")
        print("c-Depremzede olup ihtiyaç talepleri için 3 ü tuşlayınız.\n")
        print("d-Depremde yıkılan ve hasar alan binaları öğrenmek için 4 ü tuşlayınız.\n")
        print("e-Deprem bölgesinde gönüllü olarak ekiplere destek vermek için 5 i tuşlayınız.\n")
        print("f-Deprem bölgesine gidecek olan yardım araçları için yol-trafik bilgisi almak için 6 yı tuşlayınız.\n")
        aldeger = input("")
        if aldeger == "1":
                bilgi1 = "Tarafınızdan alınan bilgiler doğrultusunda bulunduğunuz konuma en kısa sürede ulaştırılmak üzere ekipler yönlendirilmiştir."
                print(bilgi1)
                print(sozluk["kamuspotu"])
                break
        elif aldeger == "2":
                demet0 = ("""Depremzede bilgisi almak istiyorsanız 1'i tuşlayınız.""","""Kayıp evcil hayvanınız hakkında bilgi almak için lütfen 2'yi tuşlayınız :""")
                print(demet0[0])
                print(demet0[1])
                soru_bilgi = input()
                if soru_bilgi == "1":
                    DepremzedeBigileri.kisi_oku()
                    break
                elif soru_bilgi == "2":
                    KayipHayvanBilgisi.h_oku()
                    break
                else:
                    print(sozluk2["uyarimesaj"])
                    continue
        elif aldeger == "3":
                TalepBilgiFormu.talep_kaydet()
                print("Talepleriniz alınmış olup en kısa zamanda tarafınıza aktarılacaktır.")
                print(sozluk["kamuspotu"])
                break
        elif aldeger == "4": 
                durum1.durum_oku()
                break
        elif aldeger == "5":
                durum2.durum_oku()
                break
        elif aldeger == "6":
                durum3.durum_oku()
                break
        else:
            print(sozluk2["uyarimesaj"])
            continue
        
                
#Admin panelini açarak Sqlite3 ile oluşturduğum depremde hasar alan binaların kaydedildiği,
#deprem bölgesine gidecek gönüllüler hakkında bilgilerin tutulduğu ve deprem bölgesine
#gidecek araçlara yollar hakkında verilen bilgilerin tutulduğu veritabanı('database11.db')

import sqlite3

class DurumYonetimi:
    
    def __init__(self):
        self.conn = sqlite3.connect('database11.db')
        self.cursor = self.conn.cursor()
        self.tablo_olustur()

    #tablo ouştur
    def tablo_olustur(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Durumlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                durum TEXT
            )
        ''')
        self.conn.commit()

    #kullanıcı kaydı yap
    def durum_ekle(self):
        t=0
        while True:
            t+=1
            status = input("Son durumu girin: ")
            self.cursor.execute('INSERT INTO Durumlar (durum) VALUES (?)', (status,))
            self.conn.commit()
            print("Durum kaydedildi!")
            break
        
    #kayıtlı kullanıcı bilgilerini oku
    def durum_oku(self):
        self.cursor.execute('SELECT * FROM Durumlar')
        rows = self.cursor.fetchall()

        if len(rows) > 0:
            print("Sırasıyla Sisteme Girilen Durumlar:")
            for row in rows:
                print(f"Durum ID: {row[0]}, Son Durum: {row[1]}")
        else:
            print("Kaydedilmiş bir durum bulunmamaktadır.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        
durum1=DurumYonetimi()
durum1.tablo_olustur()

durum2=DurumYonetimi()
durum2.tablo_olustur()

durum3=DurumYonetimi()
durum3.tablo_olustur()


#Sqlite3 ile oluşturduğum depremzede durum bilgilerinin kaydedildiği veritabanı('database22.db')

class DepremzedeBigileri:
    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('database22.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Depremzedeler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT,
                soyad TEXT,
                durumu TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @classmethod
    def kisi_kaydet(cls):
        ad = input("Depremzede ismini girin: ")
        soyad = input("Depremzede soyismini girin: ")
        durumu = input("Depremzede durumunu girin: ")

        conn = sqlite3.connect('database22.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Depremzedeler (ad, soyad, durumu) VALUES (?, ?, ?)', (ad, soyad, durumu))
        conn.commit()
        conn.close()
        print("Depremzede bilgileri kaydedildi!")

    @classmethod
    def kisi_oku(cls):
        conn = sqlite3.connect('database22.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Depremzedeler')
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for row in rows:
                print(f"Depremzede Bilgileri; Ad: {row[1]}, Soyad: {row[2]}, Durumu: {row[3]}")
        else:
            print("Veritabanında kayıtlı depremzede bilgisi bulunamadı.")

DepremzedeBigileri.create_table()


#Sqlite3 ile oluşturduğum kayıp hayvan bilgilerinin tutulduğu veritabanı('database33.db')

class KayipHayvanBilgisi:
    @classmethod
    def create_table1(cls):
        conn = sqlite3.connect('database33.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS KayipHayvanlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cins TEXT,
                renk TEXT,
                durumu TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @classmethod
    def h_kaydet(cls):
        cins = input("Kayıp hayvan cinsini girin: ")
        renk = input("Kayıp hayvan rengini girin: ")
        durumu = input("Kayıp hayvan durumunu girin: ")

        conn = sqlite3.connect('database33.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO KayipHayvanlar (cins, renk, durumu) VALUES (?, ?, ?)', (cins, renk, durumu))
        conn.commit()
        conn.close()
        print("Kayip evcil hayvan bilgileri kaydedildi!")

    @classmethod
    def h_oku(cls):
        conn = sqlite3.connect('database33.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM KayipHayvanlar')
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for row in rows:
                print(f"Kayip Hayvan Bilgileri; Cinsi: {row[1]}, Rengi: {row[2]}, Durumu: {row[3]}")
        else:
            print("Veritabanında kayıtlı kayıp hayvan bilgisi bulunamadı.")

KayipHayvanBilgisi.create_table1()


#Sqlite3 ile oluşturduğum ihtiyaç taleplerinin tutulduğu veritabanı('database44.db')

class TalepBilgiFormu:
    @classmethod
    def create_table2(cls):
        conn = sqlite3.connect('database44.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS IhtiyacTalepleri (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                soru10 TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @classmethod
    #depremzede ihtiyaç taleplerini veritabanına kaydet
    def talep_kaydet(cls):
        soru10 = input("Sizlere daha etkin ve hızlı yardımcı olabilmemiz adına ihtiyaç taleplerinizi bu ekrandan bizimle yazılı olarak paylaşır mısınız? \nTalebiniz: ")
        conn = sqlite3.connect('database44.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO IhtiyacTalepleri (soru10) VALUES (?)', (soru10,))
        conn.commit()
        conn.close()
        print("Talebiniz kaydedildi!")

TalepBilgiFormu.create_table2()


#pandas kütüphanesi ile xlsx dosya formatındaki dosyaya kayıt yapan register(kayıt) ekranı
import pandas as pd
def register():
    ad = input("Adınızı giriniz: ")
    soyad = input("Soyadınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    kisi = {'Ad': ad, 'Soyad': soyad, 'Şifre': sifre}
    df = pd.DataFrame(kisi, index=[0])
    df.to_excel('users.xlsx', index=False)
    print("Kullanıcı kaydı başarıyla oluşturulmuştur.")

#pandas kütüphanesi ile xlsx dosya formatındaki dosyaya login(giriş) yapan ekran
def login():
    while True:
        first_name = input("Adınızı Giriniz: ")
        last_name = input("Soyadınızı Giriniz: ")
        password = input("Şifrenizi Giriniz: ")
        print("\n")
        users_df = pd.read_excel('users.xlsx')
        matching_user = users_df[(users_df['Ad'] == first_name) & (users_df['Soyad'] == last_name) & (users_df['Şifre'] == password)]

        if len(matching_user) > 0:
            print("Sisteme başarıyla giriş yaptınız!")
            break
        else:
            print("Geçersiz ad, soyad veya şifre. Lütfen Tekrar deneyin.")
        
#pandas kütüphanesi ile xlsx dosya formatındaki dosyada reset işlemini yapan ekran
def reset():
    data = pd.read_excel("users.xlsx")
    ad = input("Lütfen adınızı girin: ")
    soyad = input("Lütfen soyadınızı girin: ")

    kullanici = data[(data['Ad'] == ad) & (data['Soyad'] == soyad)]
    if input("Sifrenizi öğrenmek ister misiniz? (e/h)") == "E":
        yeni_sifre = input("Yeni şifrenizi girin: ")
        data.loc[(data['Ad'] == ad) & (data['Soyad'] == soyad), 'Şifre'] = yeni_sifre
        data.to_excel("users.xlsx", index=False)
        print("Şifreniz başarıyla güncellendi!")
    else:
        print("Merhaba {} {}, sifreniz: {}".format(ad, soyad, kullanici['Şifre'].values[0]))


sozluk = {"kamuspotu":"---El Ele Türkiye!---"}

sozluk2 = {"uyarimesaj":"Yanlış tuşlama yaptınız! Lütfen tekrar deneyiniz.\n"}

sozluk3 = {"girismesaj":"MERHABA DEPREM MOBİL UYGULAMASINA HOŞ GELDİNİZ."}

sozluk4 = {"bilgimesaj":"\nYeni oturum için geri ana menüye yönlendiriliyorsunuz..."}


#menü icin admin-kullanıcı giris paneli
print(sozluk3["girismesaj"])

x=1
while True:
    x += 1
    giriş = input("PROGRAMA YÖNETİCİ OLARAK GİRİŞ YAPMAK İÇİN 'admin',KULLANICI OLARAK GİRİŞ YAPMAK İÇİN 'kullanıcı' KELİMESİNİ TUŞLAYINIZ: ")
    if giriş == "admin":
        i=1
        while True:
            i+=1
            liste01 = ["\n(2)-> Depremzede yakını bilgisi gir.","(3)-> Kayıp evcil hayvan bilgisi gir.","(4)-> Hasarlı bina bilgisi gir.","(5)-> Gönüllü destekleri bilgileri gir.","(6)-> Deprem bölgesi için yol-trafik bilgisi gir.","(7)-> Ana Menüye Dön.","*Yanlış bir tuşlama yapmanız durumunda tekrardan tuşlama yapmanız istenecektir.\n"]
            for z in liste01:
                print(z)
            vgiriş = input("lütfen uygulamada veri girişi yapılabilen 5 ana başlıktan (2,3,4,5,6) birini veya 'Ana Menüye Dönmek İçin 7'yi tuşlayınız: ")
            if  vgiriş == "2":
                DepremzedeBigileri.kisi_kaydet()
                continue    
            elif vgiriş == "3":
                KayipHayvanBilgisi.h_kaydet()
                continue
            elif vgiriş == "4":
                durum1.durum_ekle()
                continue
            elif vgiriş == "5":
                durum2.durum_ekle()
                continue
            elif vgiriş == "6":
                durum3.durum_ekle()
                continue
            elif vgiriş == "7":
                print("Ana menüye yönlendiriliyorsunuz...")
                break
            else:
                print(sozluk2["uyarimesaj"])
                continue

    elif giriş == "kullanıcı":
        v=1
        while True:
            v+=1
            liste2 = ["Sisteme üye olmak için 1","Sisteme Giriş Yapmak için 2","Şifremi unuttum için 3'ü tuşlayınız."]
            for i in liste2:
                print(i) 
            deger = input("")
            if deger == "1":
                register()
                print("\n")
                govde()
                print(sozluk4["bilgimesaj"])
                break
            elif deger == "2":
                login()
                govde()
                print(sozluk4["bilgimesaj"])
                break
            elif deger == "3":  
                reset()
            else:
                print(sozluk2["uyarimesaj"])
                continue           
    else:
        print(sozluk2["uyarimesaj"])
        continue     

