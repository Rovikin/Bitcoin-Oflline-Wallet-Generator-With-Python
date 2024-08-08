# BITCOIN ADDRESS GENERATOR

### Alat pembuat alamat dompet Bitcoin ini berjalan secara offline di bahasa pemprograman python.

## Instalasi:

### Download app termux di android. Buka terminal lalu ketik perintah berikut ini:

```
pkg upgrade
```

```
pkg update
```

```
pkg install python
```

```
cd /sdcard/Download
```

## Menjalankan python di termux

```
python btc.py
```

## Catatan:

##### Address dan private key yang dihasilkan dapat diimport di wallet safepal, electrum, bitget, dan juga wallet lain yang mendukung alamat legacy bitcoin. Saya memilih legacy karena paling kompatibel dengan banyak aplikasi wallet di android.

##### Saat membuat wallet bitcoin ini, pastikan perangkat dalam keadaan offline, matikan semua koneksi internet, dan gunakan mode pesawat. Sampai anda selesai menyimpan hasil enkripsi dari private key.

##### Simpan private key yang sudah terenkripsi, password untuk mendecryptnya, dan juga address legacy yang dihasilkan.

##### Jangan mendecrypt 'encrypted private key' kecuali anda ingin menguras semua isinya untuk tidak anda gunakan lagi. Hati2 dengan banyaknya kejahatan cyber.

##### Buatlah keamanan tambahan dengan menyimpan 'encrypted private key' dalam bentuk file .txt kemudian enkripsi lagi ke ekstensi .zip dengan menambahkan password di aplikasi xplore manager. Backup ke manapun yang anda mau, misalnya google drive, 4shared, mediafire, telegram, dll. Jangan khawatir akan bocor karena file zip anda sudah dilapisi keamanan 2 lapis. Yaitu encrypt di private key, dan juga encrypt di file zip.  