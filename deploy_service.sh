#!/bin/bash
# install dependencies
apt install gnome-screensaver xdotool npm
npm install

# deploy the as a system service
cp elon.service /etc/systemd/system/elon.service
cp elon.sh /opt/

chmod u+x /opt/elon.sh

systemctl start elon
systemctl enable elon
systemctl daemon-reload

