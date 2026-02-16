def bolmeIslemi():
    adet = int(input("Kaç adet sayı birbiriyle bölünecek?: "))

    # İlk sayıyı döngüden ÖNCE alıyoruz çünkü bu "bölünen" sayıdır.
    sonuc = float(input("1. sayıyı (bölünen) giriniz: "))

    # Döngü 1'den başlamalı (Çünkü 1. sayıyı yukarıda aldık)
    for i in range(1, adet):
        sayi = float(input(f"{i + 1}. sayıyı (bölen) giriniz: "))

        # Sıfıra bölme kontrolü
        if sayi == 0:
            print("Hata: Bir sayı 0'a bölünemez!")
            return  # Fonksiyonu burada bitir

        sonuc /= sayi  # sonuc = sonuc / sayi

    print(f"\nİşlem sonucu: {sonuc}")