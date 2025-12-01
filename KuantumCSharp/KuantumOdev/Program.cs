using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        List<KuantumNesnesi> envanter = new List<KuantumNesnesi>();
        Random rnd = new Random();
        int idCounter = 1; // yeni nesne ID sayacı

        while (true)
        {
            try
            {
                // menüyü ekrana yazdır
                Console.WriteLine("\n-----------KUANTUM AMBARI KONTROL PANELİ--------------");
                Console.WriteLine("1. Yeni Nesne Ekle (Rastgele Veri/Karanlık Madde/Anti Madde)");
                Console.WriteLine("2. Tüm Envanteri Listele (Durum Raporu)");
                Console.WriteLine("3. Nesneyi Analiz Et (ID)");
                Console.WriteLine("4. Acil Durum Soğutması Yap (Sadece IKritik olanlar için)");
                Console.WriteLine("5. Çıkış");
                Console.Write("Seçiminiz: ");
                int secim = int.Parse(Console.ReadLine());

                switch (secim)
                {
                    case 1: // yeni nesne ekleme
                        
                        int tip = rnd.Next(3);

                        Console.Write("Nesne türü: " + (tip == 0 ? "VeriPaketi" : tip == 1 ? "KaranlikMadde" : "AntiMadde"));

                        KuantumNesnesi nesne;
                        string yeniId = "qu" + idCounter++;
                        if (tip == 0)
                        {
                            nesne = new VeriPaketi(yeniId);
                            Console.WriteLine(" quantum id: " + yeniId);
                        }
                        else if (tip == 1)
                        {
                            nesne = new KaranlikMadde(yeniId);
                            Console.WriteLine(" quantum id: " + yeniId);
                        }
                        else
                        {
                            nesne = new AntiMadde(yeniId);
                            Console.WriteLine(" quantum id: " + yeniId);
                        }
                        envanter.Add(nesne);
                        break;

                    case 2: // durum raporu
                        foreach (var n in envanter)
                        {
                            Console.WriteLine(n.DurumBilgisi());
                        }
                        break;

                    case 3: // nesneyi analiz et
                        Console.Write("Analiz edilecek nesne ID: ");
                        string araId = Console.ReadLine();
                        var nesneAnaliz = envanter.Find(n => n.ID == araId);
                        if (nesneAnaliz != null)
                            nesneAnaliz.AnalizEt();
                        else
                            Console.WriteLine("ID bulunamadı!");
                        break;

                    case 4: // acil durum soğutması
                        Console.Write("Soğutulacak nesne ID: ");
                        string sogutId = Console.ReadLine();
                        var nesneSogut = envanter.Find(n => n.ID == sogutId);
                        if (nesneSogut != null)
                        {
                            if (nesneSogut is IKritik kritikNesne)
                                kritikNesne.AcilDurumSogutmasi();
                            else
                                Console.WriteLine("Bu nesne soğutulamaz!");
                        }
                        else
                        {
                            Console.WriteLine("ID bulunamadı!");
                        }
                        break;

                    case 5: // çıkış
                        return;

                    default:
                        Console.WriteLine("Geçersiz seçim!");
                        break;
                }
            }
            catch (KuantumCokusuException)
            {
                Console.WriteLine("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR...");
                break;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Hata: " + ex.Message);
            }
        }
    }
}
