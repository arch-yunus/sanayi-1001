# Enerji Kalitesi ve Fabrika Elektrik Dağıtımı (Power Quality & Electrical Distribution)

## 🎯 Yönetici Özeti
Sanayideki makine parkurunun beyni otomasyonsa, kan dolaşım sistemi fabrikanın elektrik dağıtım altyapısıdır. Şebekeden gelen yüksek gerilimin makine panolarına güvenli, kesintisiz ve "temiz" bir şekilde ulaşması, spesifik bir mühendislik disiplinidir. **Enerji Kalitesi (Power Quality)**, sadece elektrik olması demek değil; bu elektriğin akım/gerilim sinüsoidal dalgasının bozulmadan (harmoniksiz) ve güç faktörünün (Cos φ) optimizasyonuyla tezgahlara iletilmesidir. Bu doküman; trafo, şalt malzemeleri, kompanzasyon ve harmonik filtrasyonunu teorik ve saha odaklı olarak inceler.

---

## ⚙️ Fabrika Elektrik Dağıtım Anatomisi

### 1️⃣ Trafo ve Ana Dağıtım Panosu (MDP - Main Distribution Panel)
Teiaş/Tedaş ağı üzerinden Fabrikaya Orta Gerilim (OG - genelde 31.5 kV veya 34.5 kV) girer. Endüstriyel trafolar bu gerilimi makine kullanım seviyesi olan Alçak Gerilime (AG - 400V Faz-Faz, 230V Faz-Nötr) düşürür.
*   **Kuru Tip vs Yağlı Tip Trafo:** Modern tesis içlerinde yangın riskini sıfırlayan Kuru (Dökme Reçine) tip trafolar zorunludur. Dış sahalarda Yağlı tip daha ekonomik bir alternatiftir.
*   **Ana Şalter (ACB / Air Circuit Breaker):** Trafonun hemen çıkışında yer alan devasa şalterdir. Binlerce amperi kontrol eder, tesis içindeki büyük kısa devrelerde "Açma (Trip)" yaparak fabrikayı korur.

### 2️⃣ Şalt Malzemeleri ve Koruma Elemanları
Akımı kontrol eden, bölen ve koruyan saha askerleridir.
*   **MCCB (Kompakt Şalter / Kesici):** Orta ölçekli dağıtım panolarında (Örn: Bir pres hattının ana beslemesinde) termik ve manyetik koruma sağlar.
*   **MCB (Otomatik Sigorta):** Panolardaki aydınlatma, priz veya küçük motor hatlarını koruyan kompakt elemanlar. (C Tipi sanayi motorları, B serisi aydınlatma için).
*   **Kontaktör:** Bir otomasyon sinyali (PLC veya röle) ile yüksek akımlı bir hattı anahtarlayan elektromekanik donanım.
*   **Kaçak Akım Rölesi (RCD):** Çarpılmalara karşı insan hayatını (30mA) veya yangına karşı cihazları (300mA) korumak üzere faz ve nötr arasındaki izolasyon kaybını ölçen hayati bileşen.

### 3️⃣ Kompanzasyon ve Reaktif Güç (Cos φ)
**Reaktif Güç**, manyetik alan yaratan cihazların (elektrik motoru, trafo) şebekeden çektiği ancak mekanik işe çevirmediği "sanal" bir enerji türüdür. Bu güç şebekede gereksiz yük oluşturur.
*   **Kompanzasyon Panosu:** Çekilen reaktif enerjiyi (Endüktif) şebekeye geri göndermeden kendi içinde nötrlemek için zıt karakterli (Kapasitif) kondansatörlerin devreye otomatik alınıp çıkarılması sistemidir.
*   **Yasal Zorunluluk:** Tesislerin aktif güce oranla Çekilen Endüktif gücü %20'yi, Kapasitif gücü %15'i geçemez. Geçerse kurumlara (Tedaş vb.) ağır "Reaktif Ceza" ödenir.

---

## 🛠️ Atölye Gerçekleri ve İletim Standartları

