from pypdf import PdfReader

PDF_FILE = "file.pdf"
WORDLIST = "wordlist.txt"

with open(WORDLIST, "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]

reader = PdfReader(PDF_FILE)

for i, password in enumerate(passwords, 1):
    try:
        result = reader.decrypt(password)

        if result:
            print(f"[+] Password found: {password}")
            break

    except Exception:
        pass

    if i % 1000 == 0:
        print(f"[*] Tried {i} passwords...")

else:
    print("[-] Password not found in wordlist.")
