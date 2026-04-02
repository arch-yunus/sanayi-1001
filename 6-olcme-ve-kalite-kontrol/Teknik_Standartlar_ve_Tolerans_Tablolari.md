# Teknik Standartlar ve Tolerans Tabloları (Engineering Standards & Tolerances)

## 🎯 TL;DR (Yönetici Özeti)
Sanayi bağımsız bir yapı değil, global standartlara (ISO, DIN, ANSI) bağlı entegre bir sistemdir. Bir civatanın dişi Tokyo'da da, Stuttgart'ta da, Bursa'daki bir atölyede de aynı matematiksel dile sahiptir. Bu döküman; geçme toleransları (H7, g6 gibi), yüzey pürüzlülük normları ve geometrik boyutlandırma (GD&T) kurallarını, yani sanayinin "Evrensel Anayasasını" belgeler. "Kitabına uygun iş yapmak", kitabın standartlarını bilmekle başlar.

---

## ⚙️ Toleransların Dili: ISO Sistematiği

### 1️⃣ Mil ve Delik Geçme Toleransları (ISO Fits)
Üretime yön veren tolerans sınıfları, büyük ve küçük harflerle (Delikler için Büyük (H), Miller için küçük (h)) uluslararası olarak kodlanmıştır.

*   **H7 / h6 (Kaygan Geçme - Sliding Fit):** Boşluk yoka yakındır, parçalar ince bir yağ filmi üzerinde elle kaydırılabilir. Freze veya torna milinin rulman yatağı bu standartta işlenir.
*   **H7 / g6 (Boşluklu Geçme - Clearance Fit):** Rahatça hareket etmesi gereken, ısınma payının bırakıldığı sistemler (Örn: Piston ve silindir gömleği arasındaki yataklama).
*   **H7 / p6 (Sıkı Geçme - Interference Fit):** Boşluk "eksi" (-) değerdedir. Mil delikten daha kalındır. Parça hidrolik presle veya dış parça (delik) ısıtılarak (genleştirme) takılabilir. Genellikle rulmanların mile çakılmasında kullanılır.

### 2️⃣ Geometrik Boyutlandırma ve Toleranslandırma (GD&T)
Klasik "çap 50mm olsun" tanımının ötesinde, parçanın 3 boyutlu uzayda tam olarak nasıl davranması gerektiğini tanımlayan global sembollerdir.

*   **⚪ Salgı Daireselliği (Circular Runout):** Bir parça kendi ekseni etrafında dönerken yüzeyinin merkez eksenine göre oynama (salgı) miktarı (Örn: Krank mili yatakları).
*   **// Paralellik (Parallelism):** İki yüzeyin uzayda birbirine olan mesafesinin, belirlenen tolerans bölgesi içinde (Örn: 0.01mm) kusursuz paralel kalması.
*   **⟂ Diklik (Perpendicularity):** İki yüzey arasındaki açının mikron hassasiyetinde tam 90° olması (Örn: Gönye hataları).
*   **◎ Eşmerkezlilik (Concentricity):** İç içe geçmiş veya farklı çaplardaki silindirlerin tam olarak aynı eksen (merkez) etrafında dönebilirliği.

### 3️⃣ Yüzey Pürüzlülüğü (Surface Roughness - Ra)
Yüzeyin mikroskobik olarak ne kadar "dağlı-tepeli" olduğunun metrik ölçüsüdür.
*   **Ra 3.2 - 6.3:** Normal tornalama veya frezeleme yüzeyi. Fonksiyonel olmayan yüzeyler için yeterlidir.
*   **Ra 0.8 - 1.6:** Hassas tornalama veya taşlama gerektirir. Sızdırmazlık yüzeylerinin (conta oturma yeri) minimum pürüzlülüğüdür.
*   **Ra 0.1 - 0.4:** "Ayna yüzey". Honlama veya lepleme (laping) gerekir. Yüksek hızda çalışan rulman yatakları ve hidrolik piston yüzeyleri.

---

## 🛠️ Atölye Gerçekleri ve Standartların Çarpışması
"Tolerans kağıt üzerinde kolaydır, mengeneye bağlayınca terletir."

| Standart Kodu | Usta Tabiri | Tezgaha Yansıma Maliyeti |
| :--- | :--- | :--- |
| **H7/g6** | Tatlı Geçme / Tatlı Sıkı | CNC torna ile standart işleme. Maliyet: 1x |
| **IT4 (0.005mm)** | Binde Beş | Dış silindirik taşlama tezgahı şarttır. Taşlama ustasına ihtiyaç vardır. Maliyet: 3x |
| **Ra 0.2** | Ayna Yüzey | Tel erozyon (Ince ayar) veya Laping gerekir. Çok uzun sürer. Maliyet: 5x |

**Stratejik Tavsiye:** "Bir mühendis olarak teknik resme 'H5 tolerans' yazması 2 saniye sürer. Ancak o toleransı atölyede tutturmak, ortamın sıcaklığından kesme sıvısının kalitesine kadar günlerce sürecek bir optimize (maliyet) demektir. Gereksiz hassasiyet, en büyük israftır."

---

## 💻 Dijital Entegrasyon (CMM & Model Based Definition)
Teknik resimler artık kağıttan, 3D datanın içine taşınmaktadır.

1.  **MBD (Model-Based Definition):** PMI (Product Manufacturing Information) kodlarıyla tüm tolerans ve GD&T verilerinin doğrudan 3D CAD modelin içine (Solidworks/CATIA vb.) gömülmesi.
2.  **CMM Auto-Check:** İşlenen parçanın CMM makinesine bağlandığı an, bilgisayarın 3D datadaki toleranslarla kendi lazer/prob taramasını milisaniyeler içinde eşleştirip "Geçti/Kaldı" raporu vermesi.

---

## ⚠️ Operasyonel Riskler: "Okunamayan Standartlar"
Uluslararası standartların atölyede yanlış yorumlanması felaketle sonuçlanır.

-   **Metrik vs. İnç (Emperyal) Uyuşmazlığı:** Bir Amerikan makinesinin (ANSI) inç bazlı cıvatasını, bir metrik (ISO) deliğe zorlayarak (dişleri bozarak) takmak. 1999'daki Mars iklim sondasının düşme sebebi tam olarak bu birim uyuşmazlığıdır.
-   **Kritik Hata (Termal Genleşme):** 20°C ortam şartlarında üretilmiş H7 toleranslı çelik bir parçanın, 40°C fabrika ortamında CMM cihazına soğutulmadan bağlanıp "Bu hatalı" şeklinde reddedilmesi.

---

## 🚀 Meta-Mühendislik Vizyonu
Gelecekte "Tolerans" sabit bir değer değil, yapay zeka tarafından denetlenen dinamik bir varlık olacaktır.

-   **AI Tolerance Optimization:** Yapay zeka; makinenin çalışma şartlarına, malzemenin ısınma oranlarına ve maliyete bakarak mühendise "Burada H7 yerine H8 kullanırsan makine bozulmaz ama üretim hızın %20 artar" diyerek tasarım tashihi yapacak.
-   **Nanoscale Standards:** Çip üretim tezgahları gibi sistemler için ISO standartlarının artık mikron altı (Nanometre) seviyelere inmesi ve atomik boyutta pürüzlülük (Ra) ölçümlerinin sanayiye girmesi.

---
*Sanayi 1001: Kusursuzluğun sınırları, standartların tanımlandığı o binde birlik dünyada gizlidir.*
