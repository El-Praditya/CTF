# Windows Forensic
FTK Imager

# Filter Wireshark
1. tcp.stream eq 5
2. tcp contains "pico"

# Tshark
tshark -r file.pcap -T fields -e tcp.payload (tcp.seq - ip.src - dns.qry.name - http.host - http.user_agent)

# Decompile
Ghidra

# objdump
Dissamble
