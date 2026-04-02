# 🏗️ Sanayi 1001: Endüstriyel Teknik Bilgi Bankası

![Sanayi 1001 Hero Banner](assets/hero_banner.png)
![Status](https://img.shields.io/badge/Versiyon-1.5.0-blue.svg) ![License](https://img.shields.io/badge/Lisans-MIT-green.svg) ![Kapsam](https://img.shields.io/badge/Kapsam-End%C3%BCstriyel_Standartlar-orange.svg)

## 📑 Hakkında ve Temel Amacımız

**Sanayi 1001**, sanayi bölgelerindeki geniş pratik tecrübeler ile üniversitelerde okutulan teorik mühendislik temellerini aynı çatı altında birleştirmeyi amaçlayan kapsamlı ve açık kaynaklı bir teknik bilgi bankasıdır. Çeşitli imalat alanlarında, montaj hatlarında ve kalite kontrol tesislerinde edinilmiş saha tecrübelerini, küresel kabul görmüş standartlara (ISO, DIN, ANSI vb.) uygun şekilde standardize ederek belgelendirmeyi hedefleriz.

Geleneksel olarak atölyelerde usta-çırak ilişkisiyle sözlü olarak aktarılan ve zamanla kaybolma veya yozlaşma riski taşıyan endüstriyel birikimleri dijital ve kalıcı bir formata taşıyoruz. Bu depo, imalat mühendisliği, malzeme bilimi, otomasyon prosesleri ve iş güvenliği gibi birbirine bağlı çok sayıdaki disiplini, anlaşılır bir yapıda sunar. Amacımız, makine mühendisliği öğrencilerine, stajyerlere, sahada çalışan teknikerlere, yeni işe başlayan mühendislere ve hatta üretim tesislerini yöneten yöneticilere güvenilir bir referans ve başvuru kaynağı sunmaktır.

Bu kütüphane sadece tezgâhların isimlerini ve fonksiyonlarını anlatmakla yetinmez. Hangi işlemin fiziki olarak nasıl gerçekleştiğini, bu işlem sırasındaki termodinamik veya kinematik etkileri, malzemelerin bu etkilere verdiği tepkileri ve en önemlisi işi yaparken dikkat edilmesi gereken güvenlik ve kalite kriterlerini objektif ve teknik bir lisanla açıklamaktadır.

---

## 👨‍💻 Hedef Kitle ve Kullanım Kılavuzu

Bu ansiklopedi, sanayi ve üretim sektörüyle temas halinde olan farklı uzmanlık seviyelerindeki bireylerin faydalanması için tasarlanmıştır:
*   **Mühendislik Öğrencileri ve Yeni Mezunlar:** Teorik bilgilerin sahada (dökümhane, talaşlı imalat atölyeleri, kalite kontrol laboratuvarları) nasıl uygulandığını ve hangi teknik jargona dönüştüğünü görmek için okuyabilirler.
*   **Teknisyen ve Operatörler:** Kullandıkları makinelerin arka plandaki teorik işleyişini kavramak, tolerans aralıklarının mühendislik önemini anlamak ve teknik çizimlerle pratik operasyonları daha uyumlu hale getirmek için faydalanabilirler.
*   **Planlama ve Üretim Yöneticileri:** Fabrikadaki farklı departmanların (Örn: Otomasyon ile Dökümhane) birbirine nasıl bağlandığını kavramak ve "Yalın Üretim" gibi süreçleri tesise entegre ederken genel bir vizyon elde etmek için kullanabilirler.

Dokümanları okurken, her makalenin içerisinde yer alan İSG (İş Sağlığı ve Güvenliği) uyarılarına ve uluslararası standart tablolarına özellikle dikkat edilmesi önerilir. 

---

## 🏛️ Endüstriyel Disiplinler ve Kategoriler

Sanayi 1001 projesinde yer alan dokümanlar, üretim döngüsünde kavram karmaşasını önlemek adına spesifik disiplinlere ayrılarak 9 ana kategori altında toplanmıştır. Her bir kategori, kendi alanındaki alt kırılımlara ve özel rehberlere yönlendirme yapmaktadır.

### ⚙️ 1. İmalat Teknolojileri ve Makine Ekosistemi
İmalat bölümü, ham malzemenin işlenerek nihai ürüne dönüştüğü tüm fiziksel süreçleri kapsar. Parçadan talaş kaldırarak (freze, torna), malzemenin formunu değiştirerek (büküm, pres) veya malzemeyi eriterek şablonlama (enjeksiyon) yöntemiyle çalışan tüm konvansiyonel ve bilgisayar destekli (CNC) tezgâh modellerini içerir. Kesici takım seçimi, makine rijitliği, eksen sayıları ve imalat stratejilerinin incelendiği en kapsamlı bölümdür.
*   🗺️ **[Makine Taksonomisi ve Kataloğu](1-makine-parkuru-ve-üretim/Tezgah_Katalogu_ve_Siniflandirma.md):** Sanayide bulunan tüm üretim tezgâhlarının kapasite sınıflandırması ve genel fonksiyonları.
*   📊 **[CNC VMC & Torna Mimarisi](1-makine-parkuru-ve-üretim/CNC_Dik_İsleme_Merkezi_101.md):** 3 ve 5 eksen CNC dik işleme merkezlerinin kızak yapısı, eksen limitleri ve çalışma geometrileri.
*   💾 **[G-Code Programlama ve CAM Yazılımları](1-makine-parkuru-ve-üretim/CNC_Programlama_G_Code_ve_CAM_Yazilimlari.md):** CNC ünitelerini çalıştıran G ve M kodlarının satır satır analizi ile CAM yazılımlarının işleme stratejileri.
*   🌀 **[Wire EDM & Elektro-Erozyon](1-makine-parkuru-ve-üretim/Tel_Erozyon_ve_Mikronluk_Kalıp_Uretimi.md):** Kesici takımın giremediği veya malzemenin çok sert olduğu durumlarda kullanılan elektriksel deşarj işleme teorisi.
*   ✨ **[Taşlama ve Yüzey Bitirme Süreçleri](1-makine-parkuru-ve-üretim/Taslama_Tezgahlari_ve_Yuzey_Bitirme_Teknolojileri.md):** Mikron seviyesinde (0.001 mm) pasolarla yapılan silindirik ve satıh taşlama mekanikleri ile yüzey pürüzlülük iyileştirilmesi.
*   📝 **[Fiber Lazer & CNC Abkant Büküm](1-makine-parkuru-ve-üretim/Lazer_Kesim_ve_Abkant_Pres_Sac_Isleme.md):** Yüksek güçlü lazer rezonatörleri ile metal kesimi ve pres makinelerindeki sac zımba basınç hesaplamaları.
*   🗳️ **[Plastik Enjeksiyon Termodinamiği](1-makine-parkuru-ve-üretim/Plastik_Enjeksiyon_ve_Seri_Uretim_Mekanigi.md):** Eriyik polimerin kalıp içerisine basılması, basınç tutma evreleri ve kalıp sıcaklık kontrolü prensipleri.
*   🧰 **[Manuel Atölye Ekipmanları Dizini](1-makine-parkuru-ve-üretim/El_Aletleri_ve_Atolye_Ekipman_Katalogu.md):** Tezgâh dışı kurulum süreçlerinde kullanılan sökme, takma ve bağlama el aletlerinin mühendislik değerlendirmesi.
*   🏢 **[Nadir Operasyonlar ve Özel Makine Sistemleri](1-makine-parkuru-ve-üretim/Nadir_Tezgahlar_ve_Ozel_Operasyonlar_Katalogu.md):** Ağır makine parçalarında (gemi motoru blokları, rüzgâr türbin kanatları) tercih edilen borverk, broşlama ve büyük ebatlı torna işlemleri.

### 🔩 2. Mekanik ve Motor Sistemleri
Mekanik sistemler, üretilen enerjinin veya hareketin bir kaynaktan diğerine verimli bir şekilde aktarılmasını inceler. Dinamik (hareketli) parçaların maruz kaldığı kuvvet analizleri, dişlilerin taşıdığı tork kapasiteleri ve içten yanmalı motorların temel termodinamik döngüleri bu alanda işlenmektedir. Ayrıca zamanlama mekanizmalarının ve tahrik organlarının kusursuz senkronizasyon gereksinimleri detaylandırılır.
*   🔥 **[İçten Yanmalı Motor Temelleri](2-mekanik-ve-motor/Icten_Yanmali_Motor_Temelleri.md):** Dört zamanlı Otto ve Dizel motor döngülerinin teorisi, silindir blok tasarımları ve kompresyon verimlilikleri.
*   ⏱️ **[Mekanik Senkronizasyon (Sente)](2-mekanik-ve-motor/Triger_ve_Zamanlama_Sente_Atlamasi_101.md):** Eksantrik milli ve krank mili konumlarının açısal bağıntısı, sente atlaması durumunda oluşan supap-piston çarpışma riskleri.
*   ⚙️ **[Şanzıman ve Diferansiyel Mekaniği](2-mekanik-ve-motor/Sanziman_Sistemleri_ve_Diferansiyel_Mekanigi.md):** Devri düşürerek torku maksimize etmeye yarayan dişli oranları denklemi ve planet dişli/diferansiyel sistemleri.
*   🌪️ **[Turbo ve Aşırı Besleme Sistemleri](2-mekanik-ve-motor/Turbo_ve_Asiri_Besleme_Sistemleri.md):** Yanma odasına harici havayı basınçlandırarak gönderen turboşarj ve süperşarj sistemlerinin akışkanlar basınç dinamiği.

### ⚡ 3. Otomasyon, Robotik ve Altyapı Sistemleri
Üretimin insan gücünden otonom sistemlere evrildiği süreçlerin, elektriksel ve mantıksal mimarisi bu bölümde yer alır. Fabrikanın elektrik altyapısından başlayarak, programlanabilir mantık kontrolörleri (PLC), endüstriyel robotların denetleyicileri ve sensörler ağı arasındaki iletişim hiyerarşisi açıklanır. Akışkan gücüne (hidrolik ve pnömatik) yön veren valf mekanizmaları ile bu sistemlerin otomasyonla haberleşmesi incelenir.
*   🧠 **[PLC ve Kumanda Panosu](3-otomasyon-ve-elektrik/PLC_ve_Kumanda_Panosu_101.md):** Elektronik sensörlerden gelen dijital ve analog sinyallerin röle sistemleriyle veya PLC yazılım bloklarıyla (Ladder) yorumlanması.
*   📡 **[Sensör Füzyonu ve Sinyal İşleme](3-otomasyon-ve-elektrik/Endustriyel_Sensor_Fuzyonu_ve_Sinyal_Isleme.md):** İndüktif, kapasitif veya optik sensörlerden gelen geri besleme verilerinin sistem tarafından hatalardan arındırılarak işlenmesi.
*   🕸️ **[Endüstriyel Veri Yolu Sistemleri](3-otomasyon-ve-elektrik/Endustriyel_Haberlesme_Protokolleri_ve_Veri_Yolları.md):** Modbus, Profinet ve EtherCAT gibi gecikmesiz veri transferi sağlayan iletişim standartları.
*   🤖 **[Endüstriyel Robotik ve Mekatronik](3-otomasyon-ve-elektrik/Endustriyel_Robotik_ve_Mekatronik_Sistemler.md):** 6 eksenli robot kollarının taşıma kapasiteleri, kartezyen hesaplamaları, takım sonu işleyicileri ve koruma çevrimleri.
*   ⚡ **[Elektrik Motorları ve Frekans Sürücüleri](3-otomasyon-ve-elektrik/Elektrik_Motorlari_ve_Frekans_Suruculeri.md):** Fabrikanın hareket kaynağı olan asenkron motorların çalışma kuralları ve bu motorların parametrik hız denetleyicileri olan VFD üniteleri.
*   🔌 **[Enerji Kalitesi ve Fabrika Elektrik Dağıtımı](3-otomasyon-ve-elektrik/Enerji_Kalitesi_ve_Fabrika_Elektrik_Dagitimi.md):** AG/OG trafoları, sistemdeki ısı kayıplarının önüne geçen reaktif güç kompanzasyon panoları ve harmonik gürültü filtreleri.
*   💧 **[Hidrolik ve Pnömatik Sistemler](3-otomasyon-ve-elektrik/Hidrolik_ve_Pnomatik_Sistemler.md):** Basınçlandırılan akışkanın valf bloklarıyla istenilen silindirlere yönlendirilmesi ile elde edilen yüksek tonajlı kuvvet hareketleri.
*   🚿 **[Endüstriyel Boru ve Tesisat Sistemleri](3-otomasyon-ve-elektrik/Endustriyel_Boru_Tesisat_ve_Akiskan_Sistemleri.md):** P&ID proje okuma prensipleri, yüksek basınç borularının flanş yapısı, malzeme seçimi ve proses akış denetimi valfleri.

### 🧪 4. Malzeme Bilimi ve Metalürji
İmalat sürecindeki en kritik unsur malzemeyi tanımaktır. Bir çeliğin içerdiği karbon miktarının malzemenin esnekliği ile olan ters ve sertliği ile olan doğru orantısı gibi temel prensipler bu alanın konusudur. Karbon dengesi değiştirilmiş yapıların kaynak işlemi, ısıtılıp aniden soğutularak kristal evresi değiştirilen alaşımlar, korozyon ile mücadele etmek için atılan kimyasal kaplama adımları geniş bir çerçevede ele alınmaktadır.
*   👨‍🏭 **[Kaynak Teknolojileri ve Ark Fiziği](4-malzeme-ve-metalurji/Kaynak_Teknolojileri_ve_Isil_Islem.md):** MIG, MAG ve TIG gibi ergitmeli kaynak yöntemleri, ısıdan etkilenen bölgedeki (HAZ) hatalar ve tahribatsız (NDT) birleştirme muayeneleri.
*   🌡️ **[Faz Dönüşümleri ve Isıl İşlem](4-malzeme-ve-metalurji/Isil_Islem_Teknikleri_ve_Metal_Sertlestirme.md):** Malzemenin aşınma direncinin kontrollü fırınlarda ostenitleştirme ve sementasyon gibi ısıl uygulamalar ile artırılması süreci.
*   🔥 **[Döküm Teknolojileri ve Hataları](4-malzeme-ve-metalurji/Dokum_Teknolojileri_ve_Modelcilik_Hatalari.md):** Kalıplama yöntemleri ve sıvı metalin kalıp içine dolarken yaşadığı çekme payı, boşluk bırakma (Shrinkage) sorunları.
*   🧬 **[Çelik Kodları ve Seçim Rehberi](4-malzeme-ve-metalurji/Celik_Kodlari_ve_Malzeme_Secim_Rehberi.md):** İmalatta en yaygın kullanılan alaşımlı mühendislik çeliklerinin (DIN 4140, 8620 vb.) kaba akma/kopma gerilimleri ve seçim standartları.
*   🧪 **[Endüstriyel Yüzey İşlem ve Kaplama](4-malzeme-ve-metalurji/Endustriyel_Yuzey_Islem_ve_Kaplama_Teknolojileri.md):** Oksidasyonu engellemek amacıyla uygulanan galvanizasyon, eloksal (alüminyum oksit) ve aşınmayı önleyen sert krom yöntemleri.

### 👨‍🔧 5. Sanayi Kültürü ve Mesleki Organizasyon
Donanım, süreç ve malzemenin ötesinde; fabrikada bütün bunları orkestra eden insan faktörünün rol tanımları bu dizinde ele alınmaktadır. Mühendisin yaptığı teknik çizimin makine operatörüne aktarımı, personelin tezgâh başındaki görev hiyerarşisi, kaliteyi belirleyen ustalık seviyeleri ve "alaylı" (saha eğitimi) kültürden gelen deyimlerin "okullu" (teorik) mesleki literatürle eşleştirilmesi bu bölümün işlevi olarak kurgulanmıştır.
*   🎖️ **[Usta Türleri ve Görev Tanımları](5-sanayi-kulturu-ve-jargon/Usta_Turleri_ve_Gorev_Tanimlari.md):** Üretim safhasında yer alan montaj ekiplerinin, tesviye elemanlarının, takım bağlama ustalarının çerçevelendirilmiş rolleri.
*   🌳 **[Niş Uzmanlık ve Branşlaşma](5-sanayi-kulturu-ve-jargon/Nis_Usta_Branslari_ve_Uzmanlik_Haritasi.md):** Revizyon (onarılıp yenileme) pazarı alanındaki dar uzmanlık dallarının (blok çatlağı kapakçıları, turbo balans uzmanları vb.) tanımı.
*   🤝 **[Sanayi Hiyerarşisi ve Mentorluk](5-sanayi-kulturu-ve-jargon/Sanayi_Hiyerarsisi_ve_Usta_Cirak_Kulturu.md):** Çırak düzeyinden ustabaşı makamına kadar uzanan mesleki büyüme eğrisi, beceri transfer metotları.
*   📖 **[Sanayi Terimleri Sözlüğü](5-sanayi-kulturu-ve-jargon/Sanayi_Terimleri_Sozlugu.md):** Atölye seviyesinde sesletilen makine terminolojisinin karşılıklı akademik makine elemanları indeksine entegrasyonu.

### 📏 6. Ölçüm ve Kalite Kontrol (Metroloji)
Bir parçanın makinede pürüzsüz görünerek çıkması o parçanın "doğru üretildiği" anlamına gelmez. Tasarımdaki boyutun, yüzey kalitesinin ve delik çaplarının uluslararası geçme tolerans limitleri dahilinde olup olmadığı, ancak kalibre edilmiş ölçüm araçlarıyla doğrulanabilir. Bu kategori, göz kararına yer bırakmayan endüstriyel boyutsal kalite standartlarını barındırır.
*   📐 **[Ölçüm Aletleri (Kumpas, Mikrometre)](6-olcme-ve-kalite-kontrol/Olcme_Aletleri_ve_Tolerans_Fizigi_101.md):** Analog okuma prensipleri, dijital mastarlar ve CMM (Koordinat Ölçüm Makineleri) gibi hassas laboratuvar elemanlarının değerlendirilmesi.
*   🔬 **[Teknik Standartlar ve Tolerans Tabloları](6-olcme-ve-kalite-kontrol/Teknik_Standartlar_ve_Tolerans_Tablolari.md):** Parçacık geçme sıklıkları (örn: H7/g6 mil geçmeleri), teknik resimdeki geometrik konum okumaları ve tolerans sapma limitleri.

### 🛠️ 7. Bakım ve Sürdürülebilirlik
Milyon liralık makineleri verimli şekilde aylarca çalıştırmak, reaktif (arıza sonrası) müdahalelerle değil; proaktif (önleyici/kestirimci) bakımlar ile mümkün olur. Sürtünen her noktaya doğru vizkozitede yağ nüfuz ettirilmesi, ve hareket ile üretimin yarattığı yoğun termal yükün (şartlanmış veya serbest soğutma sistemleriyle) güvenli şekilde sistemden uzaklaştırılması bu alana dahildir.
*   💧 **[Triboloji, Rulmanlar ve Yağlama](7-bakim-ve-onarim/Rulmanlar_Kayislar_ve_Yaglama_Teknolojileri.md):** Rulman ömür hesabı gereksinimleri, aşınma döngülerini sönümleyici yağlama sıvıları ve devirlere bağlı sürtünme kontrolleri.
*   ❄️ **[Endüstriyel Soğutma Sistemleri](7-bakim-ve-onarim/Endustriyel_Sogutma_ve_Isi_Transfer_Sistemleri.md):** Tesisteki makinelerin soğutulması amacıyla kurulan devridaim pompaları, buharlaşmalı kuleler ve kapalı devre boru tipi ısı eşanjörleri.

### 📈 8. Atölye Yönetimi (Yalın Üretim)
İşletme kapasitesi, yalnızca makinenin devir/dakika sayısıyla değil; gereksiz hareketlerin tasfiyesi, takım arama sürelerinin azaltılması ve depolama israflarının (Muda) elimine edilmesi ile artar. Endüstri mühendisliğinin odaklandığı "Daha az atık, daha kısa çevrim süresi" hedefli yönetim felsefeleri ve organizasyon prensipleri burada incelenmiştir.
*   🎯 **[Yalın Üretim ve 5S Disiplini](8-yonetim-ve-verimlilik/Yalin_Uretim_ve_5S_Atolye_Disiplini.md):** Toyota Üretim Sistemi kökenli iyileştirmeler olan 5S'in düzen kültürü, stok maliyeti, sürekli iyileştirme (Kaizen) adımlarını barındırır.

### 🦺 9. İş Sağlığı ve Güvenliği
Ağır tonajlar, ezici presler, tehlikeli kimyasallar ve yüksek volta sahip endüstriyel tesisler ölümcül risklerle doludur. İnsan doğasının hata payı göz önünde bulundurularak, kaza veya risk unsurlarının sistemsel olarak nasıl engelleneceği; müdahale edilemez kurallarla dökümante edilmiştir. Bu kategori projenin en hayati ve en katı kural dizisidir.
*   🔒 **[İSG Risk Yönetimi ve Kaza Önleme](9-is-guvenligi-ve-risk/ISG_Risk_Yonetimi_ve_Kaza_Onleme.md):** Bakım esnasındaki kontrol panolarının fiili LOTO ile izole edilmesi, koruyucu muhafaza bypass'larının reddedilmesi ve Heinrich kaza modellemesi risk yönetimi.

---

## 🤝 İletişim ve Topluluğa Katılım Standartları

Bu kütüphane, bilginin bir araya getirildikçe değerleneceğine inanan ortak açık kaynak yapısına (Open-Source) dayanmaktadır. Makine mühendislerinin, otomasyon yazılımcılarının, meslek lisesi öğretmenlerinin ve sahada birebir tecrübe edinmiş atölye ustalarının bilgi eklemesine ve düzeltmesine (Pull Request) açıktır.

Ancak yapının bilgi kirliliğine, kanıtsız iddialara ve tehlikeli üretim uygulaması övgülerine maruz kalmasını engellemek adına katılımcıların dikkate alması gereken kati kurallar getirilmiştir. Değişiklik teklif etmeden önce veya repo altyapısıyla ilgili yeni bir tartışma (Issue) yayımlamadan önce aşağıdaki yasal çerçeve ve katılım dosyalarını incelemeniz zaruridir:

*   Değişiklik Ekleme ve Doküman İcrası için: **[Katkıda Bulunma Rehberi (CONTRIBUTING.md)](CONTRIBUTING.md)**
*   Topluluk İletişim Standardı ve Saygı Şartları için: **[Davranış Kuralları Beyannamesi (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md)**

Tüm bilgi, insanlık ortak mirasına katkı ve sektörel erişimi tamamen şeffaflaştırmak hedefine, standart kalibrasyon verileri çerçevesinde hizmet etmelidir. Katkılarınız için şimdiden teşekkür ederiz.