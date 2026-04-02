# Torna Tezgahı ve Universal İşleme 101 (Lathe & Manual Machining)

## 🎯 TL;DR (Özet)
Torna, bir iş parçasının kendi ekseni etrafında döndüğü ve kesici takımın bu dönen parçadan talaş kaldırdığı "imalatın atası" olan tezgahtır. CNC'lerin aksine, Universal (manuel) tornada hassasiyet; bilgisayar koduna değil, operatörün (ustanın) elindeki "mikrometrik hissiyata" ve kalem bileme yeteneğine bağlıdır. Bu rehber, dönen metalin fiziği ile usta tecrübesini mekatronik bir perspektifle birleştirir.

---

## ⚙️ Çalışma Mantığı (Arka Plandaki Fizik)
Torna işlemi, temel bir **silindirik kesme** fiziğidir. İş parçası ana mil (spindle) üzerindeki "ayna" tarafından tutulur ve yüksek devirle döndürülür.

1.  **Kesme Hızı (Vc):** Parçanın çapı büyüdükçe, dış yüzeydeki doğrusal hız artar. Fiziksel olarak, aynı devirde (RPM) büyük çaplı bir parçayı işlemek, küçük çaplıya göre daha fazla ısı üretir.
2.  **Talaş Kaldırma Kuvveti:** Kesici takım (kalem), parçaya daldığında muazzam bir radyal ve eksenel kuvvetle karşılaşır. Bu kuvvet, tezgahın "rijitliği" (rigid) tarafından sönümlenmelidir.
3.  **Santrifüj Etkisi:** Özellikle dengesiz (asimetrik) parçalar yüksek devirde döndüğünde, merkezkaç kuvveti tezgahı sarsabilir; bu da yüzey pürüzlülüğünü (Ra) bozar.

---

## 🛠️ Atölye Gerçekleri ve Jargon
Tornacılık, sanayinin en çok jargon barındıran branşıdır.

| Atölye Terimi | Teknik Karşılığı | Açıklama |
| :--- | :--- | :--- |
| **Ayna** | *Chuck* | Parçayı sıkan, 3 veya 4 ayaklı dönen bağlama birimi. |
| **Puntera (Punta)** | *Tailstock / Center* | Uzun parçaların ucunun salgı yapmaması için arkadan destekleyen birim. |
| **Kalem** | *Cutting Tool / Insert* | Talaş kaldıran, sert metal veya elmas uçlu kesici. |
| **Pasoda** | *Depth of Cut* | Tek seferde kaldırılan talaş miktarı. "Bir paso daha git" denir. |
| **Salgı Yapmak** | *Runout* | Parçanın dönüş ekseninden kaçık olması ve yalpalaması. |
| **Kılçık Altı** | *Undercut* | Bir fatura veya diş dibinde, birleşmeyi rahatlatmak için açılan küçük kanal. |

**Usta Tavsiyesi:** "Ayna anahtarını asla aynanın üzerinde bırakma! Unutup şaltere basarsan o anahtar mermi gibi fırlar, ya tezgahı ya da seni parçalar."

---

## 💻 Dijital Entegrasyon (Mekatronik/Yazılım Boyutu)
Manuel tornadan dijital dünyaya geçiş iki aşamada gerçekleşir:

1.  **DRO (Digital Read Out):** Manuel tornalara takılan optik cetveller ve dijital ekranlar. Ustanın volanı kaç tur çevirdiğini değil, kesicinin parçaya göre tam koordinatını (X ve Z ekseni) milimetrenin binde biri hassaslığında görmesini sağlar.
2.  **Sabit Kesme Hızı (Constant Surface Speed - CSS):** CNC tornalarda, kesici takım merkeze (sıfıra) yaklaştıkça devrin otomatik olarak artmasıdır. Bu, yüzey kalitesinin parçanın her noktasında aynı kalmasını sağlayan bir yazılım algoritmasıdır.
    *   **G-Code Karşılığı:** `G96 S200` (Kesme hızını 200 m/dk'da sabit tut).

---

## ⚠️ İş Güvenliği ve Kanlı Canlı Hatalar
Torna, sanayide uzuv kaybının en sık yaşandığı makinelerden biridir.

1.  **Eldiven Yasak:** Dönen bir aynaya eldivenle yaklaşırsanız, bir iplik takıldığı anda eliniz saniyeler içinde aynaya dolanır. Tornada asla eldiven kullanılmaz!
2.  **Talaş Sarma:** Sürekli (lüle) talaş çıkarken elinizle çekmeye çalışmayın. O talaş jilet kadar keskindir ve sizi tezgahın içine çekebilir. "Çengel" kullanın.
3.  **Gözlük Şart:** Sıcak ve keskin talaşlar mermi hızıyla fırlar; koruyucu gözlük hayat kurtarır.
4.  **Siperlik:** Ayna üzerindeki talaş sıçratma siperliği asla açık bırakılmamalıdır.

---

## 🚀 Meta-Mühendislik Vizyonu
Geleceğin tornası artık sadece bir kesici değil, bir hibrit sistemdir.

-   **Otonom Optimizasyon:** Sensörler kesme sesini dinleyerek "zırıltı" (chatter) olup olmadığını anlar ve devri otomatik olarak rezonans dışına kaydırır.
-   **Hibrit Talaşlı/Eklemeli:** Aynı tezgah hem laser metal depolama (LMD) ile parça üzerine malzeme ekleyebilir, hem de hemen ardından onu torna ederek nihai ölçüsüne getirebilir.
-   **Yapay Zeka Destekli Operatör:** Artık usta hissiyatı, titreşim ve ısı sensörlerinden gelen Big Data ile dijital ikiz üzerinden simüle edilerek mükemmelleştirilecek.

---
*Sanayi 1001: İlk talaştan son mikrona kadar, bilgi her şeydir.*
