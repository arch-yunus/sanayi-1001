# CNC Programlama ve CAM Yazılımları (G-Code & Computer-Aided Manufacturing)

## 🎯 Yönetici Özeti
CNC (Computer Numerical Control) tezgahlarının gücü, doğru G-Code programlamasıyla tam anlamıyla ortaya çıkar. Bu rehber; G ve M kodlarının fonksiyonel anatomisinden, Mastercam ve Fusion 360 gibi endüstriyel CAM yazılımlarına kadar uzanan "dijital talaşlı imalat" disiplinini kapsamlı biçimde belgeler. Bir VMC tezgahının fiziksel hassasiyeti, programcının CAM stratejisinin kalitesiyle eşdeğerdir.

---

## ⚙️ G-Code: Tezgahın Dili

### 1️⃣ Temel G-Kodları (Hazırlık Fonksiyonları)

| Kod | Açıklama | Kullanım Örneği |
| :--- | :--- | :--- |
| **G00** | Hızlı Konumlandırma (Kesme yok) | `G00 X100 Y50 Z5` |
| **G01** | Doğrusal Enterpolasyon (Kesme) | `G01 Z-10 F150` |
| **G02** | Saat Yönünde Dairesel Enterpolasyon | `G02 X50 Y50 I25 J0 F100` |
| **G03** | Saat Aksi Dairesel Enterpolasyon | `G03 X0 Y50 I-25 J0 F100` |
| **G17/18/19** | Çalışma Düzlemi Seçimi (XY, XZ, YZ) | `G17` (XY düzlemi) |
| **G40/41/42** | Takım Yarıçap Kompanzasyonu (Off/Sol/Sağ) | `G41 D01` |
| **G54–G59** | İş Koordinat Sistemi Seçimi | `G54` (1. iş sıfır noktası) |
| **G90/91** | Mutlak / Artımsal Koordinat Modu | `G91` (Artımsal mod) |

### 2️⃣ Temel M-Kodları (Makine Fonksiyonları)

| Kod | Açıklama |
| :--- | :--- |
| **M03/M04** | Mil saat / aksi yönde çalıştır |
| **M05** | Mili durdur |
| **M06** | Takım değiştir (`T02 M06`) |
| **M08/M09** | Soğutma sıvısı aç / kapat |
| **M30** | Program sonu ve başa dön |

### 3️⃣ Örnek Komple Program Yapısı
```gcode
%                        ; Program başlangıcı
O0001                    ; Program numarası
G21 G17 G90 G54          ; Metrik, XY düzlemi, Mutlak, İş koord. sist.
T01 M06                  ; 10mm parmak freze tak
S3500 M03               ; 3500 dev/dk, mili çalıştır
G00 X0 Y0 Z50            ; Hızlı konumlandırma
G00 Z5 M08               ; Güvenli yüksekliğe in, soğutucuyu aç
G01 Z-5 F80              ; Derinliğe in
G01 X100 F200            ; X yönünde kes
G00 Z50 M09              ; Geri çık, soğutucuyu kapat
M05                      ; Mili durdur
M30                      ; Program sonu
%
```

---

## 🛠️ CAM Yazılımları: "Strateji Belirleme Motoru"

### Endüstriyel CAM Yazılım Karşılaştırması

| Yazılım | Güçlü Yön | Endüstri Kullanımı |
| :--- | :--- | :--- |
| **Mastercam** | Torna + freze entegrasyonu, yüksek hız işleme (HSM) | Kalıpçılık, havacılık |
| **Fusion 360 (Autodesk)** | Bulut tabanlı, tasarım+CAM entegre | KOBİ ve prototip üretim |
| **Siemens NX CAM** | Karmaşık 5-eksen, turbine ve kanat işleme | Havacılık, savunma sanayii |
| **ESPRIT** | Tornalama ve İsviçre tarlası | Hassas tıbbi parça üretimi |

### Kritik CAM Stratejileri
- **Yüksek Hız İşleme (HSM/HFM):** Kesicinin hep aynı talaş yükünü alacağı şekilde yol hesaplanır. Kesici daha az ısınır, tezgah ömrü uzar.
- **Trochoidal Milling:** Dar kanallarda dairesel yörünge ile ilerleme. İfade ettiği etki: tam slot yerine dairesel bir iz bırakarak ısı yükünü %60 azaltır.
- **Rest Machining:** Önceki büyük kesicinin ulaşamadığı köşeleri küçük takımın otomatik tespit edip temizlemesi.

---

## 💻 Dijital Entegrasyon (Akıllı Üretim)
1. **DNC (Direct Numerical Control):** Programların USB yerine ağ (Ethernet/FANUC FOCAS) üzerinden tezgahlara otomatik dağıtılması. Hata riski ve zaman kaybı minimize edilir.
2. **MES Entegrasyonu:** Tezgahın çalışma verisi (spindle yükü, ivme, sıcaklık) MES (Manufacturing Execution System) yazılımlarına anlık aktarılır, OEE hesaplamaları otomatikleşir.
3. **Simülasyon ve Çarpışma Tespiti:** CAM yazılımlarındaki sanal tezgah ortamı, kesicinin, kovanın veya bağlama aparatının birbirine çarpma ihtimalini %100 öngörür.

---

## ⚠️ Programlama Hataları ve Kritik Riskler
- **Sıfır Nokta Hatası (WCS Shift):** G54 sıfır noktası yanlış tanımlanmışsa parça bitmeden önce takım bağlama aparatına çarpar; tezgah hasarı kaçınılmazdır.
- **Takım Çarpışması (Tool Crash):** G00 hızlı hareketinde Z yüksekliği yetersiz bırakıldığında kesicinin parçaya dalar. Sonuç: kırık kesici, bozuk parça, hasar görmüş mil.
- **Yanlış Takım Çapı Tanımı:** D offset'i yanlış girilmiş **D=10** yerine **D=1** yazılması tüm kompanzasyon hesabını bozar.

---

## 🚀 Meta-Mühendislik Vizyonu
- **AI Destekli CAM:** Parça geometrisini okuyup en uygun kesme stratejisini, takım seçimini ve ilerleme hızlarını saniyeler içinde öneren üretken AI modelleri (örn. Machina Labs).
- **Digital Twin NC Simulation:** Gerçek tezgahın fiziksel ikizinde program çalıştırılır; titreşim, takım aşınması ve enerji tüketimi simüle edilerek optimize edilir.

---
*Sanayi 1001: Kodu yazan beyin, talaşı çıkaran çelik — ikisi ayrılamaz.*
