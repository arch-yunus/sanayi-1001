# 🏗️ Sanayi 1001: Endüstriyel Bilgi Bankası ve Meta-Mühendislik Platformu

![Status](https://img.shields.io/badge/Versiyon-1.4.0_PRO_PLUS-blue.svg) ![License](https://img.shields.io/badge/Lisans-MIT-green.svg) ![Scope](https://img.shields.io/badge/Kapsam-Global_End%C3%BCstriyel_Standartlar-orange.svg)

## 📑 Stratejik Vizyon ve Operasyonel Misyon

**Sanayi 1001**, geleneksel sanayi sitelerinin ve devasa Organize Sanayi Bölgelerinin (OSB) derinliklerinde yatan "örtük" ampirik tecrübelerin (tacit knowledge), modern mühendislik disiplinlerinin sarsılmaz teorisiyle entegre edildiği, dünyanın ilk ve en kapsamlı açık kaynaklı **Endüstriyel Teknik Bilgi Bankası (Whitepaper)** ekosistemidir. Bu platform, yalnızca makineleri ve aletleri listelemekle kalmaz; demire form veren, metali eriten ve mekatronik sistemlere can veren üretim ruhunun anatomisini, tüm teorik denklemleri ve sahada yaşanmış kanlı/yağlı tecrübelerle sentezleyerek belgeler.

Misyonumuz; akademik teorilerin laboratuvarlardan çıkıp atölye zeminindeki "yağlı gerçeklikle" yüzleştiği sınırları şeffaflaştırmak, küresel üretim standartlarını (ISO, DIN, ANSI) anlaşılır kılmak ve nihayetinde "üretim hatası (Defect)" ile "kaza (Incident)" kelimelerini sanayi sözlüğünden silmeyi hedefleyen tam donanımlı bir **Operasyonel Yönetim Rehberi** inşa etmektir. Bir ustanın el becerisiyle, bir yüksek mühendisin CAD/CAM vizyonunu tek bir ekranda, tek bir lisanda buluşturan yegane köprü bu kütüphanedir.

---

## 🏛️ Teknik Taksonomi: Endüstriyel Disiplinler ve Alt Birimler

Sistem, muazzam büyüklükteki endüstriyel ekosistemi spesifik olarak 9 ana dikey hiyerarşi (Domain) altında kategorize etmektedir. Her bir modül, endüstriyel tasarım sıfır hata prensibine, maksimum verimliliğe ve termodinamik sürdürülebilirliğe hitap eden kendi içindeki sayısız alt kırılımı haritalandırmaktadır.

### ⚙️ 1. İmalat Teknolojileri ve Makine Ekosistemi
İmalat, insanlığın maddeyi kendi iradesi doğrultusunda şekillendirme sanatıdır. Bu kategori, talaşlı ve talaşsız imalat süreçlerinin fiziksel sınırlarını, malzemeye nüfuz eden kesici takımların geometrisini ve bu işlemleri icra eden konvansiyonel veya otonom sistemlerin operasyonel limitlerini detaylandırır. Makinenin çalışma rejiminden titreşim sönümleme dinamiklerine kadar üretim parkurunun her bileşeni burada atomlarına ayrılır.
*   🗺️ **[Makine Taksonomisi ve Kataloğu](1-makine-parkuru-ve-üretim/Tezgah_Katalogu_ve_Siniflandirma.md):** Konvansiyonel tezgahların ve çok eksenli CNC üretim ünitelerinin rijitlik ve kapasite sınıflandırması.
*   📊 **[CNC VMC & Torna Mimarisi](1-makine-parkuru-ve-üretim/CNC_Dik_İsleme_Merkezi_101.md):** CNC eksen interpolasyonları, servo tahrikli otonomasyon mekanizmaları ve üretim algoritmaları.
*   💾 **[G-Code Programlama ve CAM Yazılımları](1-makine-parkuru-ve-üretim/CNC_Programlama_G_Code_ve_CAM_Yazilimlari.md):** G/M kod anatomisi, takım yolu optimizasyonları ve Yüksek Hızla İşleme (HSM/Trochoidal) stratejileri.
*   🌀 **[Wire EDM & Elektro-Erozyon](1-makine-parkuru-ve-üretim/Tel_Erozyon_ve_Mikronluk_Kalıp_Uretimi.md):** Kıvılcım plazması üzerinden temassız gerçekleşen mikron seviyesindeki aşındırma ve kalıp üretim dinamiği.
*   ✨ **[Taşlama ve Yüzey Bitirme Süreçleri](1-makine-parkuru-ve-üretim/Taslama_Tezgahlari_ve_Yuzey_Bitirme_Teknolojileri.md):** Ekstrem ölçü hassasiyeti (tolerans) ve aşındırıcı disk mekaniği ile oluşturulan "Ayna Yüzey" (Ra 0.1) normları.
*   📝 **[Fiber Lazer & CNC Abkant Büküm](1-makine-parkuru-ve-üretim/Lazer_Kesim_ve_Abkant_Pres_Sac_Isleme.md):** Lazer ışınının termal kesim optimizasyonu ve saç malzemenin elastik geri esneme (Spring-back) analizleri.
*   🗳️ **[Plastik Enjeksiyon Termodinamiği](1-makine-parkuru-ve-üretim/Plastik_Enjeksiyon_ve_Seri_Uretim_Mekanigi.md):** Polimerlerin eriyik akış simülasyonu, soğuma çevrimleri ve basınç tutma teorileriyle seri üretim kalıplaması.
*   🧰 **[Manuel Atölye Ekipmanları Dizini](1-makine-parkuru-ve-üretim/El_Aletleri_ve_Atolye_Ekipman_Katalogu.md):** Alyan takımlarından havalı somun sıkmalara, mikro-kalibrasyonlu tork anahtarlarına kadar atölyenin temel kas donanımı.
*   🏢 **[Nadir Operasyonlar ve Özel Makine Sistemleri](1-makine-parkuru-ve-üretim/Nadir_Tezgahlar_ve_Ozel_Operasyonlar_Katalogu.md):** Ağır sanayinin vazgeçilmezleri olan Broşlama, Honlama, devasa Borverk işlemleri ve derin delik açma (Gun Drilling) prosesleri.

### 🔩 2. Kinematik Sistemler ve Termodinamik
Hareketin doğuş noktası ve iletimin kusursuz doğası bu bölümde incelenmektedir. Enerjinin form değiştirerek torka dönüştüğü termik odalardan, bu torku istenilen devre veya basınca ulaştıran komplike aktarım organlarına kadar tüm mekanik senfoni bu dikeyin merkezini oluşturur. Akışkanlar mekaniği ve tribolojik eşleşmeler hesaplanarak sistem ömürleri öngörülür.
*   🔥 **[Termik Motor Temelleri (ICE Teorisi)](2-mekanik-ve-motor/Icten_Yanmali_Motor_Temelleri.md):** Sıkıştırma-ateşleme, egzoz-emme çevrimlerinin ideal denklemleri, blok ve piston dinamiği.
*   ⏱️ **[Mekanik Senkronizasyon Disiplini](2-mekanik-ve-motor/Triger_ve_Zamanlama_Sente_Atlamasi_101.md):** Subap zamanlaması (Timing), milisaniyelik kam-krank faz korelasyon analizleri ve mekanik çakışma (sente) riskleri.
*   ⚙️ **[Şanzıman Mimarisi ve Tork Dağılımı](2-mekanik-ve-motor/Sanziman_Sistemleri_ve_Diferansiyel_Mekanigi.md):** Aktarma dişli oranları, planet sistem mekaniği ve yanal ivmelenme anındaki diferansiyel kilit dinamiği.
*   🌪️ **[Aşırı Besleme Kuvvetleri (Turboşarj)](2-mekanik-ve-motor/Turbo_ve_Asiri_Besleme_Sistemleri.md):** Atık egzoz basıncının geri kazanımıyla silindirlere basılan cebri havanın akışkanlar termodinamiğindeki yeri.

### ⚡ 3. Endüstri 4.0, Otomasyon ve Mekatronik Bütünleşme
Klasik röleli sistemlerin yerini yapay zeka destekli otonom sinir ağlarına bıraktığı yeni endüstriyel çağ. Fabrika zeminindeki algılayıcıların topladığı mikrosaniyelik ham verinin (Big Data), merkezi sunucularda işlenerek anlık olarak aktüatörlere, servo motorlara ve endüstriyel robotlara karar (Decision) olarak geri bildirilmesi sürecinin mimarisidir. Donanım ve yazılımın birbirine etle tırnak gibi kaynaştığı "Mekatronik" sistemlerdir.
*   🧠 **[Mantıksal Programlama (PLC) ve SCADA](3-otomasyon-ve-elektrik/PLC_ve_Kumanda_Panosu_101.md):** Ladder ve SCL algoritmaları üzerinden devasa tesislerin merkezi otonom kumanda topolojileri.
*   📡 **[Sensör Füzyonu ve Sinyal Analizi](3-otomasyon-ve-elektrik/Endustriyel_Sensor_Fuzyonu_ve_Sinyal_Isleme.md):** Analog/Dijital girişlerdeki gürültüyü sönümleyerek PLC algoritmalarına net akış sağlayan geri besleme (Feedback) filtresi.
*   🕸️ **[Endüstriyel Veri Yolu Sistemleri (Fieldbus)](3-otomasyon-ve-elektrik/Endustriyel_Haberlesme_Protokolleri_ve_Veri_Yolları.md):** Gecikmesiz (Real-time) veri transferini sağlayan Profinet, EtherCAT ve Modbus kritik ağ bağlantıları.
*   🤖 **[Endüstriyel Robotik ve Mekatronik](3-otomasyon-ve-elektrik/Endustriyel_Robotik_ve_Mekatronik_Sistemler.md):** 6-Eksenli robot kol kinematiği, ters/ileri hesaplamalar, RAPID tabanlı kodlama mimarisi ve ISO 10218 insan-robot (Cobot) güvenlik limitleri.
*   ⚡ **[Elektrik Motorları ve Frekans Sürücüleri](3-otomasyon-ve-elektrik/Elektrik_Motorlari_ve_Frekans_Suruculeri.md):** AC/DC asenkron, Servo hız hassasiyetleri, Adım motorları ve Inverter (VFD) teknolojisi üzerinden yapılan kübik güç optimizasyonları.
*   🔌 **[Enerji Kalitesi ve Elektrik Dağıtımı](3-otomasyon-ve-elektrik/Enerji_Kalitesi_ve_Fabrika_Elektrik_Dagitimi.md):** Fabrikanın enerji omurgası; kuru tip trafo merkezleri, reaktif güç (Cos φ) kompanzasyon panoları ve şebekeyi kirleten harmoniklerin aktif filtrasyonu.
*   💧 **[Hidrolik ve Pnömatik Sistemler](3-otomasyon-ve-elektrik/Hidrolik_ve_Pnomatik_Sistemler.md):** Pascal yasası üzerinden tonlarca ağırlığın basınca duyarlı valf ve pistonlarla milimetrik hareket transferi, sıkıştırılmış hava kontrolü.
*   🚿 **[Endüstriyel Boru ve Tesisat Sistemleri](3-otomasyon-ve-elektrik/Endustriyel_Boru_Tesisat_ve_Akiskan_Sistemleri.md):** Tesisat hatlarındaki (Buhar, Su, Gaz) basınç direnç parametreleri, flanş-vana bağlantıları ve global P&ID şematik sembolojisi.

### 🧪 4. Metalürji Teorisi, Yüzey Koruma ve Malzeme Bilimi
Doğadan elde edilen inorganik alaşımların insan eliyle işlenmeden önce ısı, basınç ve kimyevî reaksiyonlara tabi tutularak mukavemet sınırlarının en üst raddeye çıkarılması sanatıdır. Bir parçanın ne kadar dayanacağı, o malzemeye atanan atomik karbon bağlarına ve yüzeyini kaplayan kimyasal kalkan tabakasına bağlıdır. Doğru malzeme seçilmeden doğru tasarım yaşatılamaz.
*   👨‍🏭 **[Kaynak Metalürjisi ve Ark Fiziği](4-malzeme-ve-metalurji/Kaynak_Teknolojileri_ve_Isil_Islem.md):** Ergitme ve dolgu işlemleri sırasında kristalizasyon bozuklukları, moleküler difüzyon ve tahribatsız (NDT) birleştirme standartları.
*   🌡️ **[Faz Dönüşümleri (Dinamik Isıl İşlem)](4-malzeme-ve-metalurji/Isil_Islem_Teknikleri_ve_Metal_Sertlestirme.md):** Termal şoklarla indüklenen Ostenit-Martenzit sertleştirilme evreleri, sementasyon ve gerilim giderme reçeteleri.
*   🔥 **[Döküm Teknolojileri ve Katılaşma](4-malzeme-ve-metalurji/Dokum_Teknolojileri_ve_Modelcilik_Hatalari.md):** Döküm yolluğunun akışkan analizi, kum kalıplamada gaz emisyonundan doğan boşluk (Shrinkage) hatalarının önlenmesi.
*   🧬 **[Alaşım Spesifikasyonları ve Seçim Algoritması](4-malzeme-ve-metalurji/Celik_Kodlari_ve_Malzeme_Secim_Rehberi.md):** DIN/ISO onaylı malzeme sınıfları (4140, 7131, 304 Paslanmaz), hafifletme alaşımları ve akma gerilim sınırları.
*   🧪 **[Endüstriyel Yüzey İşlem ve Kaplama](4-malzeme-ve-metalurji/Endustriyel_Yuzey_Islem_ve_Kaplama_Teknolojileri.md):** Atmosferik pasifize edici sıcak daldırma Galvanizasyon, yüzey aşınma kalkanı olan Sert Krom, alüminyuma estetik ve tokluk katan Eloksal prosesleri.

### 👨‍🔧 5. Operasyonel Kültür ve Davranışsal Disiplin
Makinelerin yazılımsal beyinleri olsa da onlara yön veren yegane unsur insanın inisiyatifi, sezgisi ve asırlık atölye tecrübesidir. Bu kategori, bir tornacının metalin çıkardığı sesten anormalliği hissettiği "örtük bilginin" bilimsel lisanla kodlanmasını, farklı usta hiyerarşilerinin görev sınırlarını ve nesilden nesle aktarılan usta-çırak genetiğini açıklamaktadır.
*   🎖️ **[Endüstriyel Branşlar Yeterlilik Matrisi](5-sanayi-kulturu-ve-jargon/Usta_Turleri_ve_Gorev_Tanimlari.md):** Kaynakçıdan tesviyeciye, kalıpçıdan otomasyoncuya uzanan mesleki kolların limitleri.
*   🌳 **[Dikey Ustalık Sınıfları (Makromühendisler)](5-sanayi-kulturu-ve-jargon/Nis_Usta_Branslari_ve_Uzmanlik_Haritasi.md):** Arıza durumunda başvurulan "Son İnstans" uzmanları: Kapakçı, Blokçu, Balansçı ve Turbo revizyon profesörleri.
*   🤝 **[Mentorluk ve Gelenek Transferi (Hiyerarşi)](5-sanayi-kulturu-ve-jargon/Sanayi_Hiyerarsisi_ve_Usta_Cirak_Kulturu.md):** Bilginin kitaplardan değil, "işin başındayken" kazanıldığı gözlemsel ve eylemsel nöral eğitim modeli.
*   📖 **[Kritik Sanayi Terminolojisi Sözlüğü](5-sanayi-kulturu-ve-jargon/Sanayi_Terimleri_Sozlugu.md):** Sahada kullanılan yoğun argon jargonunun global makine mühendisliği terimleriyle haritalandırılmış kusursuz indeksi.

### 📏 6. Metroloji, Tolerans Fiziği ve Kalite Güvence
Üretilen parçanın iki farklı lokasyon ve sıcaklıkta (örneğin İstanbul'da işlenip Tokyo'da montaja girmesi durumu) aynı boyutsal gerçekliği sağlaması gerekir. Bir parçayı çizmek ile o parçayı gerçek fizik kuralları içinde onaylamak arasındaki hassas eşik bu ana koldur. Geometrik boyutlandırma, lazer prob ile kalibrasyon ve global standartlarla uygunluğun son onayı burada verilir.
*   📐 **[Metrolojik Enstrümanlar (Kumpas/CMM)](6-olcme-ve-kalite-kontrol/Olcme_Aletleri_ve_Tolerans_Fizigi_101.md):** Kalibrasyonlu mikrometrelerin okuma limitleri, CMM makinelerinin uzaysal nokta alma (Point Cloud) analizleri ve sıcaklık kompanzasyonlu okumalar.
*   🔬 **[Uluslararası Teknik Standartlar (ISO/DIN)](6-olcme-ve-kalite-kontrol/Teknik_Standartlar_ve_Tolerans_Tablolari.md):** Mil ve boşluk tolerans geçmeleri (H7/g6 vb.), Geometrik Boyutlandırma (GD&T) ve parçanın temas noktalarındaki pürüzsüzlüğünü belirleyen Ra (Roughness) standartları.

### 🛠️ 7. Operasyonel Sürdürülebilirlik, Bakım Felsefesi ve Termodinamik Tahliye
Milyonlarca dolarlık üretim sistemlerinin bir gecede hurdaya dönmemesi için sürekli gözetlenmesi, hareketin yarattığı sürtünmenin ve atık ısının sistemden derhal uzaklaştırılması mecburidir. Bu süreç reaktif (bozulunca düzelt) değil, proaktif (bozulmadan engelle) yöntemlere dayanarak fabrikanın hayatta kalma süresini belirler.
*   💧 **[Triboloji, Yağlama Çözümleri ve Rulman Fiziği](7-bakim-ve-onarim/Rulmanlar_Kayislar_ve_Yaglama_Teknolojileri.md):** Rulman kinematik analizleri, devir bazlı viskoz sıvı (yağ) tutunmaları ve erken yorulmayı gösteren titreşim spektrumlarının sönümlenme yaklaşımları.
*   ❄️ **[Endüstriyel Soğutma ve Isı Dağıtımı](7-bakim-ve-onarim/Endustriyel_Sogutma_ve_Isi_Transfer_Sistemleri.md):** Kompresör destekli Chiller üniteleri, buharlaşmalı Soğutma Kuleleri, Plakalı eşanjörler ve prosesin termal sınırda tutularak makinelerin erimesinin engellenmesi.

### 📈 8. Atölye Yönetimi ve Verimlilik (Yalın Üretim Disiplini)
Daha çok makinenin daha çok üretim yapacağı yanılgısı bu bölümde yıkılır. Asıl verimlilik, makinenin başında geçen o gereksiz "beklemelerin", hatalı stokların ve plansız duruşların yok edilmesidir. Toyota felsefesiyle gelişen bu doktrin, operasyonlardaki katma değersiz her hamleyi (İsraf) teşhis edip sistemin sadece katma değere odaklandığı felsefik ve pratik dönüşümü hedefler.
*   🎯 **[Yalın Üretim, 5S Metodolojisi ve Kaizen](8-yonetim-ve-verimlilik/Yalin_Uretim_ve_5S_Atolye_Disiplini.md):** TPS (Toyota Üretim Sistemi) ışığında israf kalemleri (Muda), Seiri-Seiton gibi 5S görsel atölye organizasyonu, Poka-Yoke ile hatanın fiziksel olarak engellenmesi ve Kaizen devrimleri.

### 🦺 9. İş Sağlığı, Güvenliği ve Kök Neden Analizi (İSG-OHS)
Hiçbir üretim kapasitesi veya ticari ciro hedefleri, tek bir parmağın kopmasından daha değerli görülemez. Risk yönetimi; ölüm veya yaralanmayla sonuçlanabilecek kazaları tehlike anından çok önce, daha makine dizayn evresinde nötralize etme bilimidir. İnsanın reaksiyon hızına ve hata payına bağlı olmayan sıfır toleranslı prosedürler topluluğudur.
*   🔒 **[İSG Risk Yönetimi ve Kaza Önleme](9-is-guvenligi-ve-risk/ISG_Risk_Yonetimi_ve_Kaza_Onleme.md):** Risk skoru hesaplaması (Heinrich Üçgeni teorisi), ölümcül bakımlarda uygulanan 5 kademeli Enerji İzolasyonu (LOTO) prosedürü ve KKD direktiflerinden oluşan güvenlik anayasası.

---

## 🏗️ Yetkinlik Sınırları ve Mesleki Evrim Matrisi (Kariyer Yolculuğu)

Endüstriyel dünyada itibari değerler; unvanlardan ziyade sahada üstlenilen teknik sorumluğun hacmi, kriz anındaki karar verme soğukkanlılığı ve kompleks arızaların teşhisinde kullanılan analitik zeka ile doğru orantılıdır. Aşağıdaki matris bu ağır basamakları netleştirir.

| Hiyerarşik Seviye | Uluslararası Akademik Karşılık | Sahadaki Yetki, Yükümlülük ve Operasyonel Derinlik |
| :--- | :--- | :--- |
| **Çırak (Apprentice)** | *Assistant Operator & Trainee* | Atölye ekosisteminin temellerini izleyerek kavrayan, temizlik ve hazırlık süreçlerinden sorumlu, İSG kurallarını içselleştiren ilk aşama üretim adayıdır. Görevi "yapmak" değil "nasıl yapıldığını özümsemek" olan geleceğin mimarıdır. |
| **Kalfa (Journeyman)** | *Certified Production Technician* | Makinenin dilini çözmüş, belirlenen SOP (Standart Operasyon Prosedürü) sınırları dâhilinde kimseye ihtiyaç duymadan üretim (talaş kaldırma, montaj, kaynak) yapabilen yetkin personeldir. Rutin işlerde %100 otonom çalışır. |
| **Usta (Master Craftsman)** | *Senior Tech Lead & Problem Solver* | Sadece parçayı üreten değil; "Neden hatalı çıktı?" sorusuna anında teşhis (Troubleshooting) koyabilen, üretim süreçlerini en baştan (Setup) dizayn edebilen ve kalfalara liderlik eden karar verici merciidir. Sanayinin ana direğidir. |
| **Piri Sani (Grandmaster)** | *Visionary Consultant / Meta-Engineer* | Milyonda bir görülen sistemik çökmeleri önceden koklayan, imkansız denilen kurtarma operasyonlarını bizzat yöneten, teknik sınırları baştan yazan, yeni tasarımları onaylayan ve sadece bilgisi için kapısına gidilen "Duayen" lider. |

---

## 🤝 Katılımcı Dokümantasyon Standardı ve Açık Kaynak Gücü

**Sanayi 1001** projesi, durağan bir kitap değil, "Kaizen" prensibiyle global endüstri tarafından sürekli güncellenen ve sınanan yaşayan bir ağacın ta kendisidir. CMM makinesinin kalibrasyon verisinden, eloksal banyosunun kimyasal sırrına, yeni nesil IO-Link protokolünden en dipteki çıraklık psikolojisine kadar kütüphanemizi derinleştirecek, hatalarını filtreleyecek olan şey bu ortak "Meta-Mühendis" aklıdır. 

Sizden beklenen; atölyenin içindeki "Yağlı Saha Tecrübesini", bilgisayar ekranındaki o acımasız ve kusursuz "Akademik Çıkarım" ile harmanlayarak birleştirmeniz ve geleceğin ustalarına, mühendislerine sarsılmaz bir miras olarak (Pull Request yoluyla) aktarmanızdır.

---
**Lisans Modeli:** MIT Open Industrial Documentation Initiative  
**Ortak Operatör Tipi:** Geliştiriciler, Baş Mühendisler, Makine Mimarları ve Evrensel Meta-Mühendisler Ağı