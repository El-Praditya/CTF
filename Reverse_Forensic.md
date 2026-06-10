# Windows Forensic
FTK Imager

# Filter Wireshark
1. tcp.stream eq 5
2. tcp contains "pico"

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
