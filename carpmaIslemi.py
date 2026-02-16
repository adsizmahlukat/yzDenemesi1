def carpmaIslemi():
    # Kullanıcıdan kaç adet sayı çarpılacağını alıyoruz
    adet = int(input("Çarpılacak Veri Miktarını giriniz: "))

    # Çarpmada etkisiz eleman 1 olduğu için başlangıç değerini 1 yapıyoruz
    sonuc = 1

    for i in range(adet):
        sayi = float(input(f"{i + 1}. sayıyı giriniz: "))
        sonuc *= sayi  # sonuc = sonuc * sayi

    print(f"\nToplam {adet} adet sayının çarpımı: {sonuc}")
