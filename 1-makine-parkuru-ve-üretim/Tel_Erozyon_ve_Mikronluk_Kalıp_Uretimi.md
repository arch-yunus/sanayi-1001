# Tel Erozyon ve Mikronluk Kalıp Üretimi (Wire EDM & Precision Tooling)

## 🎯 TL;DR (Özet)
Tel Erozyon (Wire Electrical Discharge Machining - WEDM); dielektrik bir sıvı içinde, çok ince bir pirinç tel ile iş parçası arasında oluşturulan elektriksel kıvılcımlar (ark) vasıtasıyla metali eriterek/yakarak kesme işlemidir. Fiziksel bir temasın olmadığı bu yöntemle, sertliği ne olursa olsun iletken tüm metallerde mikronluk hassasiyetle (0.001 mm) karmaşık geometriler ve dişi-erkek kalıp boşlukları üretilir. Sanayinin "cerrah neşteri"dir.

---

## ⚙️ Çalışma Mantığı (Arka Plandaki Fizik)
Tel erozyon, **elektriksel deşarj** ve **elektro-erozyon** prensipleriyle çalışır.

1.  **Plazma Kanalı Oluşumu:** Tel (anot) ve iş parçası (katot) birbirine çok yaklaştığında, aradaki dielektrik sıvıda iyonlaşma başlar ve bir plazma kanalı oluşur.
2.  **Mikroskobik Patlamalar:** Saniyede binlerce kez tekrarlanan arklar, metal yüzeyinde yerel olarak 8000°C ile 12000°C arası bir sıcaklık yaratır. Metal bu noktada sıvılaşır ve dielektrik sıvının basıncıyla yüzeyden "sökülüp" atılır.
3.  **Temassız Kesim:** Tel parçaya asla dokunmaz. Bu sayede incecik saclar veya çok sertleştirilmiş çelikler, mekanik bir zorlama (stres) olmadan, eğilmeden bükülmeden kesilebilir.

---

## 🛠️ Atölye Gerçekleri ve Jargon
Tel erozyon atölyesi; sessiz, titiz ve "su içinde" geçen bir dünyadır.

| Atölye Terimi | Teknik Karşılığı | Açıklama |
| :--- | :--- | :--- |
| **Tel Kırma** | *Wire Breakage* | Kesim sırasında telin aşırı gerilme veya kısa devre nedeniyle kopması. Kalıpçıların kabusudur. |
| **Havuzlama** | *Submerged Machining* | İş parçasının tamamen dielektrik su deposu içinde kesilmesi. |
| **Tel Sürme** | *Wire Threading* | Kopan veya yeni başlayan telin otomatik olarak delikten geçirilmesi. |
| **Reçine (Mix-Bed)** | *Deionization Resin* | Suyun iletkenliğini sabit tutmak için kullanılan filtreleme sistemi. |
| **Sıfırlama (Edge Find)** | *Centering* | Telin parçanın kenarını veya deliğini elektriksel temasla binde bir hassasiyetle bulması. |

**Usta Tavsiyesi:** "Su banyosundaki suyun sıcaklığına ve iletkenliğine dikkat et. Su ısınırsa parça genleşir, binde bir ölçü kaçar; kalıp bittiğinde dişi-erkek birbirine geçmez, emeklerin çöp olur."

---

## 💻 Dijital Entegrasyon (Mekatronik/Yazılım Boyutu)
Tel erozyon, bilgisayar desteği olmadan (CNC) var olamaz.

-   **4 Eksenli Kesim (UV-XY):** Telin üst kafası (U-V) ve alt kafası (X-Y) birbirinden bağımsız hareket edebilir. Bu sayede parçanın üstü kare, altı daire olacak şekilde "konik" kesimler yapılabilir.
-   **Jeneratör Kontrolü:** ECU, arkın şiddetini ve hızını (On-Off time) malzemenin kalınlığına göre milisaniye düzeyinde ayarlar.
-   **Kısa Devre Algoritması:** Eğer tel parçaya değerse (kısa devre), sistem teli mikron düzeyinde geri çeker, arkı temizler ve tekrar ilerler. Bu otonom bir "self-recovery" sürecidir.

---

## ⚠️ İş Güvenliği ve Kanlı Canlı Hatalar
Sessiz ve yavaş görünse de, tel erozyon yüksek voltaj ve hassas kimyasal riskler barındırır.

1.  **Elektrik Çarpması:** Makine çalışırken suyun içine veya tele dokunmak. Yüksek frekanslı arklar ciddi sinir hasarına yol açabilir.
2.  **Parçanın Düşmesi:** Kesim bittiğinde (kopma koparma anı), ağır metal parçanın ayak üzerine düşmesi veya telin üzerine düşerek teli/tezgahı bozması. "Kesim bitmeden parçayı mıknatısla veya destekle tutmalısın."
3.  **Yanlış Tel Seçimi:** Kalın tel ile dar kavisleri dönmeye çalışmak. Fiziksel olarak mümkün değildir; tel gerilip kopacaktır.
4.  **Cilt Tahrişi:** Dielektrik sıvısı ve metal çamuru (sludge) sürekli temas halinde egzama yapabilir; eldiven ve hijyen kritiktir.

---

## 🚀 Meta-Mühendislik Vizyonu
Geleceğin "Tel Erozyonu" atomik seviyeye iniyor.

-   **Micro-EDM:** 5 mikron (saç telinden ince) kalınlıktaki tellerin yapay zeka ile yönetilerek, mikro-cerrahi aletleri veya nano-sensörlerin üretimi.
-   **Frictionless Future:** Telin yerine lazer-erozyon geçişli hibrit sistemler gelerek, dielektrik sıvıya ihtiyaç duymadan, çok daha yüksek hızlarda "soğuk kesim" yapılacak.
-   **Dinamik Tel Gerilimi:** Yapay zeka, kesim sesinden (elektriksel gürültüden) telin kopma riskini %99 tahmin edip hızı o an optimize edecek.

---
*Sanayi 1001: Elektriğin kıvılcımını, mikronun disipliniyle şekillendiriyoruz.*
