import os
import json
import re

def build_database():
    print("==================================================")
    print("SANAYI 1001: Veritabani (JSON API) Derleyici Basladi")
    print("==================================================")

    db = {
        "metadata": {
            "version": "2.0",
            "name": "Sanayi 1001 API",
            "description": "Endüstriyel Teknik Bilgi Bankasi"
        },
        "domains": {}
    }

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Tüm klasörleri tara (1-9 arasındaki numaralarla başlayan klasörler)
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f[0].isdigit()]

    for folder in sorted(folders):
        domain_name = folder.replace("-", " ").title()
        db["domains"][domain_name] = []
        
        folder_path = os.path.join(base_dir, folder)
        md_files = [f for f in os.listdir(folder_path) if f.endswith('.md') and f != "index.md"]
        
        for md_file in md_files:
            file_path = os.path.join(folder_path, md_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Başlığı çıkar (İlk # Header)
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else md_file.replace("_", " ").replace(".md", "")
                
                # Dosyayı paragraflara/alt başlıklara bölebiliriz, ama şimdilik ham textini alalım.
                # İSG uyarılarını yakala
                isg_warnings = re.findall(r'>\s*\[!WARNING\].*?(?=>\s*\[|\n\n|\Z)', content, re.DOTALL | re.IGNORECASE)
                isg_warnings += re.findall(r'>\s*\[!IMPORTANT\].*?İSG.*?(?=>\s*\[|\n\n|\Z)', content, re.DOTALL | re.IGNORECASE)
                
                doc_entry = {
                    "title": title,
                    "filename": md_file,
                    "content_length": len(content),
                    "has_isg_warning": len(isg_warnings) > 0,
                    "raw_content": content
                }
                db["domains"][domain_name].append(doc_entry)
                
    api_dir = os.path.join(base_dir, "api")
    if not os.path.exists(api_dir):
        os.makedirs(api_dir)
        
    output_path = os.path.join(api_dir, "sanayi_1001_db.json")
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
        
    print(f"Bitti! Toplam {len(folders)} ana domain islendi.")
    print(f"Cikti Yolu: {output_path}")
    print("==================================================")

if __name__ == "__main__":
    build_database()
