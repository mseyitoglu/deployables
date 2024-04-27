#!/bin/bash -x

yum update -y
yum install python3 -y
yum install pip -y
pip install flask
yum update -y

APP="https://raw.githubusercontent.com/mseyitoglu/deployables/main/simple%20web-app%20roman-numerals-converter"
cd /home/ec2-user/
wget ${APP}/app.py
mkdir templates && cd templates
wget ${APP}/templates/index.html
wget ${APP}/templates/result.html
cd ..
python3 app.py



