#!
yum update -y
yum install httpd -y
cd /var/www/html
FOLDER="https://raw.githubusercontent.com/mseyitoglu/deployables/main/picture-carousel-static-website-deployment%20with%20cloud-formation/static-web/"
wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg

systemctl start httpd
systemctl enable httpd

