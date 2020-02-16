# EV GİDERLERİ TAKİP PROGRAMI
class Pazar:
    def __init__(self):
        self.islem_tarihi=input("İşlem Tarihini Giriniz :")
        self.bakiye=0
        # veri tabanına bağlanma için fonksiyon
    def baglan(self):
        import sqlite3
        self.vt=sqlite3.connect("gider.sqlite")
        self.im=self.vt.cursor()
        return sqlite3,self.vt,self.im
    # gider adında bir tablo oluşturalım
    def olustur(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS gider ("İşlem Tarihi",
                        "Fatura Tutarı","Son Ödeme Tarihi","Ödeme","Gün Sayısı",
                        "Sarfiyat","Ortalama Fiyat","Ortalama Sariyat","Bakiye")""")
        self.vt.commit()
    # data çağırma fonksiyonu tanımlayalım
    def cagir(self):
        self.im.execute("""SELECT * FROM gider""")
        data=self.im.fetchall()        
        return data
    # Fatura işleme fonksiyonu yazalım
    def fatura(self):
        self.fatura_tutari=float(input("Fatura Tutarını Giriniz :"))
        self.son_odeme_tarihi=input("Son Ödeme Tarihini Giriniz :")
        self.odeme=0
        self.gun_sayisi=int(input("Gün Sayısını Giriniz :"))
        self.sarfiyat=float(input("Sarfiyat Miktarını Giriniz :"))
        self.ortalama_fiyat=self.fatura_tutari/self.gun_sayisi
        self.ortalama_sarfiyat=self.sarfiyat/self.gun_sayisi
        if self.bakiye==0:            
            self.bakiye=self.bakiye+self.fatura_tutari
        else:
            self.bakiye=data[-1][-1]
        degisken=[self.islem_tarihi,self.fatura_tutari,
                  self.son_odeme_tarihi,self.odeme,self.gun_sayisi,
                  self.sarfiyat,self.ortalama_fiyat,
                  self.ortalama_sarfiyat,self.bakiye]
        self.im.execute("""INSERT INTO gider VALUES(?,?,?,?,?,?,?,?,?)""",degisken)
        self.vt.commit()
    # Ödeme fonksiyonu yazdıralım
    def odeme(self):        
        self.fatura_tutari=0
        self.son_odeme_tarihi=""
        self.odeme=float(input("Ödeme Tutarını Giriniz :"))        
        self.gun_sayisi=None
        self.sarfiyat=None
        self.ortalama_fiyat=None
        self.ortalama_sarfiyat=None
        Bakiye=(self.cagir()[-1][-1])       
        self.bakiye=Bakiye-self.odeme
        degisken=[self.islem_tarihi,self.fatura_tutari,
                  self.son_odeme_tarihi,self.odeme,self.gun_sayisi,
                  self.sarfiyat,self.ortalama_fiyat,
                  self.ortalama_sarfiyat,self.bakiye]
        self.im.execute("""INSERT INTO gider VALUES(?,?,?,?,?,?,?,?,?)""",degisken)
        self.vt.commit()
    # veri tablosu yazdırma fonksiyonu yazalım
    def yazdir(self):
        self.im.execute("""SELECT * FROM gider""")
        data=self.im.fetchall()
        print("data =",data)
        self.vt.close()        
#ornek=Pazar()
#ornek.baglan()
#ornek.olustur()
#ornek.fatura()
#print(ornek.cagir())
#print(ornek.cagir()[-1][-1])
#ornek.odeme()        
#print(ornek.cagir())
#ornek.yazdir()
import sys
print(sys.path)
        
        
        
