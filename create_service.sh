#!/bin/bash

#create systemd config
get_service_conf()
{
eval "$1='[Unit]\n
Description=Logit service\n
\n
[Service]\n
Environment=\"DISPLAY=$(echo $DISPLAY)\"\n
Environment=\"DBUS_SESSION_BUS_ADDRESS=$(echo $DBUS_SESSION_BUS_ADDRESS)\"\n
User=$(whoami)\n
ExecStart=/bin/bash /opt/logit.sh\n
\n
[Install]\n
WantedBy=multi-user.target'
"
}

conf=''
get_service_conf conf
# sudo echo -e $conf >/etc/systemd/system/logit.service
echo -e $conf >logit.service
