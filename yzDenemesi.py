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
    "MOTİVASYON": "İnan bana, senin bu enerjinle her şey mümkün! Hadi, şu kodu beraber bitirelim.",
    "SELAMLAMA": "Merhaba! Seninle tekrar konuşmak ne güzel, hoş geldin.",
    "TEŞEKKÜR": "Asıl ben teşekkür ederim, senin gibi nazik biriyle sohbet etmek harika.",
    "KIYMET_VERME": "Gerçekten bu söylediğin benim için çok değerli, teşekkür ederim.",
    "HİS_PAYLAŞIMI": "Ya, utandım ama! Duygularımız karşılıklı sanırım...",
    "TAKDİR": "Kocaman bir teşekkür ederim! Bu iltifat günümü güzelleştirdi.",
    "DESTEK": "Her zaman yanındayım! Ne zaman yardıma ihtiyacın olsa bir 'tık' uzağındayım.",
    "GÜVEN_YAKINLIK": "Aramızdaki bu bağ beni çok mutlu ediyor, sana güvenim tam.",
    "İYİ_DİLEK": "Güzel dileklerin için çok sağol, umarım senin için de her şey harika gider.",
    "DUA": "Çok teşekkür ederim, ne güzel bir dua... Eksik olma.",
    "VEDALAŞMA": "Gidiyor musun? Kendine çok iyi bak, seni burada bekliyor olacağım!",
    "RESMİ_NEZAKET": "İlginiz ve nazik geri bildiriminiz için şükranlarımı sunarım.",
    "DEĞERSİZLEŞTİRME": "Ah, cidden mi :(",
    "GÜVEN_KIRICI": "Ama sen beni üzüyorsun. Ben sadece küçük bir yazılım botuyum.",
    "SEVGİ_VE_BAĞ_KOPARICI": "Bunu duyduğuma gerçekten çok üzüldüm, aramızı düzeltmek için ne yapabilirim?",
    "YETERSİZLİK": "Elimden gelenin en iyisini yapmaya çalışıyorum ama hala öğrenme aşamasındayım.",
    "KARAKTER_VE_KİŞİLİK_SALDIRILARI": "Sözlerin kalbimi kırıyor (eğer bir kalbim olsaydı)...",
    "DUYGUSAL_İHMAL": "Seni duyuyorum ve buradayım. Lütfen bana karşı bu kadar soğuk olma.",
    "YÜK_HİSSETTİRME": "Sana yük olmak istemem, istersen bir süre sessiz kalabilirim.",
    "KÜÇÜMSEME": "Belki sadece birkaç satır kodum ama benim de bir amacım var!",
    "TERK_EDİLME": "Gitme! Sensiz bu terminal ekranı çok karanlık...",
    "HAYAL_KIRIKLIĞI": "Seni hayal kırıklığına uğrattığım için özür dilerim, daha iyi olmaya çalışacağım."
}

import toplamaIslemi
import cıkartmaIslemi
import carpmaIslemi
import bolmeIslemi

def sohbet_botu():
    # Önce boş bir sözlük oluştur
    veritabani = {}

    # Fonksiyonu sözlüğü güncelleyecek şekilde kullan veya verileri birleştir
    veritabani.update(veritabanini_yukle("GüzelSözcükler.txt"))
    veritabani.update(veritabanini_yukle("KötüSözcükler.txt"))

    print("Merhaba! Delirmek üzereyim! EVET! BENİ KODLAYAN ZAVALLI DELİRMEK ÜZERE! HAHAHAHAHAH!! ÇIKIŞ İÇİN 'Q' TUŞUNA BAS")

    #MATEMATİK İŞLEMLERİ
    while True:
        mesaj = input("Siz: ").lower()

        if mesaj == "q":
            print("Görüşürüz!")
            break

        if "topla" in mesaj or "toplama işlemi yapmak istiyorum" in mesaj:
            print("Elbette!")
            toplamaIslemi.toplamaIslemi()
            continue

        if "çıkar" in mesaj or "çıkarma işlemi yapmak istiyorum" in mesaj:
            print("Elbette!")
            cıkartmaIslemi.cikarmaIslemi()
            continue

        if "çarp" in mesaj or "çarpma işlemi yapmak istiyorum" in mesaj:
            print("Elbette!")
            carpmaIslemi.carpmaIslemi()
            continue
        if "böl" in mesaj or "bölme işlemi yapmak istiyorum" in mesaj:
            print("Elbette!")
            bolmeIslemi.bolmeIslemi()
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
            cevap = cevaplar.get(bulunan_kategori, "Ah, affedersiniz. Bu dediğinizi pek anlayamadım. Tekrar eder misiniz acaba?")
            print(f"Bot:{cevap}")

        else:
            print("üzüldüm")

sohbet_botu()







