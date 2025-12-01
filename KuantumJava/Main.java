import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<KuantumNesnesi> envanter = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        int idCounter = 1;

        while (true) {
            try {
                // menü
                System.out.println("\nKUANTUM AMBARI KONTROL PANELİ");
                System.out.println("1. Yeni Nesne Ekle (Rastgele Veri/Karanlık Madde/Anti Madde üretir)");
                System.out.println("2. Tüm Envanteri Listele (Durum Raporu)");
                System.out.println("3. Nesneyi Analiz Et (ID isteyerek)");
                System.out.println("4. Acil Durum Soğutması Yap (Sadece IKritik olanlar için!)");
                System.out.println("5. Çıkış");
                System.out.print("Seçiminiz: ");
                int secim = Integer.parseInt(scanner.nextLine());

                switch (secim) {
                    case 1: // yeni nesne ekle
                        int tip = new Random().nextInt(3);
                        String yeniId = "qnt" + idCounter++;
                        KuantumNesnesi nesne;
                        if (tip == 0) {
                            nesne = new VeriPaketi(yeniId);
                            System.out.println("Yeni VeriPaketi eklendi: " + yeniId);
                        } else if (tip == 1) {
                            nesne = new KaranlikMadde(yeniId);
                            System.out.println("Yeni KaranlıkMadde eklendi: " + yeniId);
                        } else {
                            nesne = new AntiMadde(yeniId);
                            System.out.println("Yeni AntiMadde eklendi: " + yeniId);
                        }
                        envanter.add(nesne);
                        break;

                    case 2: // listeleme
                        for (KuantumNesnesi nes : envanter) {
                            System.out.println(nes.durumBilgisi());
                        }
                        break;

                    case 3: // analiz et
                        System.out.print("Analiz edilecek nesne ID: ");
                        String araId = scanner.nextLine();
                        boolean bulundu = false;
                        for (KuantumNesnesi nes : envanter) {
                            if (nes.getID().equals(araId)) {
                                nes.analizEt();
                                bulundu = true;
                                break;
                            }
                        }
                        if (!bulundu) {
                            System.out.println("ID bulunamadı!");
                        }
                        break;

                    case 4: // soğutma
                        System.out.print("Soğutulacak nesne ID: ");
                        String sogutId = scanner.nextLine();
                        boolean bulundu2 = false;
                        for (KuantumNesnesi nes : envanter) {
                            if (nes.getID().equals(sogutId)) {
                                bulundu2 = true;
                                if (nes instanceof IKritik) {
                                    ((IKritik) nes).acilDurumSogutmasi();
                                } else {
                                    System.out.println("Bu nesne soğutulamaz!");
                                }
                                break;
                            }
                        }
                        if (!bulundu2) {
                            System.out.println("ID bulunamadı!");
                        }
                        break;

                    case 5: // çıkış
                        System.out.println("Çıkış yapılıyor.");
                        scanner.close();
                        return;

                    default:
                        System.out.println("Geçersiz seçim!");
                        break;
                }
            } catch (KuantumCokusuException ex) {
                System.out.println("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR...");
                break;
            } catch (Exception ex) {
                System.out.println("Hata: " + ex.getMessage());
            }
        }
        scanner.close();
    }
}
