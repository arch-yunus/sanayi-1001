# PLC ve Kumanda Panosu 101 (Industrial Automation & Control Panels)

## 📋 Özet (Executive Summary)
Endüstriyel otomasyonun kalbi, programlanabilir mantıksal denetleyiciler (PLC - Programmable Logic Controller) ve onları çevreleyen kumanda panolarıdır. Bu döküman; röle mantığından modern PLC mimarisine, sensör türlerinden pano içi yerleşime kadar temel kavramları teknik ve pratik yönleriyle ele alır.

---

## ⚡ PLC Nedir ve Neden Kullanılır?
PLC, zorlu fabrika koşullarında (toz, nem, titreşim ve elektriksel gürültü) çalışmak üzere özel olarak tasarlanmış, giriş/çıkış (I/O) birimleri olan bir bilgisayardır.

-   **Mimarisi:** Merkezi İşlem Birimi (CPU), Bellek ve Giriş/Çıkış modüllerinden oluşur.
-   **Çevrim Süresi (Scan Time):** PLC'nin girişleri okuması, programı yürütmesi ve çıkışları güncellemesi arasında geçen süredir; genellikle milisaniye mertebesindedir.

## 🛠️ Kumanda Panosu Bileşenleri
Bir panonun içini açtığınızda görebileceğiniz standart ekipmanlar:

-   **Otomatik Sigorta (Circuit Breaker):** Aşırı akım ve kısa devreye karşı koruma sağlar.
-   **Kontaktör (Contactor):** Elektrik motorları gibi yüksek güç çeken yükleri anahtarlamak için kullanılan elektromanyetik şalterdir. Atölye tabiriyle "Çekti-Bıraktı" yapan cihazdır.
-   **Röle (Relay):** Düşük akımla yüksek akımı kontrol eden, PLC çıkışlarını korumak için kullanılan minyatür anahtardır.
-   **Raylı Terminal (Terminal Block):** Kabloların düzenli bir şekilde bağlanmasını sağlar.

## 📡 Sensör Teknolojileri (Input Devices)
Sistemin "duyu organları":
1.  **Endüktif Sensör:** Sadece metal nesneleri algılar. Atölyede "Metale Bakar" denilir.
2.  **Kapasitif Sensör:** Plastik, sıvı veya katı her türlü maddeyi algılayabilir.
3.  **Optik Sensör:** Işık demetiyle (Fotosel) engel algılar. Mesafe ölçümü veya varlık kontrolünde kritiktir.

## 🏭 Sanayi Gerçeği: "Faz Kaybı" ve "Motor Yanması"
-   **Nedeni:** Üç fazlı (L1, L2, L3) bir motor beslemesinde sigortalardan birinin atması veya bir kablonun kopması sonucu motorun iki fazda kalmasıdır.
-   **Sonucu:** Motor, milini döndürebilmek için kalan iki fazdan aşırı akım çekmeye başlar; sargılar ısınır ve "Yanar".
-   **Mühendislik Çözümü:** Panoya "Faz Koruma Rölesi" eklemek. Fazlardan biri gittiğinde sistemi otomatik olarak durdurur.

## ⚠️ Güvenlik Uyarısı (Safety Warning)
1.  **Ölçüm Yapmadan Dokunma:** Voltajın kesildiğine dair lambalara güvenmeyin; multimetre (avometre) ile her zaman ölçüm yapın (Live-Dead-Live testi).
2.  **Topraklama Şart:** Her pano ve her motor gövdesi mutlaka uygun kesitteki sarı-yeşil topraklama kablosuyla topraklanmalıdır.
3.  **Yüksek Gerilim:** 400V AC (Sanayi Cereyanı), insan kalbini durdurmak için gerekenden binlerce kat daha fazla enerjiye sahiptir!
