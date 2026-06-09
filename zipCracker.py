#!/usr/bin/env python3
import zipfile
import sys

ZIP_FILE = "file.zip"
WORDLIST = "wordlist.txt"

def try_passwords(zip_path, wordlist_path):
    with zipfile.ZipFile(zip_path) as zf:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                password = line.strip()

                if not password:
                    continue

                try:
                    # Coba extract dengan password ini
                    zf.extractall(pwd=password.encode())
                    print(f"[+] Password found: {password}")
                    return

                except RuntimeError:
                    # Password salah
                    pass

                except Exception:
                    pass

                if i % 1000 == 0:
                    print(f"[*] Tried {i} passwords...")

    print("[-] Password not found in wordlist.")

if __name__ == "__main__":
    zip_path = sys.argv[1] if len(sys.argv) > 1 else ZIP_FILE
    wordlist_path = sys.argv[2] if len(sys.argv) > 2 else WORDLIST

    try_passwords(zip_path, wordlist_path)
