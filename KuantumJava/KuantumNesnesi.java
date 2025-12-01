// tüm nesnelerin soyut sınıfı
public abstract class KuantumNesnesi {
    protected String ID;
    private double stabilite;
    protected int tehlikeSeviyesi;

    public KuantumNesnesi(String id) {
        this.ID = id;
        try {
            setStabilite(70.0);
        } catch (KuantumCokusuException e) {
            
        }
        this.tehlikeSeviyesi = (int)(Math.random() * 10) + 1;
    }

    public String getID() { return ID; }
    public double getStabilite() { return stabilite; }

    public void setStabilite(double value) throws KuantumCokusuException {
        if (value < 0) {
            stabilite = 0;
            throw new KuantumCokusuException(ID);
        }
        stabilite = Math.min(value, 70.0);
    }

    public String durumBilgisi() {
        return "ID: " + ID + ", Stabilite: " + stabilite;
    }

    public abstract void analizEt() throws KuantumCokusuException;
}
