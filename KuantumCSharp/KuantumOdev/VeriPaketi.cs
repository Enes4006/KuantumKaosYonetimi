using System;

// güvenli veri nesnesi (Kritik değil)
public class VeriPaketi : KuantumNesnesi
{
    public VeriPaketi(string id)
    {
        ID = id;
        Stabilite = 70.0;                           // örnek başlangıç stabilitesi
        TehlikeSeviyesi = new Random().Next(1, 11);  // 1-10 rastgele değer
    }

    public override void AnalizEt()
    {
        Stabilite -= 5;                              // stabilite 5 azalır
        Console.WriteLine("Veri içeriği okundu.");   
    }
}
