import random

# özel istisna sınıfı: Stabilite < 0 olunca fırlatılır
class KuantumCokusuException(Exception):
    def __init__(self, id):
        super().__init__(f"Kuantum çöktü! Nesne {id} patladı!")

# Tüm nesnelerin ortak sınıfı
# kapsülleme kullanılarak stabilite kontrolü yapılır
class KuantumNesnesi:
    def __init__(self, id):
        self.ID = id
        self._stabilite = 70.0
        self.tehlike_seviyesi = random.randint(1, 10)

    @property
    def stabilite(self):
        return self._stabilite

    @stabilite.setter
    def stabilite(self, value):
        if value < 0:
            # stabilite 0'ın altına düşerse istisna
            raise KuantumCokusuException(self.ID)
        self._stabilite = min(value, 100.0)

    


    def analiz_et(self):
        raise NotImplementedError

    def durum_bilgisi(self):
        return f"ID: {self.ID}, Stabilite: {self.stabilite:.1f}"

# tehlikeli nesneler için işaretleyici sınıf
class IKritik:
    def acil_durum_sogutmasi(self):
        raise NotImplementedError

# güvenli veri nesnesi (IKritik değil)
class VeriPaketi(KuantumNesnesi):
    def analiz_et(self):
        self.stabilite = self.stabilite - 5
        print("Veri içeriği okundu.")

# tehlikeli nesne (IKritik uygulanır)
class KaranlikMadde(KuantumNesnesi, IKritik):
    def analiz_et(self):
        self.stabilite = self.stabilite - 15

    def acil_durum_sogutmasi(self):
        self.stabilite = self.stabilite + 50
        print("Soğutma yapıldı, stabilite yenilendi.")

# çok tehlikeli nesne (IKritik uygulanır)
class AntiMadde(KuantumNesnesi, IKritik):
    def analiz_et(self):
        self.stabilite = self.stabilite - 25
        print("Evrenin dokusu titriyor...")

    def acil_durum_sogutmasi(self):
        self.stabilite = self.stabilite + 50
        print("Acil durum soğutması yapıldı, stabilite yenilendi.")

def main():
    envanter = []
    id_counter = 1

    while True:
        try:
            print("\nKUANTUM AMBARI KONTROL PANELİ")
            print("1. Yeni Nesne Ekle (Rastgele Veri/Karanlık Madde/Anti Madde üretir)")
            print("2. Tüm Envanteri Listele (Durum Raporu)")
            print("3. Nesneyi Analiz Et (ID isteyerek)")
            print("4. Acil Durum Soğutması Yap (Sadece IKritik olanlar için!)")
            print("5. Çıkış")
            secim = input("Seçiminiz: ")

            if secim == "1":
                tip = random.randint(0, 2)
                yeni_id = f"q{id_counter}"
                id_counter += 1
                if tip == 0:
                    nesne = VeriPaketi(yeni_id)
                    print(f"Yeni VeriPaketi eklendi: {yeni_id}")
                elif tip == 1:
                    nesne = KaranlikMadde(yeni_id)
                    print(f"Yeni KaranlıkMadde eklendi: {yeni_id}")
                else:
                    nesne = AntiMadde(yeni_id)
                    print(f"Yeni AntiMadde eklendi: {yeni_id}")
                envanter.append(nesne)

            elif secim == "2":
                for nesne in envanter:
                    print(nesne.durum_bilgisi())

            elif secim == "3":
                ara_id = input("Analiz edilecek nesne ID: ")
                found = False
                for nesne in envanter:
                    if nesne.ID == ara_id:
                        nesne.analiz_et()
                        found = True
                        break
                if not found:
                    print("ID bulunamadı!")

            elif secim == "4":
                sogut_id = input("Soğutulacak nesne ID: ")
                found = False
                for nesne in envanter:
                    if nesne.ID == sogut_id:
                        found = True
                        if isinstance(nesne, IKritik):
                            nesne.acil_durum_sogutmasi()
                        else:
                            print("Bu nesne soğutulamaz!")
                        break
                if not found:
                    print("ID bulunamadı!")

            elif secim == "5":
                print("Çıkış yapılıyor.")
                break

            else:
                print("Geçersiz seçim!")

        except KuantumCokusuException:
            print("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR...")
            break

if __name__ == "__main__":
    main()
