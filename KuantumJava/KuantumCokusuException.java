// özel istisna sınıfı: stabilite 0 veya altına inince fırlatılır
public class KuantumCokusuException extends Exception {
    public KuantumCokusuException(String id) {
        super("Kuantum çöktü! Nesne " + id + " patladı!");
    }
}
