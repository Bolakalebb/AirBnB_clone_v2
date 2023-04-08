#!/usr/bbin/env bash
# This bash script will set up web servers for the deployment of web_static
sudo apt-get update
sudo ap-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<!DOCTYPE html>
<html>
  <head>
    <title>Testing Ngnix Configuration</title>
  </head>
  <body>
     Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
