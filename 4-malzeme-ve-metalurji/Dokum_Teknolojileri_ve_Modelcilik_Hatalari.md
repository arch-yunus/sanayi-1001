# Döküm Teknolojileri ve Modelcilik Hataları (Casting & Patternmaking)

## 🎯 TL;DR (Özet)
Döküm; sıvı hale getirilmiş metalin, istenen şekle sahip bir boşluğa (kalıp) dökülerek katılaşmasıyla parça elde etme sanatıdır. Karmaşık geometrilerin üretilmesinde en kadim ama en teknik yöntemdir. Bir döküm parçasının kalitesi; sadece metalin sıcaklığına değil, sıvı metalin kalıp içindeki akış hızına (Laminar/Turbulent), gaz çıkış yollarına ve metalin katılaşırken yaptığı "çekme" (Shrinkage) fiziğine bağlıdır.

---

## ⚙️ Çalışma Mantığı (Arka Plandaki Fizik)
Döküm, **faz değişimi** ve **akışkanlar dinamiği**nin birleşimidir.

1.  **Sıvı Metal Akışı (Bernoulli Prensibi):** Metal, kalıba (yolluk - runner) girdiğinde hızı ve basıncı kontrol edilmelidir. Çok hızlı akış, kum kalıbı aşındırıp parçaya "kum bulaşmasına" (Sand inclusions) sebep olur; çok yavaş akış ise metalin kalıbı doldurmadan donmasına (Misrun) yol açar.
2.  **Katılaşma ve Çekme (Shrinkage):** Metal sıvıdan katıya geçerken hacmi azalır. Fiziksel olarak, parça merkezinde "boşluk" (Lunker) oluşmaması için "Besleyici" (Riser) adı verilen ek metal rezervleri kullanılır. Besleyici, parçadan daha geç donarak sıvı metal takviyesi yapar.
3.  **Gaz Geçirgenliği:** Kalıbın içindeki hava ve yakılan reçineden çıkan gazlar dışarı atılmalıdır. Kalıbın gaz geçirgenliği (Permeability) olmazsa, metal içinde "gaz boşlukları" (Blowholes) oluşur.

---

## 🛠️ Atölye Gerçekleri ve Jargon
Dökümhane; tozun, ateşin ve tecrübenin harmanlandığı bir yerdir.

| Atölye Terimi | Teknik Karşılığı | Açıklama |
| :--- | :--- | :--- |
| **Model** | *Pattern* | Metalin şeklini alacağı ahşap, plastik veya metal kalıp örneği. |
| **Yolluk** | *Gating System* | Sıvı metalin kalıp boşluğuna girdiği kanal yolu. |
| **Maça** | *Core* | Parçanın içindeki boşlukları (delikleri) oluşturmak için kullanılan kum blok. |
| **Derece** | *Flask* | Kum kalıbın etrafını saran metal kutu/çerçeve. |
| **Derece Kaçıklığı** | *Mismatch* | Kalıbın alt ve üst yarısının tam hizalanmaması sonucu parçanın yamuk çıkması. |
| **Lunker** | *Shrinkage Cavity* | Katılaşma sırasında oluşan, parçanın içindeki çekme boşluğu. |

**Usta Tavsiyesi:** "Dökümden önce dereceyi iyice ağırlaştır veya cıvatalarla sık. Sıvı metalin kaldırma kuvveti (Archimedes prensibi) şakaya gelmez; derece havaya kalkarsa o kızgın metal her yere yayılır, her şeyi yakar."

---

## 💻 Dijital Entegrasyon (Mekatronik/Yazılım Boyutu)
Modern döküm artık "göz kararı" pota devirmek değil, **Dönüşüm Simülasyonu** ile yapılır.

-   **Döküm Simülasyon Yazılımları (Casting Simulation):** Parçanın neresinin önce, neresinin sonra donacağını (Solidification) bilgisayar ortamında simüle eder. Böylece yolluk ve besleyici yerleri deneme-yanılma yapmadan belirlenir.
-   **İndüksiyon Ocağı Otomasyonu:** Metalin içindeki Karbon, Silis ve Manganez miktarı "Spektrometre" cihazıyla saniyeler içinde ölçülür ve yazılım, içeriği istenen standarda (Örn: GGG-40) getirmek için ne kadar "alaşım" eklenmesi gerektiğini hesaplar.
-   **3D Kum Yazıcılar (Sand Printing):** Model yapma zahmetini ortadan kaldırarak, karmaşık kum kalıpları ve maçaları doğrudan 3D yazıcıdan çıkartıp döküme hazır hale getirir.

---

## ⚠️ İş Güvenliği ve Kanlı Canlı Hatalar
Dökümhane, mutlak dikkat ve disiplin gerektirir; aksi takdirde sonuçlar "patlayıcı" olabilir.

1.  **Nemli Kalıp / Pota:** Kızgın metalin (1400°C+) içine bir damla su girmesi demek, suyun aniden buharlaşarak metalin binlerce parça halinde çevreye patlaması (Steam explosion) demektir. Potalar ve kalıplar her zaman "kupkuru" olmalıdır.
2.  **Yanlış Koruyucu Ekipman (KKE):** Sentetik (naylon vb.) kıyafetler dökümhanede giyilmez; metal sıçradığında teninize yapışır. Sadece özel deri veya yanmaz (alüminize) kıyafet kullanılmalıdır.
3.  **Toz ve Silikozis:** Kumdan çıkan ince tozlar akciğerlere telafisi olmayan zarar verir. Maske kullanımı opsiyonel değil, bir yaşam şartıdır.
4.  **Kritik Hata (Under-pouring):** Potalarda metalin yetmemesi sonucu kalıbın yarım kalması. Atölye deyimiyle: "Parça eksik çıktı".

---

## 🚀 Meta-Mühendislik Vizyonu
Geleceğin "Dökümü" artık forma girmiş, dijital bir sanata dönüşüyor.

-   **Otonom Pota Devirme:** Robotik kollar, metalin üzerindeki "curufu" ve "sıcaklığı" lazerle ölçüp akış hızını saniyede 10 mm hassasiyetle yöneterek sıfır hatalı döküm yapacak.
-   **Giga-Casting:** Tesla'nın öncülük ettiği gibi, otomobilin tüm şasisi onlarca parça değil, tek bir devasa döküm makinesiyle (Giga-press) tek parça halinde basılacak. Montaj hataları sıfıra inecek.
-   **Yapay Zeka Destekli Alaşımlar:** Belirli bir mukavemet değeri için en az enerji harcayacak "İdeal Metalurji"yi yapay zeka tasarlayıp ocağı buna göre programlayacak.

---
*Sanayi 1001: Ateşi forma, formu bilgiye döküyoruz.*
