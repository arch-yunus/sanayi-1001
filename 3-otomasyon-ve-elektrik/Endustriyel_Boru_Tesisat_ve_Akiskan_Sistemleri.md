# Endüstriyel Boru, Tesisat ve Akışkan Sistemleri (Piping & Process Engineering)

## 🎯 Yönetici Özeti
Bir fabrikanın içindeki boru ağı, insan vücudundaki damar sistemi gibidir: basınçlı hava, soğutma suyu, yakıt, buhar ve proses akışkanları bu altyapı üzerinden taşınır. **Proses Boruculuğu (Piping Engineering)**, boru malzeme seçiminden, bağlantı elemanları (fitting) ve vana tiplerinden, sistem basıncı hesaplamalarına kadar ciddi bir mühendislik disiplinidir. Bu rehber; endüstriyel tesis altyapısının "damarlarını" belgeler.

---

## ⚙️ Akışkan Sistemleri Temelleri

### Bernoulli Denklemi ve Borçluk Pratiği
```
P₁ + ½ρv₁² + ρgh₁ = P₂ + ½ρv₂² + ρgh₂ + Δp_kaybı
```
- **Basınç düşümü (Δp):** Boru uzunluğu, çapı, akışkan viskozitesi ve sürtünme katsayısına bağlıdır.
- **Pratik Kural:** Kompresör hattında hat hızı genellikle 6–10 m/s; su hatlarında 1–3 m/s tutulur.

---

## 🏗️ Boru Malzemeleri Sınıflandırması

| Malzeme | Kullanım Alanı | Avantaj | Dezavantaj |
| :--- | :--- | :--- | :--- |
| **Siyah Çelik Boru** | Buhar, gaz, yakıt | Yüksek basınç ve sıcaklık dayanımı | Pas; galvanizleme veya boya şart. |
| **Galvanizli Boru** | Soğuk su, hava | Korozyon direnci | Sıcak suda çinko çözünür, sağlık riski. |
| **Bakır Boru** | Klima, soğutma, gaz | Antibakteriyal, kolay şekillendirme | Maliyet yüksek; amonyak ile reaksiyona girer. |
| **Paslanmaz Çelik (316L)** | Gıda, kimya, ilaç | Hijyen, korozyon direnci | Kaynak uzmanlığı gerektirir. |
| **HDPE / PP-R** | Soğuk-sıcak su, kimyasal | Hafif, korozyon yok, kolay montaj | Sıcaklık sınırlı (~90°C). |

---

## 🔩 Bağlantı Elemanları ve Vana Sınıflandırması

### Fitting (Bağlantı) Türleri
- **Dirsek (Elbow):** 45° veya 90° yön değişimi.
- **Te (Tee):** Hat ayrımı veya birleşimi.
- **Redüksiyon:** Farklı çaptaki boruların birleştirilmesi.
- **Nipel / Manşon:** Düz hat uzatma.
- **Flanş:** Sökülebilir bağlantı; büyük çaplı ve yüksek basınçlı sistemler.

### Vana Türleri ve Seçim Rehberi

| Vana Tipi | Sembolü | Kullanım | Özellik |
| :--- | :--- | :--- | :--- |
| **Küresel Vana (Ball)** | ⊙—● | Açma/kapama | Hızlı, tam açık/tam kapalı |
| **Küçük Kapak (Globe)** | ⊙—▽ | Akış kısma (throttling) | Hassas kontrol |
| **Kelebek Vana (Butterfly)** | ⊙—⊕ | Büyük hat, düşük basınç | Kompakt ve hafif |
| **Geri Vurma (Check)** | →| | Tek yönlü akış | Geri akışı engeller |
| **Emniyet Valfi (Safety)** | ⊙—↑ | Basınç koruma | Ayar basıncında açılır |

---

## 🛠️ Atölye Gerçekleri ve Jargon

| Atölye Terimi | Teknik Karşılığı | Bağlam |
| :--- | :--- | :--- |
| **Boru Kırmak** | Pipe Break (Pressure Test) | Sisteme su veya hava basarak sızıntı testi. |
| **Hat Atmak** | Pipe Run / Routing | Bir noktadan diğerine boru güzergahı planlamak. |
| **Diş Açmak** | Threading | Borunun ucuna pafta ile vida dişi açmak. |
| **Teflon (PTFE)** | Thread Seal Tape | Dişli bağlantılardaki sızdırmazlık şeridi. |
| **Askı/Kelepçe** | Pipe Support / Clamp | Borunun kendi ağırlığını ve titreşimi taşıyan destek elemanları. |

**Kritik Tavsiye:** "Boru hattında her zaman en yüksek noktaya otomatik hava tahliye valfi, en alçak noktaya ise drenaj vanası koy. Hava cebi tıkanmaya, su birikintisi de korozyona yol açar."

---

## 💻 Dijital Entegrasyon (P&ID ve Akıllı Tesisat)
1. **P&ID (Piping & Instrumentation Diagram):** Tesisin tüm boru, ekipman, vana ve enstrümanlarını standart sembollerle gösteren mühendislik belgesi. ISO 10628 standardıyla çizilir.
2. **Akıllı Boru (Smart Piping):** Yerleşik basınç ve akış sensörleri olan boru segmentleri, sızıntıyı ve akış anomalisini buluta raporlayan IoT sistemi.
3. **Hydrotesting Simülasyonu:** FEA ile boru geçişlerindeki stres konsantrasyonlarını (dirsek, flanş vb.) basınç testi öncesinde sanal ortamda doğrulama.

---

## ⚠️ Kritik Güvenlik Riskleri
- **Su Darbesi (Water Hammer):** Vanaların çok hızlı kapatılmasıyla oluşan ani basınç dalgası (darbe) boru ve bağlantıları patlatabilir. Yavaş kapanan motorlu vana kullanılmalıdır.
- **Buhar Sistemi Yanıkları:** 180°C üzerindeki doymuş buhar, temas halinde deri katmanlarını anında tahrip eder. Valf ve flanş bağlantılarında tam ısı yalıtımlı eldiven zorunludur.
- **Gaz Sızıntısı:** Doğal gaz veya LPG hatlarında fiziksel sızıntı testi (köpük solüsyonu) yapılmadan sisteme basınç uygulanmaz.

---

## 🚀 Meta-Mühendislik Vizyonu
- **Kendi Kendini Onaran Borular:** Nano kapsüller içinde saklanan polimer malzemelerin boru cidarındaki mikro çatlak başladığında kimyasal reaksiyon başlatarak kendiliğinden tıkaması.
- **Digital P&ID:** Fiziksel sistemi birebir yansıtan 3D dijital ikizde herhangi bir vanayı tıklayarak basınç değeri, bakım geçmişi ve yedek parça stoku görüntüleme.

---
*Sanayi 1001: Bir fabrikanın sağlığı, damarlarındaki akışkanın kalitesiyle ölçülür.*
