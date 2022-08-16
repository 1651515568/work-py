tar -zxvf Python-2.7.1.tgz;
mkdir /var/www/html/py27;
cd Python-2.7.1;
./configure --prefix=/var/www/html/py27/;
make;
make install;
./python ../minitor.py