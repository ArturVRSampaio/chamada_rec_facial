
#update && upgrade
sudo apt-get update;
sudo apt-get upgrade;

#instalacao

#Instalacao necessaria:
#(seguindo a ordem hierárquica)
#python3
#Opencv
#Face_recognition
#sklearn


#python3
sudo apt-get install python3;

sudo apt-get install build-essential cmake unzip pkg-config;
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libx11-dev libgtk-3-dev


sudo apt-get install libgtk-3-dev

sudo apt-get install libatlas-base-dev gfortran

sudo apt-get install python3-dev


sudo pip3 install -U scikit-learn

sudo pip3 install --user numpy scipy matplotlib ipython jupyter pandas sympy nose


#download do opencv
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip

sudo pip3 install opencv-contrib-python
#extração
unzip opencv.zip
unzip opencv_contrib.zip

#instalaçãp
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

sudo pip3 install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc


source ~/.bashrc

sudo pip3 install sklearn

sudo pip3 install numpy

cd ~/opencv-3.4.1/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules \
-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
-D BUILD_EXAMPLES=ON ..

make -j4

sudo make install
sudo ldconfig


pkg-config --modversion opencv

#cd ~
#ls /usr/local/lib/python3.6/site-packages/ #cv2.cpython-36m-x86_64-linux-gnu.so

cd ~
cd /usr/local/lib/python3.6/site-packages/
sudo mv cv2.cpython-36m-x86_64-linux-gnu.so cv2.so

cd ~



#face_recognition install


sudo apt-get update
sudo apt-get upgrade

sudo pip3 install face_recognition
