# Extract Metadata
strings image.jpg
file image.jpg

# File disisipkan di dalam file lain

| Tool | Fungsi | Syntax |
|------|--------|--------|
| exiftool|extract metadata| exiftool file_sasa.jpg|
|binwalk|file disisipkan|binwalk -e image.jpg|
|strings|melihat daleman executable|strings file|
|zsteg|ekstrak data PNG/BMP|zsteg file.png|
|steghide|extract data dari img/audio.|steghide info file.bpm OR steghide extract -sf picture1.bmp|
|stegsolve|lihat flag tersembunyi di dalam gambar|GUI|
