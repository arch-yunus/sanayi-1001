# Endüstriyel Yüzey İşlem ve Kaplama Teknolojileri (Surface Finishing & Coating)

## 🎯 Yönetici Özeti
Bir makine parçasının işlenmesi, sadece talaş kaldırma süreciyle sona ermez. İşlenmiş çıplak metal; korozyon, aşınma ve kimyasal bozunmaya karşı savunmasızdır. **Yüzey işlem ve kaplama (Surface Treatment)**, metalin dış kristal yapısını değiştirerek veya üzerine koruyucu bir tabaka inşa ederek parçanın ömrünü eksponansiyel olarak artıran kimyasal ve metalürjik bir disiplindir. Bu rehber; galvanizasyondan sert kroma, eloksaldan kataforeze kadar endüstriyel kaplama teknolojilerinin teorik ve pratik analizini sunar.

---

## ⚙️ Yüzey Korumasının Fiziği ve Kimyası

### 1️⃣ Galvanizasyon (Çinko Kaplama)
Demir ve çelik malzemelerin korozyondan (paslanmadan) korunması için uygulanan en yaygın endüstriyel metottur.
*   **Sıcak Daldırma Galvaniz (Hot-Dip):** Metalin ~450°C'de erimiş çinko havuzuna daldırılması. Çinko, demirle alaşım yaparak kalın (50-100 μm) ve mekanik darbelere ultra dayanıklı bir zırh oluşturur. Dış mekan çelik konstrüksiyonlarında standarttır.
*   **Elektro-Galvaniz:** Elektroliz yoluyla (soğuk) çinko kaplama. Çok daha ince (5-15 μm) ve homojen bir mikron kaplama sağlar. Vida, cıvata ve tolerans hassasiyeti gerektiren makine parçalarında tercih edilir.

### 2️⃣ Eloksal (Anodizing - Alüminyum Optimizasyonu)
Alüminyumun yüzeyindeki doğal oksit tabakasının, sülfürik asit ve elektrik akımıyla yapay olarak kalınlaştırılması işlemidir.
*   **Standart Eloksal:** Korozyon direnci ve estetik (renklendirme) sağlar. Mimari profillerde yaygındır.
*   **Sert Eloksal (Hard Anodizing):** Düşük sıcaklıkta (0°C) uygulanan, alüminyum yüzeyini neredeyse takım çeliği sertliğine (60 HRC civarı) çıkaran işlemdir. Pnömatik silindir içlerinde ve havacılık parçalarında kullanılır.

### 3️⃣ Sert Krom Kaplama (Hard Chrome Plating)
Sürtünmenin ve aşınmanın yüksek olduğu dönen/kayan yüzeylerde uygulanır. Krom (Cr6+) iyonlarının elektrolizle yüzeye bağlanmasıdır.
*   **Özellikleri:** Ultra düşük sürtünme katsayısı, cam gibi parlak ve pürüzsüz yüzey, ~65-70 HRC yüksek sertlik.
*   **Tipik Uygulamalar:** Hidrolik piston milleri, motor subap sapları, krank milleri.

### 4️⃣ Kataforez Boya (KTL/E-Coating)
Su bazlı boya partiküllerinin, elektriksel potansiyel farkı kullanılarak (negatif-pozitif kutup çekimi) metalin her hücresine eşit oranda nüfuz etmesi işlemidir.
*   **Karakteristik:** Ulaşılması imkansız kör deliklerin içini bile aynı mikron kalınlığında boyar. Otomotiv şasilerinin ilk ve en hayati pas koruma katmanıdır.

---

## 🛠️ Atölye Gerçekleri ve Tolerans Yönetimi

| Operasyon | Eklenen/Değişen Kalınlık | Mekanik Toleranslara Etkisi |
| :--- | :--- | :--- |
| **Sıcak Galvaniz** | + 50-150 mikron | Dişli (vida) çekilmiş parçalar kaplamadan sonra çalışmaz; kılavuz yeniden çekilmelidir. |
| **Elektro-Galvaniz** | + 5-15 mikron | H7/g6 gibi sıkı olmayan geçmelerde kabul edilebilir, dişleri bozmaz. |
| **Sert Krom** | + 10-500 mikron | Kromdan önce paylı (küçük) taşlama yapılır; kaplamadan sonra tekrar taşlanarak ölçüye getirilir. |
| **Sert Eloksal** | ~%50 içe, %50 dışa doğru | Parça ölçüsünü mikron bazında büyütür, hassas yataklamalarda CNC'de pay bırakılmalıdır. |

---

## 💻 Karbon Ayak İzi ve Çevre 4.0
1. **Atık Su Arıtma (Zero Liquid Discharge):** Galvaniz ve krom tesislerindeki asidik/siyanürlü atık suların iyon değiştirici reçineler ve ters osmoz ile %100 oranında geri dönüştürülmesi.
2. **Krom VI (Cr6+) İkamesi:** Geleneksel sert kromun kanserojen altı değerlikli yapısı, REACH regülasyonları gereği yerini "Trivalent Chrome (Cr3+)" veya "HVOF (Yüksek Hızlı Oksijen-Yakıt Püskürtme) Tungsten Karbür" kaplamalara bırakmaktadır.

---

## ⚠️ Kritik Riskler ve Tehlike Analizi
- **Hidrojen Gevrekliği (Hydrogen Embrittlement):** Çelik parçaların elektro-galvaniz veya asitle temizleme sırasında içine giren hidrojen atomları, metali içten cam gibi kırılgan yapar (Özellikle 10.9 ve üzeri yüksek mukavemetli cıvatalarda). Kaplamadan hemen sonra 200°C'de hidrojen giderme fırınlanması (Baking) şarttır.
- **Siyanür ve Asit Zehirlenmesi:** Kaplama banyolarındaki ağır kimyasalların buharı yavaş katildir. Egzoz emiş (Scrubber) sistemlerinin saniye durmaması gerekir.
- **Termal Distorsiyon:** Sıcak daldırma galvanizde (450°C), ince saclı profillerin veya asimetrik kaynaklı yapıların kendi etrafında kıvrılması (çarpılma) kronik bir hatadır.

---
*Sanayi 1001: Metalin kalitesi işleme esnasında, ömrü ise kaplama banyosunda belirlenir.*
