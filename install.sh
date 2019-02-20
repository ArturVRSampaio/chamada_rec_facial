cd ~
#update && upgrade
sudo apt-get update;
sudo apt-get upgrade;
#instalacao

#Instalacao necessaria:
#(seguindo a ordem hierárquica)
#python3
#dlib
#Face_recognition

#python3
sudo apt install python3-pip

#--------
cd ~
#dlib
git clone https://github.com/davisking/dlib.git

cd dlib
mkdir build; cd build; cmake ..; cmake --build .

cd ..
python3 setup.py install

#------
cd~
#face_recognition install
sudo apt-get update

sudo pip3 install face_recognition

#-----
cd ~
