// tehlikeli nesne (IKritik uygulanır)
public class KaranlikMadde extends KuantumNesnesi implements IKritik {
    public KaranlikMadde(String id) {
        super(id);
    }
    @Override
    public void analizEt() throws KuantumCokusuException {
        setStabilite(getStabilite() - 15);     // stabilite 15 azalır
    }
    @Override
    public void acilDurumSogutmasi() {
        try {
            setStabilite(getStabilite() + 50);
            System.out.println("Soğutma yapıldı, stabilite yenilendi.");
        } catch (KuantumCokusuException e) {
            // 100'den fazla olmaz, hata çıkmaz
        }
    }
}
