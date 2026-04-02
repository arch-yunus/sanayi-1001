# Endüstriyel Robotik ve Mekatronik Sistemler (Industrial Robotics & Mechatronics)

## 🎯 Yönetici Özeti
Mekatronik; makine mühendisliği, elektronik, bilgisayar bilimi ve kontrol teorisinin kesişiminde doğan ve modern üretim sistemlerinin mimarını şekillendiren disiplinler arası bir mühendislik dalıdır. Endüstriyel robotlar bu disiplinin en yüksek tezahürüdür. Bu rehber; endüstriyel robot anatomisinden, hareket kinematik algoritmalarından ve gerçek fabrika entegrasyonundaki yazılım katmanlarına kadar uzanan robotik-mekatronik ekosistemi belgeler.

---

## ⚙️ Endüstriyel Robot Anatomisi

### 1️⃣ Robot Sınıfları ve Uygulama Alanları

| Robot Tipi | Eksen Sayısı | Güçlü Yön | Tipik Uygulama |
| :--- | :--- | :--- | :--- |
| **SCARA** | 4 | Yüksek hız, yatay düzlem | Montaj, pick-and-place |
| **Eklemli Kol (Articulated)** | 6–7 | Tam serbestlik, karmaşık hareket | Kaynak, boyama, CNC yükleme |
| **Delta/Paralel** | 3–4 | Ultra yüksek hız | Gıda sektörü paketleme |
| **Kartezyen/Portal** | 3 | Uzun mesafe, yüksek yük | Depo otomasyonu, CNC transfer |
| **Collaborative (Cobot)** | 6–7 | İnsan ile güvenli çalışma | Küçük seri ve esnek montaj |

### 2️⃣ Robot Kinematik Temelleri
- **İleri Kinematik (Forward Kinematics):** Eklem açılarından (θ₁...θₙ) uç efektörün (end-effector) uzaydaki pozisyon ve oryantasyonunu hesaplama (Denavit-Hartenberg DH parametreleri).
- **Ters Kinematik (Inverse Kinematics):** Uç efektörün hedef pozisyonundan gerekli eklem açılarını geriye hesaplama. Çoklu çözüm ve tekillik (singularity) yönetimi gerektirir.
- **Jacobian Matrisi:** Robot kolunun eklem hızlarını uç efektör hızına dönüştüren ve kuvvet/tork dağılımını modelleyen temel matris.

---

## 🛠️ Endüstriyel Saha Gerçekleri

| Atölye Terimi | Teknik Karşılığı | Operasyonel Yansıması |
| :--- | :--- | :--- |
| **Singularity (Tekillik)** | Jacobian matrisinin rank kaybı | Robot kolu belirli bir pozisyonda kontrolsüz hareket eder; acil durum. |
| **Payload (Yük Kapasitesi)** | Maksimum taşınabilir kütle | Nominal yükü aşmak servo motor hasarına ve yörünge sapmalarına yol açar. |
| **Teach Pendant** | El Programlama Birimi | Operatörün robotu adım adım öğrettiği/programladığı el bilgisayarı. |
| **Güvenlik Kafesi (Safety Fence)** | Physical Safeguarding | ISO 10218-2 kapsamında, insan-robot ayrım güvenlik bariyeri. |
| **Force Torque Sensörü** | F/T Sensor | Montaj kuvvetini hisseden ve parçanın doğru yerine yerleştiğini doğrulayan sensör. |

---

## 💻 Yazılım ve Dijital Katman
### Robot Programlama Dilleri
- **RAPID (ABB):** `MoveL`, `MoveJ`, `Set DO10` gibi hareket ve sinyal komutları.
- **KRL (KUKA):** `PTP`, `LIN`, `ARC` komutlarıyla KUKA manipülatörler.
- **Universal Robots Script (URScript):** Cobot'lar için Python-benzeri sözdizimi.

### Örnek ABB RAPID Kodu
```rapid
MODULE MainModule
  CONST robtarget pHome := [...];       ! Ev pozisyonu
  CONST robtarget pWeld := [...];       ! Kaynak noktası
  
  PROC main()
    MoveJ pHome, v1000, z50, tool0;     ! Ev pozisyonuna git
    MoveL pWeld, v100, fine, tWeldGun;  ! Doğrusal kaynak hareketi
    SetDO doWeld, 1;                    ! Kaynak arkını başlat
    WaitTime 2;                         ! 2 sn bekle
    SetDO doWeld, 0;                    ! Kaynağı durdur
    MoveJ pHome, v1000, z50, tool0;     ! Geri dön
  ENDPROC
ENDMODULE
```

### ROS (Robot Operating System) Entegrasyonu
- Açık kaynak çerçevesi olan ROS, sensörden gelen verileri (kamera, LiDAR, F/T) işleyerek planlama algoritmalarına (MoveIt!) besler. Akademik AR araştırmadan sanayi cobot entegrasyonuna kadar geniş ekosistemi vardır.

---

## ⚠️ Endüstriyel Robot Güvenliği (ISO 10218 / TS EN ISO 10218)
- **Safety-Rated Monitored Stop:** İnsan güvenlik bölgesine girdiğinde robot kolu tamamen durur (enerji kesilmez, pozisyon korunur).
- **Speed and Separation Monitoring:** Lazer tarayıcılar insanın mesafesine göre robot hızını kademeli olarak düşürür.
- **Power and Force Limiting (Cobot):** Cobotların temas kuvveti belirli bir eşiği (örn. 150 N) aştığında otomatik durması. İnsan kırılganlığı profiline göre ISO/TS 15066 standartlarıyla hesaplanır.

---

## 🚀 Meta-Mühendislik Vizyonu
- **Swarm Robotics:** Küçük, birbirleriyle iletişim kuran yüzlerce robotun merkezi bir bilgisayar olmadan kolektif zeka ile bir fabrika görevini tamamlaması (Biyolojik ilham: Arı kovanı).
- **Morphing End-Effectors:** Vakum, pens ve kaynak torcu fonksiyonlarını tek bir uç efektörde saniyeler içinde değiştiren akıllı multi-fonksiyonel robotik eller.
- **Neuromorphic Control:** Beynin nöron devre mimarisini taklit eden çipler (Intel Loihi) ile gerçek zamanlı, ultra düşük gecikme süreli robot kontrol sistemleri.

---
*Sanayi 1001: İnsan zekasını metal kola, dijital sinir sistemine aktarıyoruz.*
