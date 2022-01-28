#!/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install dnsutils -y
cd ~/IPdisplayscreen/src #NO MÅ IPdisplayscreen ligge i heime katalogen
chmod +x ./modules.sh
sh modules.sh
chmod +x ./startipdisplay.sh
sudo raspi-config nonint do_i2c 0
cd IPdisplayscreen/src
sudo python3 setup.py #Må køyrast som sudo for å ha rettigheitane til å endre /etc/rc.local fila
sudo chmod +x ./setrclocal.sh #Fungera ikkje for ein eller annan rar grunn
sudo sh setrclocal.sh
