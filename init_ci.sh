#!/bin/bash -

CERT_DIR=./certs
DOMAIN=eid.local
IP4_PREFIX=$(hostname -I | cut -d' ' -f 1 | cut -d. -f 1,2)

function createCert {
    NAME_PREFIX=$1
    openssl req -newkey rsa:2048 -nodes -keyout $NAME_PREFIX.key -x509 -days 365 -out $NAME_PREFIX.cer -subj "/C=DE/ST=Berlin/L=Berlin/O=eid-fu-swp/OU=eid-fu-swp/CN=$DOMAIN"
}

function addToEnv {
    echo "$1" >> .env
}

function addToCompose {
    echo "    extra_hosts:" >> docker-compose.test.yml
    echo "    - \"$DOMAIN:$1\"" >> docker-compose.test.yml
}

echo :Remove existing setup files
rm .env {www,MAIN}.{cer,key} > /dev/null

echo :Shutdown the system if running and cleanup
sudo docker-compose down
sudo docker volume rm eidfuswp_db_mysql


echo :Create .env file
addToEnv "BOILERPLATE_DOMAIN=$DOMAIN"
addToEnv "BOILERPLATE_IPV4_16PREFIX=$IP4_PREFIX"
addToEnv "BOILERPLATE_IPV6_SUBNET=bade:affe:dead:beef:b011::/80"
addToEnv "BOILERPLATE_IPV6_ADDRESS=bade:affe:dead:beef:b011:0642:ac10:0080"
addToEnv "BOILERPLATE_WWW_CERTS=$CERT_DIR"
addToEnv "BOILERPLATE_API_SECRETKEY=$(date | md5sum | cut -d' ' -f 1)"
sleep 1
addToEnv "BOILERPLATE_DB_PASSWORD=$(date | md5sum | cut -d' ' -f 1)"

echo "#################### .env ####################"
cat .env
echo "##############################################"


echo "Make sure the line '$IP4_PREFIX.0.128<tab>$DOMAIN' is in you /etc/hosts"
echo -e "\n$IP4_PREFIX.0.128\t$DOMAIN" | sudo tee --append /etc/hosts
echo Check hosts file
echo "################# /etc/hosts #################"
sudo cat /etc/hosts
echo "##############################################"

echo :Add IP to docker-compose.test.yml
addToCompose "$IP4_PREFIX.0.128"
sudo cat docker-compose.test.yml

echo :Create ssl certifactes
createCert MAIN
createCert www

sudo mv {MAIN,www}.{cer,key} "$CERT_DIR/"
sudo chown root:root $CERT_DIR/{MAIN,www}.{cer,key}