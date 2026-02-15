def toplamaIslemi():

    adet = int(input("Toplanacak Veri Miktarını giriniz: "))

    toplam = 0
    for i in range(adet):
        sayi = float(input(f"{i+1}. sayıyı giriniz:"))
        toplam += sayi
    print(f"\ntoplam {adet} adet sayının toplamı: {toplam}")
