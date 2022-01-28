#Ikkje tenk paa denne
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..
cd ..
rm -rf IPdisplayscreen.zip
zip -r IPdisplayscreen.zip IPdisplayscreen
scp IPdisplayscreen.zip pi@192.168.1.144:/home/pi/
rm -rf IPdisplayscreen.zip