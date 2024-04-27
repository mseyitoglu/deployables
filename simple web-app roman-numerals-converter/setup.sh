#!/bin/bash -x

yum update -y
yum install python3 -y
yum install pip3 -y
pip3 install flask
pip install flask
yum update -y

APP="https://raw.githubusercontent.com/mseyitoglu/deployables/main/simple%20web-app%20roman-numerals-converter"
cd /home/ec2-user/
wget ${APP}/app.py
mkdir app && cd app
wget ${APP}/templates/index.html
wget ${APP}/templates/result.html

