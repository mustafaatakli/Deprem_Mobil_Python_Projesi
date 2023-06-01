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
                print(sozluk["kamuspotu"])
                print(bilgi1)
                break
        elif aldeger == "2":
                demet0 = ('Depremzede yakını bilgisi almak istiyorsanız 1^i tuşlayınız.','Kayıp evcil hayvanınız hakkında bilgi almak için lütfen 2^yi tuşlayınız :')
                print(demet0[0])
                print(demet0[1])
                soru_bilgi = input()
                k=1
                while True:
                    k += 1
                    if soru_bilgi == "1":
                        isim11 = input("Yakını olduğunuz depremzedenin ismini giriniz: ")
                        soyisim11 = input("Yakını olduğunuz depremzedenin soyismini giriniz: ")
                        if isim11 == isim1 and soyisim11 == soyisim1:
                            print(isim11,soyisim11,"isimli kişinin durumu: ",sonuc2)
                            break      
                    elif soru_bilgi == "2":
                        hirk1 = input("Evcil hayvanınız cinsini giriniz: ")
                        hrenk1 = input("Evcil hayvanınızın rengini giriniz: ")
                        if hirk1 == hirk and hrenk1 == hrenk:
                            print(hirk1,"ırkına sahip",hrenk1,"renkli","evcil hayvanınızın durumu: ",sonuc3)
                            break
        
                            break   
                        else:
                            print(sozluk2["uyarimesaj"])
                            continue
    
        elif aldeger == "3":
                soru10 = input("Sizlere daha etkin ve hızlı yardımcı olabilmemiz adına ihtiyaç taleplerinizi bu ekrandan bizimle yazılı olarak paylaşır mısınız? \n")
                print("Talepleriniz alınmış olup en kısa zamanda tarafınıza aktarılacaktır.")
                print(sozluk["kamuspotu"])
                break
        elif aldeger == "4": 
                read_status()
                #print(sonuc4)
                break
        elif aldeger == "5":
                durum_oku()
                #print("Yeni guncellenmiş durum açıklaması: ",sonuc5)
                break
        elif aldeger == "6":
                durum_okuv3()
                #print("Yeni Son Durum: ",sonuc6)
                break
        else:
            print(sozluk2["uyarimesaj"])
            continue



#Sqlite3 ile oluşturduğum depremde hasar alan binaların kaydedildiği veritabanı('database.db')
import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Durumlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            durum TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_status():
    status = input("Durumunuzu girin: ")

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Durumlar (durum) VALUES (?)', (status,))
    conn.commit()

    print("Durum kaydedildi!")

    conn.close()

def read_status():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Durumlar')
    rows = cursor.fetchall()

    if len(rows) > 0:
        print("Durumlar:")
        for row in rows:
            print(f"Durum ID: {row[0]}, Durum: {row[1]}")
    else:
        print("Kaydedilmiş bir durum bulunmamaktadır.")

    conn.close()

create_table()



#Sqlite3 ile oluşturduğum deprem bölgesine gidecek gönüllüler hakkında bilgilerin veritabanı('databasev2.db')
import sqlite3

def tablo_olustur():
    conn = sqlite3.connect('databasev2.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Durumlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            durum TEXT
        )
    ''')

    conn.commit()
    conn.close()

def durum_ekle():
    status = input("Durumunuzu girin: ")

    conn = sqlite3.connect('databasev2.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Durumlar (durum) VALUES (?)', (status,))
    conn.commit()

    print("Durum kaydedildi!")

    conn.close()

def durum_oku():
    conn = sqlite3.connect('databasev2.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Durumlar')
    rows = cursor.fetchall()

    if len(rows) > 0:
        print("Durumlar:")
        for row in rows:
            print(f"Durum ID: {row[0]}, Durum: {row[1]}")
    else:
        print("Kaydedilmiş bir durum bulunmamaktadır.")

    conn.close()

tablo_olustur()


#Sqlite3 ile oluşturduğum, deprem bölgesine gidecek araçlara yollar hakkında bilgilerin veritabanı('databasev3.db')
import sqlite3

def tablo_olusturv3():
    conn = sqlite3.connect('databasev3.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Durumlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            durum TEXT
        )
    ''')

    conn.commit()
    conn.close()

def durum_eklev3():
    status = input("Yol-Trafik Durumunu Girin: ")

    conn = sqlite3.connect('databasev3.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Durumlar (durum) VALUES (?)', (status,))
    conn.commit()

    print("Durum kaydedildi!")

    conn.close()

