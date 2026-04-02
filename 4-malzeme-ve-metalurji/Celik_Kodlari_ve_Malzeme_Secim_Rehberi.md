# Çelik Kodları ve Malzeme Seçim Rehberi (Industrial DNA: Steel Alloys)

## 🎯 TL;DR (Özet)
Her mühendislik tasarımı, doğru malzemenin seçimiyle başlar. Sanayide çelik; sadece "demir" değil, içindeki karbon ve alaşım (Krom, Nikel, Molibden vb.) elementlerinin oranıyla karakter kazanan bir "DNA"dır. Bu döküman; 4140'tan 7131'e, 304 paslanmazdan 7075 alüminyuma kadar sanayide en sık kullanılan metallerin kodlarını, özelliklerini ve "yağ-ısı" karşısındaki davranışlarını belgeler. Metalin dilini bilmeyen, tasarımı yürütemez.

---

## ⚙️ Metalin DNA'sı: Alaşımların Dünyası

### 1️⃣ Islah ve İmalat Çelikleri (Güç ve Dayanım)
*   **4140 (42CrMo4):** Sanayide "her işe gelen" efsanevi çelik. Yüksek tokluk ve sertlik verir. Millerde, dişlilerde ve akslarda kullanılır. Isıl işleme (Sertleştirmeye) çok iyi tepki verir.
*   **Ck45:** Karbon oranı orta düzede olan, kolay işlenebilen ama 4140 kadar sertleşmeyen temel imalat çeliği.
*   **St37 / St52:** Yapısal çelikler. Kaynak edilebilirliği mükemmeldir ama sertleşmezler (Sadece kaba form, şasi vb.).

### 2️⃣ Sementasyon Çelikleri (Yüzey Sert, İç Yumuşak)
*   **7131 (16MnCr5):** Dişlilerin vazgeçilmezi. Yüzeyi cam gibi sertleştirilirken (Sementasyon), iç kısmın "darbe emici" (yumuşak) kalmasını sağlar. Dişli çarklarda ve miller de bu tercih edilir.

### 3️⃣ Paslanmaz Çelikler (Korozyon Direnci)
*   **304 Paslanmaz:** Gıda ve kimya sanayinde standarttır; korozyona dirençlidir ama tuzlu suda veya asitte zayıf kalabilir. "Mıknatıs tutmaz" (Östenitik).
*   **316 Paslanmaz:** Molibden ilavesiyle asitlere ve deniz suyuna karşı üstün direnç gösterir. Sanayinin "marine" sınıfıdır.

### 4️⃣ Alüminyum Alaşımları (Hififlik ve Havacılık)
*   **6061 Alüminyum:** Kolay işlenir, korozyona dayanır; yapısal profillerde ve basit makine parçalarında kullanılır.
*   **7075 Alüminyum (Ergal):** Çelik kadar sağlamdır ama alüminyum kadar hafiftir. Havacılık, savunma ve yüksek gerilimli kalıp parçalarında kullanılır.

---

## 🛠️ Atölye Gerçekleri ve Jargon
"Hangi çeliği alalım usta?" - Karar verme anı:

| Çelik Kodu | Atölye Adı | Karakteristik Özellik |
| :--- | :--- | :--- |
| **4140** | Islah Çeliği | Sertleşince "cam" olmaz, esner ve sağlam durur. |
| **7131** | Karbonatlı (Semente) | Isıl işlemden sonra yüzeyine eğe işlemez, ama içinden kırılmaz. |
| **304** | Krom | Kaynağı zordur, işlerken çabuk ısınır ve matkap ucunu yakar. |
| **Çelik Çelik** | *High Speed Steel (HSS)* | Kendisi zaten kesicidir; diğer metalleri yontmak için kullanılır. |
| **Döküm (Pik)** | *Gray Iron* | Hassas ama kırılgandır; sönümleme özelliği nedeniyle tezgah gövdelerinde kullanılır. |

**Usta Tavsiyesi:** "4140 kullanıyorsan yağın içinde su verme yapmalısın. Eğer suya sokarsan saniyeler içinde çatlar, parçayı 'çıt' diye kırarsın. Her metalin ayrı bir soğutma 'duası' vardır."

---

## 💻 Dijital Entegrasyon (Mat-Sim: Material Simulation)
Malzeme seçimi artık "bilgisayar başında" bitiyor.

1.  **FEA (Finite Element Analysis):** Seçilen malzemenin (Örn: 4140) yük altındaki bükülmesi, simülasyon dünyasında 1 kg hata payı ile hesaplanır.
2.  **EDX / Spektro:** Metalin içindeki elementlerin (C, Si, Mn, Cr) oranını saniyeler içinde ölçen elde taşınabilir dijital cihazlar. "Bu parça gerçekten 316 mı?" sorusunun cevabı burada.
3.  **Kritik Yazılım Algoritması (Heat Rate):** Isıl işlem fırınlarındaki her alaşımın "fırın süresi ve sıcaklığı" (Phase Transformation Diagram) yazılımla otonom yönetilir.

---

## ⚠️ İş Güvenliği: "Karışan Metaller, Patlayan Sistemler"
Malzeme hatası, gizli bir bombadır.

-   **Yanlış Malzeme Seçimi:** St37 (yumuşak) bir çelikten motor cıvatası yapmak; motorun çalışma anında cıvataların kopup blok parçalaması demektir. "Cıvata kafasındaki 8.8 veya 10.9 kodlarına bakmayı asla unutma!"
-   **Zehirli Gazlar:** Galvanizli (Çinko kaplı) sacı kaynak yaparken çıkan sarımtırak duman ölümcüldür; metal dumanı ateşi (Zinc fume fever) yapar. Havalandırma ve maske hayati önem taşır.
-   **Kıvılcım Riski:** Titanyum ve Magnezyum gibi metalleri taşlarken çıkan kıvılcımlar su ile sönmez, daha beter patlar. Ozel yangın söndürücüler şarttır.

---

## 🚀 Meta-Mühendislik Vizyonu
Gelecek, "Akıllı ve Fonksiyonel Dereceli" malzemelerde.

-   **Memory Alloys (Nitinol):** Bükülen metalin ısıtılınca eski haline dönmesi (Süper elastisite). Robotik ve havacılıkta devrim!
-   **3D Printed Graded Steel:** Bir ucunu 4140 (tok), diğer ucunu 7131 (sert) olarak aynı anda basan metalik geçiş teknolojileri.
-   **Graphene Reinforced Steel:** Çeliğin içine grafen enjekte edilerek 10 kat daha hafif ama 100 kat daha sağlam "Nano-Metal"lerin üretimi.

---
*Sanayi 1001: Maddeyi tanımayan, manayı (formu) veremez.*
