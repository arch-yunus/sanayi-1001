import os
import json
import sys

def load_db():
    api_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api", "sanayi_1001_db.json")
    if not os.path.exists(api_path):
        print("[!] Veritabani bulunamadi. Lutfen once 'python tools/sanayi_db_builder.py' calistirin.")
        sys.exit(1)
    
    with open(api_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def print_help():
    print("==============================================")
    print(" 🛠️  SANAYI 1001 - HACKER TERMINALI")
    print("==============================================")
    print("Kullanim:")
    print("  python sanayi.py arama <kelime>    : Butun ansiklopedide kelimeyi arar")
    print("  python sanayi.py isg_ihlal         : ISG uyarisi EKSIK olan belgeleri bulur")
    print("  python sanayi.py stat              : Veritabani istatistiklerini gosterir")
    print("==============================================")

def search_term(term):
    db = load_db()
    print(f"\nArama Sonuclari: '{term}'\n" + "-"*40)
    found = False
    for domain, docs in db["domains"].items():
        for doc in docs:
            if term.lower() in doc["raw_content"].lower() or term.lower() in doc["title"].lower():
                print(f"[{domain}] -> {doc['title']} ({doc['filename']})")
                found = True
    if not found:
        print("Hicbir sonuc bulunamadi.")

def check_isg():
    db = load_db()
    print("\nISG (Is Guvenligi) Eksigi Olan Belgeler:\n" + "-"*40)
    found = False
    for domain, docs in db["domains"].items():
        for doc in docs:
            if not doc.get("has_isg_warning", False):
                print(f"[TEHLIKE] {doc['title']} ({doc['filename']})")
                found = True
    if not found:
        print("[OK] Tum belgelerde ISG uyarisi tam.")

def print_stats():
    db = load_db()
    total_docs = sum(len(docs) for docs in db["domains"].values())
    total_size = sum(doc["content_length"] for docs in db["domains"].values() for doc in docs)
    print("\nVeritabani Istatistikleri:\n" + "-"*40)
    print(f"Toplam Kategori Sayisi : {len(db['domains'])}")
    print(f"Toplam Teknik Dokuman  : {total_docs}")
    print(f"Toplam Karakter Hacmi  : {total_size} karakter")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)
        
    cmd = sys.argv[1].lower()
    
    if cmd == "arama" and len(sys.argv) >= 3:
        search_term(" ".join(sys.argv[2:]))
    elif cmd == "isg_ihlal":
        check_isg()
    elif cmd == "stat":
        print_stats()
    else:
        print_help()

if __name__ == "__main__":
    main()
