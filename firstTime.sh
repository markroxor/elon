cp ~/logit/logit.sh /opt/
sudo mkdir /var/log/logit
chmod u+x /opt/logit.sh
cp logit.service /etc/systemd/system/
sudo systemctl start logit
sudo systemctl enable logit
