# Cara mount detail
fls -r -o 360448 disk.flag.img | grep -Ei "flag|txt|secret|hidden"
icat -o 360448 disk.flag.img 1234
