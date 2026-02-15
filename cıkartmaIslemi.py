def cikarmaIslemi():
    adet = int(input("Kaç adet sayı?: "))
    sonuc = float(input("1. sayıyı giriniz: "))

    for i in range(1, adet):
        sayi = float(input(f"{i + 1}. sayıyı giriniz: "))
        sonuc -= sayi

    # Buradaki boşluğa dikkat! 'def'in içinde ama 'for'un dışında olmalı.
    print(f"\nİşlem sonucu {sonuc}.")
