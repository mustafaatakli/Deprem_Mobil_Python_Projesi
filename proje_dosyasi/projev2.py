
def vgiriş4():
    #bilgi1 = "Belirttiğiniz adreste .....caddesinde bulunan ....apartmanı depremi hafif hasarla atlatmıştır."
    bilgi = input("Son Durum: ")
    print("son durum guncellenmiştir: ",bilgi)
    return bilgi

    
def vgiriş2():
    durum1 = input("Durumu Giriniz: ")
    print("Guncellenen durum:",isim1,soyisim1,"isimli kişinin durumu",durum1)
    return durum1


def vgiriş6():
    bilgi2 = input("Son Durum: ")
    print("Son Durum Güncellenmiştir.Yeni Son Durum: ",bilgi2)
    return bilgi2

def vgiriş5():
    bilgi3 = input("Durum Güncellemesi: ")
    print("Son Durum Güncellenmiştir.Yeni Son Durum: ",bilgi3)
    return bilgi3


def vgiriş3():
    durum2 = input("Durumu Giriniz: ")
    print("Guncellenen durum: ",hirk,"cinsinli",hrenk,"rengine sahip hayvanınızın durumu: ",durum2)
    return durum2



sozluk = {"kamuspotu":"---El Ele Türkiye!---"}
#print(sozluk["kamuspotu"])


sozluk2 = {"uyarimesaj":"Yanlış tuşlama yaptınız! Lütfen tekrar deneyiniz."}
#print(sozluk2["uyarimesaj"])


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
                sonuc4 = vgiriş4() 
                break      
            elif vgiriş == "6":
                sonuc6 = vgiriş6()
                break
            elif vgiriş == "5":
                sonuc5 = vgiriş5()
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
                    isim2 = input("lutfen isminizi giriniz: ")
                    soyisim2 = input("lutfen soyisminiz giriniz: ")
                    tel2 = input("lutfen tel no giriniz: ")
                    sifre = input("lutfen şifre belirleyiniz:")
                    guvenlik_sorusu = input("En sevdiğiniz rengi yazınız: ")
                    print("\n\nSisteme kaydınız tamamlanmıştır. Sayın",soyisim2,"Sisteme Hoş geldiniz!")
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
                            print(sonuc4)
                            break
                    elif aldeger == "5":
                            print("Yeni guncellenmiş durum açıklaması: ",sonuc5)
                            break
                    elif aldeger == "6":
                            print("Yeni Son Durum: ",sonuc6)
                            break
                    else:
                        print(sozluk2["uyarimesaj"])
                        continue


    elif deger == "2":
        n=1
        while True:
            n += 1
            isim2 = input("lutfen isminizi giriniz: ")
            soyisim2 = input("lutfen soyisminiz giriniz: ")
            tel2 = input("lutfen şifrenizi giriniz: ")
            print("\n\nSisteme kaydınız tamamlanmıştır. Sayın",soyisim2,"Sisteme Hoş geldiniz!")
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
                    demet1 = ('Depremzede yakını bilgisi almak istiyorsanız 1^i tuşlayınız.','Kayıp evcil hayvanınız hakkında bilgi almak için lütfen 2^yi tuşlayınız :')
                    print(demet1[0])
                    print(demet1[1])
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
                    print(sonuc4)
                    break
            elif aldeger == "5":
                    print("Yeni guncellenmiş durum açıklaması: ",sonuc5)
                    break
            elif aldeger == "6":
                    print("Yeni Son Durum: ",sonuc6)
                    break
            else:
                print(sozluk["kamuspotu"])
                continue


    elif deger == "3":    
        cevap1 = input("Şifre güvenlik sorusunun cevabını yazınız: ")
        if cevap1 == guvenlik_sorusu:
            print("Cevap Doğrulanmıştır.")
            yeni_sifre = input("Lütfen yeni şifrenizi giriniz: ")
            yeni_sifre = guvenlik_sorusu
            print("Şifreniz başarıyla değiştirilmiştir.")
    

    else:
        print(sozluk2["uyarimesaj"])
















    