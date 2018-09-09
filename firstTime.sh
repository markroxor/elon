#create systemd config
get_service_conf()
{
eval "$1='[Unit]\n
Description=Logit service\n
\n
[Service]\n
Environment=\"DISPLAY=:0\"\n
Environment=\"DBUS_SESSION_BUS_ADDRESS=$(echo $DBUS_SESSION_BUS_ADDRESS)\"\n
User=$(whoami)\n
ExecStart=/bin/bash /opt/logit.sh\n
\n
[Install]\n
WantedBy=multi-user.target'\n
"
}

conf=''
get_service_conf conf
sudo echo $conf >/etc/systemd/system/


cp ~/logit/logit.sh /opt/

sudo mkdir /var/log/logit
chmod u+x /opt/logit.sh

sudo systemctl start logit
sudo systemctl enable logit
