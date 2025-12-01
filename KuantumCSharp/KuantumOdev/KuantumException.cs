using System;

// özel istisna sınıfı: stabilite 0 veya altına indiğinde fırlatılır
public class KuantumCokusuException : Exception
{
    public KuantumCokusuException(string id)
        : base($"Kuantum çöktü! Nesne {id} patladı!") { }
}
