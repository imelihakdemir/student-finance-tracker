import json

# Verileri dosyadan yükleme fonksiyonu
def verileri_yukle():
    try:
        with open("veri.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        # Dosya henüz yoksa başlangıç değerlerini döndür
        return {"bakiye": 0, "gecmis": []}

# Verileri dosyaya kaydetme fonksiyonu
def verileri_kaydet(bakiye, gecmis):
    veri = {
        "bakiye": bakiye,
        "gecmis": gecmis
    }
    with open("veri.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)

# Program başladığında verileri yükle
veri = verileri_yukle()
bakiye = veri["bakiye"]
gecmis = veri["gecmis"]

while True:
    print("\n=== Öğrenci Finans Takipçisi v3.0 (Kalıcı) ===")
    print("1 - Para ekle")
    print("2 - Harcama ekle")
    print("3 - Bakiyeyi göster")
    print("4 - Bakiyeyi sıfırla")
    print("5 - Harcama geçmişini göster")
    print("6 - Çıkış")

    secim = input("Seçtiğiniz işlemi giriniz: ")

    if secim == '1':
        eklenen = float(input("Eklenecek miktarı girin: "))
        bakiye = bakiye + eklenen
        verileri_kaydet(bakiye, gecmis)  # Değişikliği dosyaya yaz
        print("Para eklendi. Güncel bakiye:", bakiye, "TL")

    elif secim == '2':
        harcama = float(input("Harcama miktarını girin: "))
        aciklama = input("Harcama açıklaması (Örn: Yemek, Dolmuş): ")
        
        bakiye = bakiye - harcama
        
        kayit = aciklama + " -> " + str(harcama) + " TL"
        gecmis.append(kayit)
        
        verileri_kaydet(bakiye, gecmis)  # Değişikliği dosyaya yaz
        print("Harcama kaydedildi. Güncel bakiye:", bakiye, "TL")

    elif secim == '3':
        print("Güncel Bakiyeniz:", bakiye, "TL")

    elif secim == '4':
        bakiye = 0
        gecmis = []
        verileri_kaydet(bakiye, gecmis)  # Sıfırlamayı dosyaya yaz
        print("Bakiyeniz ve geçmişiniz başarıyla sıfırlandı!")

    elif secim == '5':
        print("\n--- HARCAMA GEÇMİŞİ ---")
        if len(gecmis) == 0:
            print("Henüz hiç harcama yapılmadı.")
        else:
            for harcama_kaydi in gecmis:
                print("-", harcama_kaydi)

    elif secim == '6':
        print("Çıkış yapılıyor... Kendine iyi bak!")
        break

    else:
        print("Geçersiz bir seçim yaptınız! Lütfen 1-6 arasında bir sayı girin.")