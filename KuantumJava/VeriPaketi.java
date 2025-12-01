// güvenli veri nesnesi (IKritik değil)
public class VeriPaketi extends KuantumNesnesi {
    public VeriPaketi(String id) {
        super(id);
    }
    @Override
    public void analizEt() throws KuantumCokusuException {
        setStabilite(getStabilite() - 5);      // stabilite 5 azalır
        System.out.println("Veri içeriği okundu.");
    }
}
