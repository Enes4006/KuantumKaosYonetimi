# ⚛ Kuantum Kaos Yönetimi (Quantum Chaos Management)

Bu proje, nesne yönelimli programlama (OOP) prensipleri kullanılarak geliştirilmiş bir konsol tabanlı simülasyon uygulamasıdır. Amaç, farklı türdeki kuantum nesnelerinin stabilitelerini kontrol etmek, tehlike durumlarını yönetmek ve sistem çöküşünü önlemektir.

Proje; **abstract class, encapsulation, inheritance, polymorphism, interface ve exception handling** gibi OOP kavramlarının gerçekçi bir senaryo üzerinden uygulanmasını hedeflemektedir.

---

## 🧠 Projenin Amacı

Kuantum nesnelerinin stabilitelerini izleyen, analiz eden ve gerekli durumlarda acil müdahale yapan bir sistem tasarlamak.

Sistemde üç farklı nesne türü bulunmaktadır:

- **VeriPaketi** → Düşük riskli, stabiliteyı yavaş azaltır
- **KaranlikMadde** → Orta riskli, stabiliteyi daha fazla düşürür
- **AntiMadde** → Çok yüksek riskli, en fazla zarar verir

Stabilite değeri 0'ın altına düşerse **Kuantum Çöküşü (Exception)** meydana gelir ve sistem kapanır.

---

## 🔧 Kullanılan OOP Kavramları

| Kavram | Açıklama |
|------|------|
| Abstract Class | `KuantumNesnesi` soyut sınıf olarak tanımlandı |
| Encapsulation | `stabilite` değişkeni private yapılıp property ile korundu |
| Inheritance | Tüm nesneler `KuantumNesnesi` sınıfından türedi |
| Polymorphism | `analiz_et()` her sınıfta farklı şekilde işlendi |
| Interface (Marker) | `IKritik` ile tehlikeli nesneler belirlendi |
| Exception Handling | `KuantumCokusuException` üretildi |

---

## 🧩 Geliştirme Sürecinde Karşılaşılan Zorluklar

- Abstract class ve interface yapılarını doğru şekilde kurmak
- Stabilite kontrolünü kapsülleme ile sağlamak
- Tüm dillerde aynı mantığı korumak
- Exception yapısını senaryoya uygulatmak
- Çoklu sınıf yapısını düzenli tutmak

Bu süreç sayesinde OOP mantığı çok daha iyi kavranmıştır.

---
