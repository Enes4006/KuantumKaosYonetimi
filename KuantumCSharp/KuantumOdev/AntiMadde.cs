using System;

// çok tehlikeli nesne (IKritik uygulanır)
public class AntiMadde : KuantumNesnesi, IKritik
{
    public AntiMadde(string id)
    {
        ID = id;
        Stabilite = 70.0; // örnek başlangıç stabilitesi
        TehlikeSeviyesi = new Random().Next(1, 11);
    }

    public override void AnalizEt()
    {
        Stabilite -= 25;
        Console.WriteLine("Evrenin dokusu titriyor..."); 
    }

    public void AcilDurumSogutmasi()
    {
        Stabilite += 50;
        Console.WriteLine("Acil durum soğutması yapıldı, stabilite yenilendi.");
    }
}
