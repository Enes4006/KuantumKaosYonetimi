import random
from abc import ABC, abstractmethod

# özel istisna sınıfı: Stabilite < 0 olunca fırlatılır
class KuantumCokusuException(Exception):
    def __init__(self, id):
        super().__init__(f"Kuantum çöktü! Nesne {id} patladı!")


# ===================== ABSTRACT CLASS =====================
class KuantumNesnesi(ABC):
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
            raise KuantumCokusuException(self.ID)
        self._stabilite = min(value, 100.0)

    @abstractmethod
    def analiz_et(self):
        pass

    def durum_bilgisi(self):
        return f"ID: {self.ID}, Stabilite: {self.stabilite:.1f}"


# ===================== INTERFACE (MARKER) =====================
class IKritik:
    def acil_durum_sogutmasi(self):
        raise NotImplementedError


# ===================== SUB CLASSES =====================

class VeriPaketi(KuantumNesnesi):
    def analiz_et(self):
        self.stabilite -= 5
        print("Veri içeriği okundu.")


class KaranlikMadde(KuantumNesnesi, IKritik):
    def analiz_et(self):
        self.stabilite -= 15
        print("Karanlık madde analiz edildi.")

    def acil_durum_sogutmasi(self):
        self.stabilite += 50
        print("Soğutma yapıldı, stabilite yenilendi.")


class AntiMadde(KuantumNesnesi, IKritik):
    def analiz_et(self):
        self.stabilite -= 25
        print("Evrenin dokusu titriyor...")

    def acil_durum_sogutmasi(self):
        self.stabilite += 50
        print("Acil durum soğutması yapıldı, stabilite yenilendi.")


# ===================== MAIN PROGRAM =====================

def main():
    envanter = []
    id_counter = 1

    while True:
        try:
            print("\nKUANTUM AMBARI KONTROL PANELİ")
            print("1. Yeni Nesne Ekle")
            print("2. Envanteri Listele")
            print("3. Nesneyi Analiz Et")
            print("4. Acil Durum Soğutması Yap")
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
                print("Çıkış yapılıyor...")
                break

            else:
                print("Geçersiz seçim!")

        except KuantumCokusuException as e:
            print(e)
            print("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR...")
            break


if __name__ == "__main__":
    main()
