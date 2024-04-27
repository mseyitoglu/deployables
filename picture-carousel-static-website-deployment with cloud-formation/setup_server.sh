#!/bin/bash -x

# update the system and install apache

yum update -y
yum install httpd -y

#change to the current directory and download web content

cd /var/www/html
FOLDER="https://raw.githubusercontent.com/mseyitoglu/deployables/main/picture-carousel-static-website-deployment%20with%20cloud-formation/static-web/"
wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg

systemctl start httpd
systemctl enable httpd

