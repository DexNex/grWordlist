#!/bin/bash

# Memperbarui dan meng-upgrade sistem
sudo apt-get update -y
sudo apt-get upgrade -y

# Menginstal lolcat, figlet, dan Python
sudo apt-get install -y lolcat figlet python3 python3-pip

# Menginstal paket Python yang diperlukan
# catat bahwa random dan subprocess adalah modul bawaan Python dan tidak perlu diinstal
# jika ada paket Python lain yang perlu diinstal, tambahkan di bawah ini
# contoh: pip3 install requests

echo "Instalasi selesai."
