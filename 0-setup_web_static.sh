#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Airbnb clone v2" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart