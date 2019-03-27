#!/bin/bash
mkdir -p logs

#create systemd config for Linux
get_service_conf_linux()
{
eval "$1='[Unit]\n
Description=Elon service\n
\n
[Service]\n
Environment=\"DISPLAY=$(echo $DISPLAY)\"\n
Environment=\"DBUS_SESSION_BUS_ADDRESS=$(echo $DBUS_SESSION_BUS_ADDRESS)\"\n
User=$(whoami)\n
ExecStart=/bin/bash /opt/elon.sh\n
\n
[Install]\n
WantedBy=multi-user.target'
"
}

conf=''

get_service_conf_linux conf
echo -e $conf >elon.service

# dependencies
pip install pyyaml oyaml --user
