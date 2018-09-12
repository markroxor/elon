#!/bin/bash

# deploy the as a system service
cp logit.service /etc/systemd/system/logit.service
cp logit.sh /opt/

chmod u+x /opt/logit.sh

systemctl start logit
systemctl enable logit
systemctl daemon-reload
