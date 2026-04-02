import os, strutils, terminal

proc validateISGProtocol() =
  echo "================================================="
  echo "🏭 SANAYİ 1001: İSG UYGUNLUK DENETÇİSİ ÇALIŞIYOR"
  echo "================================================="
  
  var 
    totalDocs = 0
    unsafeDocs = 0

  # Tüm klasörleri tara ve sadece markdown dosyalarını yakala
  for file in walkDirRec(".."):
    if file.endsWith(".md") and not file.contains("README") and not file.contains("CONTRIBUTING") and not file.contains("CODE_OF_CONDUCT") and not file.contains("task") and not file.contains("walkthrough") and not file.contains("implementation_plan"):
      totalDocs += 1
      let content = readFile(file)
      let filename = extractFilename(file)
      
      # Dosyada iş güvenliği veya risk uyarısı terimi var mı?
      if not (content.contains("İSG") or content.contains("İş Güvenliği") or content.contains("Risk") or content.contains("Tehlike")):
        setForegroundColor(fgRed)
        echo "[⚠️ İHLAL TESPİT EDİLDİ] -> ", filename, " (İSG Uyarısı Eksik!)"
        resetAttributes()
        unsafeDocs += 1

  echo "-------------------------------------------------"
  echo "🔍 Analiz Edilen Toplam Teknik Doküman: ", totalDocs
  
  if unsafeDocs == 0:
    setForegroundColor(fgGreen)
    echo "[✅ ONAY] Bütün sistem İSG (İş Sağlığı ve Güvenliği) standartlarına uygundur. Üretime geçilebilir."
    resetAttributes()
    quit(0)
  else:
    setForegroundColor(fgRed)
    echo "[❌ FATAL ERROR] ", unsafeDocs, " adet dokümanda güvenlik protokolü eksik! Makine şalteri açılamaz."
    resetAttributes()
    quit(1)

when isMainModule:
  validateISGProtocol()
