# BITCOIN ADDRESS GENERATOR

[![Video Tutorial](https://img.youtube.com/vi/a8gCo0Ajcvo/maxresdefault.jpg)](https://youtu.be/a8gCo0Ajcvo?si=q3zYEp-OkPLvXXXM)

#### This Bitcoin address generator tool operates offline using the Python programming language.

## Installation:

#### Download the Termux app on Android. Open the terminal and type the following commands:

```
pkg upgrade
pkg update
pkg install python
pip install ecdsa pycryptodome
pip install base58
cd /sdcard
pkg install git
git clone https://github.com/Rovikin/Bitcoin-Oflline-Wallet-Generator-With-Python.git
cd /sdcard/Bitcoin-Oflline-Wallet-Generator-With-Python
```
### Running Python in Termux

#### To run the Python script and private key decryptor, use the following command:

```
python btc.py
```

#### To run the file encryptor or decryptor script, use the following command:

```
python file_encryptor.py
```

## Notes:

##### The address and private key generated can be imported into SafePal, Electrum, Bitget, and other wallets that support Bitcoin legacy addresses. I chose legacy because it is the most compatible with many wallet applications on Android.

##### When creating this Bitcoin wallet, ensure that the device is offline, turn off all internet connections, and use airplane mode until you have finished saving the encrypted private key.

##### Save the encrypted private key, the password for decrypting it, and the generated legacy address.

##### Do not decrypt the 'encrypted private key' unless you intend to use up all its contents. Be cautious of cyber threats.



# BITCOIN ADDRESS GENERATOR

### Alat pembuat alamat dompet Bitcoin ini berjalan secara offline di bahasa pemprograman python.

## Instalasi:

### Download app termux di android. Buka terminal lalu ketik perintah berikut ini:

```
pkg upgrade
pkg update
pkg install python
pip install ecdsa pycryptodome
pip install base58
cd /sdcard
pkg install git
git clone https://github.com/Rovikin/Bitcoin-Oflline-Wallet-Generator-With-Python.git
cd /sdcard/Bitcoin-Oflline-Wallet-Generator-With-Python
```

## Menjalankan python di termux

```
python btc.py
```
#### Menjalankan enkripsi atau dekripsi file:

```
python file_encryptor.py
```

## Catatan:

##### Address dan private key yang dihasilkan dapat diimport di wallet safepal, electrum, bitget, dan juga wallet lain yang mendukung alamat legacy bitcoin. Saya memilih legacy karena paling kompatibel dengan banyak aplikasi wallet di android.

##### Saat membuat wallet bitcoin ini, pastikan perangkat dalam keadaan offline, matikan semua koneksi internet, dan gunakan mode pesawat. Sampai anda selesai menyimpan hasil enkripsi dari private key.

##### Simpan private key yang sudah terenkripsi, password untuk mendecryptnya, dan juga address legacy yang dihasilkan.

##### Jangan mendecrypt 'encrypted private key' kecuali anda ingin menguras semua isinya untuk tidak anda gunakan lagi. Hati2 dengan banyaknya kejahatan cyber.

Support This Project
If you'd like to support the development of this project, you can make a donation with bitcoin. Here is the QR Code for donations:
img.png

Thank you for your support!
