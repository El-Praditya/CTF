# Windows Forensic
FTK Imager

# Filter Wireshark
1. tcp.stream eq 5
2. tcp contains "pico"
3. http OR http.request (hanya tampilkan http request)
4. http.request.method == "POST" (cari request dengan method POST)
5. http && http.request.method == "POST" (contoh cara pake 2 command sekaligus)

# Tshark
tshark -r file.pcap -T fields -e tcp.payload (tcp.seq - ip.src - dns.qry.name - http.host - http.user_agent)

# Decompile
Ghidra

# objdump. For dissamble 
objdump -d vuln | grep "<"

# gdb. For run line by line
gdb namafile

# nm. For cari fungsi kyk main() win() flag()
nm vuln | grep " T "

# xxd. Melihat HEX
xxd file.png
