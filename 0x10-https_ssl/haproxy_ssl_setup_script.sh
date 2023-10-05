#!/bin/bash

# Set up Pre-requisites
sudo apt-get update
haproxy -v
sudo snap install --classic certbot
sudo service haproxy stop
sudo certbot certonly --standalone -d www.leonze.tech
sudo mkdir -p /etc/haproxy/certs
DOMAIN='www.leonze.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs

# add necesary configuration to haproxy config file

# check if the config file is ok, if so skip to restart section else fix it:
# sudo haproxy -f /etc/haproxy/haproxy.cfg -c

# Fixes:
# Run this command to correct the DH parameter error:
# sudo openssl dhparam -out /etc/haproxy/dhparams.pem 2048
# Add the line below to your config file, as the last line of the global section:
# ssl-dh-param-file /etc/haproxy/dhparams.pem

# restart haproxy service:
# sudo service haproxy restart