def durum_okuv3():
    conn = sqlite3.connect('databasev3.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Durumlar')
    rows = cursor.fetchall()

    if len(rows) > 0:
        print("Durumlar:")
        for row in rows:
            print(f"Durum ID: {row[0]}, Durum: {row[1]}")
    else:
        print("Kaydedilmiş bir durum bulunmamaktadır.")

    conn.close()

tablo_olusturv3()



#depremzede durum bilgisi save ve read fonksiyonu
def vgiriş2():
    durum1 = input("Durumu Giriniz: ")
    print("Guncellenen durum:",isim1,soyisim1,"isimli kişinin durumu",durum1)
    return durum1
#kayıp hayvan bilgi fonksiyonu
def vgiriş3():
    durum2 = input("Durumu Giriniz: ")
    print("Guncellenen durum: ",hirk,"cinsinli",hrenk,"rengine sahip hayvanınızın durumu: ",durum2)
    return durum2



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
#register()

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
#login()
        
#pandas kütüphanesi ile xlsx dosya formatındaki dosyada reset işlemini yapan ekran
def reset():
    data = pd.read_excel("users.xlsx")
    ad = input("Lütfen adınızı girin: ")
    soyad = input("Lütfen soyadınızı girin: ")

    kullanici = data[(data['Ad'] == ad) & (data['Soyad'] == soyad)]
    if input("Sifrenizi öğrenmek ister misiniz? (E/H)") == "E":
        yeni_sifre = input("Yeni şifrenizi girin: ")
        data.loc[(data['Ad'] == ad) & (data['Soyad'] == soyad), 'Şifre'] = yeni_sifre
        data.to_excel("users.xlsx", index=False)
        print("Şifreniz başarıyla güncellendi!")
    else:
        print("Merhaba {} {}, sifreniz: {}".format(ad, soyad, kullanici['Şifre'].values[0]))
#reset()



sozluk = {"kamuspotu":"---El Ele Türkiye!---"}

sozluk2 = {"uyarimesaj":"Yanlış tuşlama yaptınız! Lütfen tekrar deneyiniz."}

sozluk3 = {"girismesaj":"MERHABA DEPREM MOBİL UYGULAMASINA HOŞ GELDİNİZ."}

print(sozluk3["girismesaj"])

x=1
while True:
    x += 1
    giriş = input("PROGRAMA YÖNETİCİ OLARAK GİRİŞ YAPMAK İÇİN 'admin',KULLANICI OLARAK GİRİŞ YAPMAK İÇİN 'kullanıcı' KELİMESİNİ TUŞLAYINIZ: ")
    if giriş == "admin":
        i=1
        while True:
            i+=1
            liste01 = ["\n(2)-> Depremzede yakını bilgisi gir.","(3)-> Kayıp evcil hayvan bilgisi gir.","(4)-> Hasarlı bina bilgisi gir.","(5)-> Gönüllü destekleri bilgileri gir.","(6)-> Deprem bölgesi için yol-trafik bilgisi gir."]
            for z in liste01:
                print(z)
            vgiriş = input("uygulamada veri girişi yapılabilen 5 ana başlıktan (2,3,4,5,6) lütfen birini tuşlayınız: ")
            if  vgiriş == "2":
                isim1 = input("İsim: ")
                soyisim1 = input("Soyisim: ")
                sonuc2 = vgiriş2()
                break
            elif vgiriş == "3":
                hirk = input("Kurtarılan evcil hayvanın cinsini giriniz: ")
                hrenk = input("Kurtarılan evcil hayvanın rengini giriniz: ")
                sonuc3 = vgiriş3()
                break
            elif vgiriş == "4":
                insert_status()
                break      
            elif vgiriş == "6":
                durum_eklev3()
                break
            elif vgiriş == "5":
                durum_ekle()
                break
            else:
                print(sozluk2["uyarimesaj"])
                continue

    elif giriş == "kullanıcı":
       
        liste2 = ["Sisteme üye olmak için 1","Sisteme Giriş Yapmak için 2","Şifremi unuttum için 3'ü tuşlayınız."]
        for i in liste2:
            print(i) 
    deger = input("")
    if deger == "1":
                j=1
                while True:
                    j += 1
                    register()
                    break
                    govde()
                    break

    elif deger == "2":
        n=1
        while True:
            n += 1
            login()
            govde()
            break
    elif deger == "3":  
        
        reset()
    else:
        print(sozluk2["uyarimesaj"])

    
