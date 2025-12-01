const readline = require('readline');

// Kullanıcı girdisi için yardımcı fonksiyon
function prompt(question) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    return new Promise(resolve => rl.question(question, ans => {
        rl.close();
        resolve(ans);
    }));
}

// Özel hata sınıfı
class KuantumCokusuException extends Error {
    constructor(id) {
        super(`Kuantum çöktü! Nesne ${id} patladı!`);
        this.name = "KuantumCokusuException";
    }
}

// Tüm nesnelerin ortak sınıfı
class KuantumNesnesi {
    constructor(id) {
        this.ID = id;
        this._stabilite = 100.0;
        this.tehlikeSeviyesi = Math.floor(Math.random() * 10) + 1;
    }

    get stabilite() {
        return this._stabilite;
    }
    set stabilite(value) {
        if (value < 0) {
            throw new KuantumCokusuException(this.ID);
        } else if (value > 100) {
            this._stabilite = 100;
        } else {
            this._stabilite = value;
        }
    }

    analizEt() {
        throw new Error("AnalizEt soyut metodu");
    }

    durumBilgisi() {
        return `ID: ${this.ID}, Stabilite: ${this.stabilite.toFixed(1)}`;
    }
}

// Güvenli veri nesnesi (Kritik değil)
class VeriPaketi extends KuantumNesnesi {
    analizEt() {
        this.stabilite = this.stabilite - 5;
        console.log("Veri içeriği okundu.");
    }
}

// Tehlikeli nesne (Kritik)
class KaranlikMadde extends KuantumNesnesi {
    analizEt() {
        this.stabilite = this.stabilite - 15;
    }
    acilDurumSogutmasi() {
        this.stabilite = this.stabilite + 50;
        console.log("Soğutma yapıldı, stabilite yenilendi.");
    }
}

// Çok tehlikeli nesne (Kritik)
class AntiMadde extends KuantumNesnesi {
    analizEt() {
        this.stabilite = this.stabilite - 25;
        console.log("Evrenin dokusu titriyor...");
    }
    acilDurumSogutmasi() {
        this.stabilite = this.stabilite + 50;
        console.log("Acil durum soğutması yapıldı, stabilite yenilendi.");
    }
}

async function main() {
    let envanter = [];
    let idCounter = 1;

    while (true) {
        try {
            console.log("\nKUANTUM AMBARI KONTROL PANELİ");
            console.log("1. Yeni Nesne Ekle (Rastgele Veri/Karanlık Madde/Anti Madde üretir)");
            console.log("2. Tüm Envanteri Listele (Durum Raporu)");
            console.log("3. Nesneyi Analiz Et (ID isteyerek)");
            console.log("4. Acil Durum Soğutması Yap (Sadece IKritik olanlar için!)");
            console.log("5. Çıkış");
            let secim = await prompt("Seçiminiz: ");

            if (secim === "1") {
                let tip = Math.floor(Math.random() * 3);
                let yeniId = "N" + idCounter++;
                let nesne;
                if (tip === 0) {
                    nesne = new VeriPaketi(yeniId);
                    console.log(`Yeni VeriPaketi eklendi: ${yeniId}`);
                } else if (tip === 1) {
                    nesne = new KaranlikMadde(yeniId);
                    console.log(`Yeni KaranlıkMadde eklendi: ${yeniId}`);
                } else {
                    nesne = new AntiMadde(yeniId);
                    console.log(`Yeni AntiMadde eklendi: ${yeniId}`);
                }
                envanter.push(nesne);

            } else if (secim === "2") {
                for (let nesne of envanter) {
                    console.log(nesne.durumBilgisi());
                }

            } else if (secim === "3") {
                let araId = await prompt("Analiz edilecek nesne ID: ");
                let bulundu = false;
                for (let nesne of envanter) {
                    if (nesne.ID === araId) {
                        nesne.analizEt();
                        bulundu = true;
                        break;
                    }
                }
                if (!bulundu) {
                    console.log("ID bulunamadı!");
                }

            } else if (secim === "4") {
                let sogutId = await prompt("Soğutulacak nesne ID: ");
                let bulundu = false;
                for (let nesne of envanter) {
                    if (nesne.ID === sogutId) {
                        bulundu = true;
                        if (nesne.acilDurumSogutmasi) {
                            nesne.acilDurumSogutmasi();
                        } else {
                            console.log("Bu nesne soğutulamaz!");
                        }
                        break;
                    }
                }
                if (!bulundu) {
                    console.log("ID bulunamadı!");
                }

            } else if (secim === "5") {
                console.log("Çıkış yapılıyor.");
                break;

            } else {
                console.log("Geçersiz seçim!");
            }

        } catch (e) {
            if (e instanceof KuantumCokusuException) {
                console.log("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR...");
                break;
            } else {
                console.log("Hata:", e.message);
            }
        }
    }
    process.exit();
}

main();
