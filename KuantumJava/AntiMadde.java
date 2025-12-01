// çok tehlikeli nesne (IKritik uygulanır)
public class AntiMadde extends KuantumNesnesi implements IKritik {
    public AntiMadde(String id) {
        super(id);
    }
    @Override
    public void analizEt() throws KuantumCokusuException {
        setStabilite(getStabilite() - 25);
        System.out.println("Evrenin dokusu titriyor...");
    }
    @Override
    public void acilDurumSogutmasi() {
        try {
            setStabilite(getStabilite() + 50);
            System.out.println("Acil durum soğutması yapıldı, stabilite yenilendi.");
        } catch (KuantumCokusuException e) {
            // 100'den fazla olmaz
        }
    }
}
