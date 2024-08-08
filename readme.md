# BITCOIN ADDRESS GENERATOR

#### This Bitcoin address generator tool operates offline using the Python programming language.

## Installation:

#### Download the Termux app on Android. Open the terminal and type the following commands:

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

### Running Python in Termux

####To run the Python script, use the following command:

```
python btc.py
```

## Notes:

##### The address and private key generated can be imported into SafePal, Electrum, Bitget, and other wallets that support Bitcoin legacy addresses. I chose legacy because it is the most compatible with many wallet applications on Android.

##### When creating this Bitcoin wallet, ensure that the device is offline, turn off all internet connections, and use airplane mode until you have finished saving the encrypted private key.

##### Save the encrypted private key, the password for decrypting it, and the generated legacy address.

##### Do not decrypt the 'encrypted private key' unless you intend to use up all its contents. Be cautious of cyber threats.

##### For additional security, store the 'encrypted private key' in a .txt file and then encrypt it again to a .zip file with a password using the Xplore Manager app. Backup the file to any location you prefer, such as Google Drive, 4shared, Mediafire, Telegram, etc. Don't worry about leaks because your zip file is secured with two layers of protection: encryption on the private key and encryption on the zip file.