| Atölye Durumu / Jargon | Açıklama | Operasyonel Risk |
| :--- | :--- | :--- |
| **"Fazlardan Biri Gitti"** | Single Phasing | Şebekeden gelen 3 fazın 1'inin kesilmesi. 3 fazlı motor dönmeye çalışır ancak ısınarak yanar. "Faz Koruma Rölesi" takılması hayati zorunluluktur. |
| **"Sıfırlama Yapılmış"** | Topraklama Yerine Nötr Kullanımı | Makinenin gövdesini (toprak hattı) Nötr'e bağlama hatası. Şebekede kopukluk olursa gövdede 220V belirir; ölümcül çarpılmadır. |
| **"Şalter Atıyor (Trip)"** | Aşırı Akım (Overload) | Ya kablo kesiti incedir, ya parçada kısa devre vardır ya da şalter arızalıdır. Şalter değerini gözü kapalı büyütmek, hattın veya makinenin yanıp kül olması demektir. |

---

## 💻 Harmonik Kirlilik ve Enerji Kalitesi (Power Quality)

### Harmonik Nedir?
Frekans Sürücüleri (VFD), CNC tezgah güç kaynakları, LED aydınlatmalar gibi cihazlar "Lineer Olmayan" akım çeker. Yani şebekenin mükemmel SİNÜS dalgasını parçalayarak testere dişi gibi kirli bir dalgaya dönüştürürler.

**Sonuçları:**
1.  **Trafo ve Motor Isınması:** Cihazların içinden geçen yüksek frekanslı sinyaller bakır ve demir kayıplarını ikiye katlar; ısınmayı artırır.
2.  **Kondansatör Patlamaları:** Kompanzasyon panolarındaki kondansatörler aşırı harmonik akımı nedeniyle şişer veya patlar.
3.  **Hassas Kart Yanmaları:** Aynı hattı paylaşan PLC veya CNC beyin kartları (PSU) gerilim kirliliğinden dolayı aniden bozulur.

**Dijital Çözüm (Aktif Harmonik Filtre):** Kirliliği sürekli analiz edip, şebekeye "zıt yönde kirlilik (anti-dalga)" basarak toplam dalgayı tekrar tertemiz bir Sinüs'e (Gürültü İptal Kulaklığı mantığı) dönüştüren Akıllı Filtreleme cihazlarıdır.

---

## ⚠️ Elektrik İş Güvenliği (Arc Flash & İzolasyon)
- **Ark Parlaması (Arc Flash):** Yüksek akımlı panolarda (Ana Dağıtım veya Trafo) yanlış bir temasla oluşan devasa kısa devrenin havayı iyonize ederek 19.000°C'lik bir alev ve şok dalgası yaratmasıdır. Ark flaş forması giymeden AG/OG şalterlere müdahale edilmesi yasaktır.
- **Kilitleme / LOTO (Lock-Out Tag-Out):** Pano dışından izole şalter kapatılmalı, asma kilitlenmeli ve kilit anahtarı sadece çalışmayı yapan teknisyenin cebinde olmalıdır.
- **Topraklama Ölçümü:** Fabrika temel topraklama direnci (genelde < 5 Ohm) her yıl kalibrasyonlu Meger cihazı ile bağımsız firmalarca ölçülmeli ve raporlanmalıdır.

---

## 🚀 Meta-Mühendislik Vizyonu
- **Mikroşebekeler (Microgrids):** Fabrikaların sadece elektrik tüketen değil, çatısındaki güneş paneli (Rooftop Solar), batarya depolama (BESS) üniteleri ve kojenerasyon tesisleriyle kendi enerjisini üreten, hatta şebekeye satan yapay zeka yönetimli (AI-EMS) santraller haline gelmesi.
- **Katı Hal Trafoları (Solid-State Transformers):** Demir çekirdekli asırlık trafolar yerine; gerilim dönüşümünü sadece yarı-iletken IGBT'lerle gerçekleştiren 10 kat daha hafif akıllı trafolar.

---
*Sanayi 1001: Bir fabrikada elektriğin görünmeyen kalitesi, üretimin görünen kalitesini belirler.*
