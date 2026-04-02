# Tezgah Kataloğu ve Sınıflandırma (Industrial Machine Taxonomy)

## 🎯 TL;DR (Özet)
Bu döküman, modern bir fabrikanın veya bir atölyenin sahip olabileceği tüm mekanik "kasları" (tezgahları) sınıflandırmayı amaçlar. Sanayide her tezgahın bir "uzmanlık alanı", bir "hassasiyet sınırı" ve bir "çalışma mantığı" vardır. Bu liste, kaba talaştan mikron düzeyinde bitirmeye kadar tüm makine parkurunun haritasıdır.

---

## ⚙️ Tezgahlar: Kategorik Bilgi Bombardımanı

### 1️⃣ Talaşlı İmalat Tezgahları (Metal Kesme)
*   **Üniversal Torna:** Silindirik parçaların kesilmesi için temel tezgah. Manuel kontrol.
*   **CNC Torna:** Bilgisayar kontrollü, karmaşık silindirik formlar (Vida, mil, flanş).
*   **Dik İşleme Merkezi (VMC):** 3 veya daha fazla eksende prizmatik parçaların (Motor bloğu, kalıp) işlenmesi.
*   **Yatay İşleme Merkezi (HMC):** Ağır ve büyük parçaların, talaşın kendi kendine düştüğü yatay mil avantajıyla işlenmesi.
*   **Borverk (Boring Machine):** Dev parçaların içine çok hassas ve büyük delikler açmak, yüzey taramak için kullanılan sanayi devi.
*   **Planya ve Vargel:** İleri-geri hareketle düz yüzey hatları veya kanal açan geleneksel tezgahlar.
*   **Broşlama (Tığ Çekme):** Bir parçanın içindeki kanalın (Kama yuvası) tek bir dikey geçişle hassas şekilde açılması.
*   **Honlama (Honing):** Silindir iç yüzeylerinin, yağ tutacak mikrotay kanallara sahip olması için yapılan süper hassas bitirme.

### 2️⃣ Aşındırma ve Hassas Yüzey İşleme
*   **Sathı Taşlama:** Düz metal yüzeylerin mikron seviyesinde düzeltilmesi.
*   **Silindirik Taşlama:** Millerin veya deliklerin dış/iç çaplarının mikron hassaslığında parlatılması.
*   **Tel Erozyon (Wire EDM):** Elektrik arkıyla su içinde, iletken tüm metallerin mikronluk kesilmesi.
*   **Dalma Erozyon (Sink EDM):** Bir elektrotun (Kalıp şeklinin aynısı) metale dalarak, o şeklin tersini bırakarak boşaltması.
*   **Laping:** İki yüzeyin birbirine sızdırmazlık düzeyinde alışması için yapılan en üst düzey aşındırma.

### 3️⃣ Sac ve Plastik Şekillendirme
*   **Lazer Kesim:** Sacın yüksek ısı ile hızla kesilmesi (Fiber/CO2).
*   **Abkant Pres:** Sacın tonajlı baskı ve V-kalıplarla bükülmesi.
*   **Giyotin Makas:** Sacın bir bıçak darbesiyle düz olarak kesilmesi.
*   **Eksantrik Pres:** Kalıp yardımıyla saca bir vuruşta şekil veren veya delik açan seri üretim devi.
*   **Hidrolik Pres:** Yavaş ama çok yüksek tonajlı, form verme (Derin çekme) veya burç çakma işlemleri.
*   **Plastik Enjeksiyon:** Hammaddenin eritilip kalıba basılarak seri plastik üretimi.

---

## 🛠️ Atölye Gerçekleri ve Jargon
"Hangi makinede ne yapılır?" - Atölye şefinin zihnindeki seçim kriterleri:

| Tezgah | Uzmanlık Alanı | Atölye Gereksinimi |
| :--- | :--- | :--- |
| **Borverk** | Büyük Bloklar (Gemi motoru vb.) | Koca bir hol ve vinç kapasitesi. |
| **Tel Erozyon** | Sertleşmiş Kalıp Çeliği | Saf su (Dielektrik) ve hassas klima. |
| **VMC** | Her türlü prizmatik parça | G-Code bilgisi ve CAM yazılımı. |
| **Taşlama** | Sızdırmazlık ve Hassas Tolerans | Mutlak tozsuzluk ve bor yağı akışı. |
| **Vargel** | Geniş Kanallar (Kama yuvası vb.) | Geleneksel kalem bileme ustadı. |

---

## 💻 Dijital Entegrasyon (Mekatronik Boyutu)
Modern tezgahlar artık sadece bir mekanizma değil, birer "Compute Node"dur.

1.  **DNC (Direct Numerical Control):** Tezgahların fabrikanın ana sunucusuna bağlanıp, G-Code'ları merkezden otonom olarak çekmesi.
2.  **Adaptive Feed Control:** Tezgahın, malzemenin sertliğine göre ilerleme hızını kendi kendine optimize etmesi.
3.  **Digital Twin:** Tezgahın dijital ikizi üzerinden, parça daha işlenmeden "çarpışma" (Crash) testlerinin yapılması.

---

## ⚠️ İş Güvenliği ve Kanlı Canlı Hatalar
"Makine seni değil, sen makineyi yönetmelisin."

-   **Momentum Tehlikesi:** Dev bir Borverk milinin durması saniyeler sürer; o momentumun arasında hiçbir canlı kalamaz.
-   **Kıvılcım ve Yangın:** Lazer ve Taşlama gibi makinelerde çıkan kıvılcımların hammadde depolarına sıçraması.
-   **Kör Noktalar:** CNC kabini içindeki "unvan fırlaması" durumunda camın mukavemeti.

---

## 🚀 Meta-Mühendislik Vizyonu
Gelecek, "Exoskeleton" makineler ve hibrit üretimde.

-   **Additive + Subtractive:** Parçanın önce 3D printer ile eklenip, aynı kafanın frezeye dönüşüp onu işlemesi.
-   **Self-Calibrating Machines:** Tezgahın, ısındığında veya aşındığında kendi hassasiyetini lazerle ölçüp yazılımsal olarak düzeltmesi.

---
*Sanayi 1001: Her makine, insan zekasının çeliğe binen gücüdür.*
