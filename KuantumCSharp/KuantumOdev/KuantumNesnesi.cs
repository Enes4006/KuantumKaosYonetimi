using System;

// Tüm nesnelerin ortak soyut sınıfı
public abstract class KuantumNesnesi
{
    public string ID { get; set; } // nesne kimliği
    private double stabilite;
    public double Stabilite // 0-100 arasında değer alır
    {
        get { return stabilite; }
        set
        {
            if (value < 0)             // 0'ın altına inerse çöküş
            {
                stabilite = 0;
                throw new KuantumCokusuException(ID);
            }
            stabilite = Math.Min(value, 100.0); // 100'ü aşarsa 100'e sabitlenir
        }
    }
    public int TehlikeSeviyesi { get; set; }     // 1-10 arasında tehlike seviyesi

    // AnalizEt soyut metodu: alt sınıflarda tanımlanacak
    public abstract void AnalizEt();

    // Durum bilgisi: ID ve anlık stabiliteyi döndürür
    public string DurumBilgisi()
    {
        return $"ID: {ID}, Stabilite: {Stabilite:F1}";
    }
}
