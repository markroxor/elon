chmod u+x ~/logit/logit.sh
sudo systemctl start myfirst
sudo systemctl enable myfirst
cp logit.service /etc/systemd/system/