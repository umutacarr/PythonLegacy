class Urun: # Ana sınıf
    def __init__(self,Urunadi,Fiyat,Stok):# init le özellik ekliyoruz
        self.Urunadi=Urunadi
        self.Fiyat=Fiyat
        self.Stok=Stok

    def urun_bilgisi_goster(self):
        print(f"ürün adi {self.Urunadi},ürün fiyatı {self.Fiyat}, stok bilgisi {self.Stok} ")


    def kalanurunSayisi(self,number):
       sonuc=self.Stok-number

       print(f"kalan stok sayısı {sonuc}")

class Kahve(Urun): #kahve sınıfı Urun sınıfından miras alıyo
    def __init__(self,Urunadi,Fiyat,Stok,Tur,Sıcaklık):#bütün özellikler
        super().__init__(Urunadi,Fiyat,Stok)# miras aldığı özellikler
        self.Tur=Tur#kendi özelliklerini ekliyoruz
        self.Sıcaklık=Sıcaklık
   

    def onerilenBoyut(self):
        print(f"{self.Urunadi} kahvesi orta boy içilmelidir.")

class Tatli(Urun):
    def __init__(self, Urunadi, Fiyat, Stok,Tur,Seker):
        super().__init__(Urunadi, Fiyat, Stok)
        self.Tur=Tur
        self.Seker=Seker

    def diyetdostuMu(self):
        oran=int(input("şeker oranı yüzde kaç olmalı :"))
        if oran <self.Seker:
            print("diyet dostu")
        else:
            print("diyet dostu değildir")

class İcecek(Urun):
    def __init__(self, Urunadi, Fiyat, Stok,İcecektur,Gazli):
        super().__init__(Urunadi, Fiyat, Stok)
        super.İcecektur=İcecektur
        super.Gazli=Gazli

    def ServisTuru(self):
        if self.Gazli==True:
            print("soğuk içilir")
        else:
            print("sıcak içilir")

nesne1=Kahve("Kahve",56,5,"Kahve",78)
nesne1.urun_bilgisi_goster()    
nesne1.onerilenBoyut()

nesne2=Tatli("Baklava",250,50,"Şerbetli",50)
nesne2.urun_bilgisi_goster()
nesne2.diyetdostuMu()

nesne3=Urun("Elma",50,20)
nesne3.urun_bilgisi_goster()
nesne3.kalanurunSayisi(9)
