with open("Merhaba.txt", "r", encoding="utf-8") as f:
    icerik = f.read()

import time
import sys

print("Yükleniyor", end="") # Alt satıra geçme dedik

for i in range(3):
    time.sleep(0.5)      # yarım saniye bekle
    print(".", end="")   # yanına nokta koy
    sys.stdout.flush()   # terminali anında güncellemeye zorla
print("\n")
print(icerik)










def guzel_sozcukler_iste(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            #Virgülleri temizle ve kelimeleri listeye al
            sozcukler = [s.strip().lower() for s in icerik.split(",")]
            return sozcukler
    except FileNotFoundError:
        print(f"Hata: {dosya_adi} dosyası bulunamadı!")
        return []

def veritabanini_yukle(dosya_adi):
    kategori_sozlugu = {}
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            if "|" in satir:
                sol_taraf, kategori = satir.strip().split("|") # .strip() ekledik
                # Burası önemli: Virgülle bölmelisin!
                kelimeler = [k.strip().lower() for k in sol_taraf.split(",")]

                for kelime in kelimeler:
                    kategori_sozlugu[kelime] = kategori
    return kategori_sozlugu

#CEVAP HAVUZU

cevaplar = {
    "MOTİVASYON": "İnan bana, senin bu enerjinle her şey mümkün!",
    "SELAMLAMA": "Merhaba! Seninle tekrar konuşmak ne güzel.",
    "TEŞEKKÜR": "Asıl ben teşekkür ederim, senin gibi nazik biriyle sohbet etmek harika."
}

import toplamaIslemi

def sohbet_botu():
    # 1. Önce veritabanını (sözlüğü) yüklüyoruz.
    # Dosya adının "Veritabanı.txt" (veya senin verdiğin ad) olduğundan emin ol.
    veritabani = veritabanini_yukle("GüzelSözcükler.txt")

    print("Merhaba! Delirmek üzereyim! EVET! BENİ KODLAYAN ZAVALLI DELİRMEK ÜZERE! HAHAHAHAHAH!! ÇIKIŞ İÇİN 'Q' TUŞUNA BAS")


    while True:
        mesaj = input("Siz: ").lower()

        if mesaj == "q":
            print("Görüşürüz!")
            break

        if "topla" in mesaj or "toplama işemi yapmak istiyorum" in mesaj:
            print("Elbette!")
            toplamaIslemi.toplamaIslemi()
            continue

        #KONTROL NOKTASI
        bulunan_kategori = None
        tespit_edilen_kelime = ""

        # 2. Döngüyü sözlüğün anahtarları (kelimeler) üzerinde kuruyoruz
        for kelime in veritabani:
            if kelime in mesaj:
                # Eğer kelimeyi bulursak, onun kategorisini alıyoruz
                bulunan_kategori = veritabani[kelime]
                tespit_edilen_kelime = kelime
                break #BİR TANE BULMAMIZ YETERLİ



        #YANIT MEKANİZMASI
        if bulunan_kategori:
            # Eğer kategori cevaplar sözlüğümüzde varsa oradaki cümleyi çekiyoruz
            # Eğer o kategoriye özel cevap yoksa genel bir cevap veriyoruz
            cevap = cevaplar.get(bulunan_kategori, "Çok naziksiniz, teşekkürler!")
            print(f"Bot:{cevap}")
        else:
            print("Üzüldüm...(Anlayamadım)")
sohbet_botu()







