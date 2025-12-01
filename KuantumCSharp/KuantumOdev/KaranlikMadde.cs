using System;

// tehlikeli nesne (IKritik uygulanır)
public class KaranlikMadde : KuantumNesnesi, IKritik
{
    public KaranlikMadde(string id)
    {
        ID = id;
        Stabilite = 70.0; // örnek başlangıç stabilitesi
        TehlikeSeviyesi = new Random().Next(1, 11);
    }

    public override void AnalizEt()
    {
        Stabilite -= 15; // stabilite 15 birim düşer
    }

    public void AcilDurumSogutmasi()
    {
        Stabilite += 50;
        Console.WriteLine("Soğutma yapıldı, stabilite yenilendi.");
    }
}
