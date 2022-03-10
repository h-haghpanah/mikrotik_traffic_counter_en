#!/bin/sh
python3 -m venv /etc/mikrotik_traffic_counter_en/mikrotik_venv
source ../mikrotik_venv/bin/activate
pip3 install -r ../requirement.txt
cp /etc/mikrotik_traffic_counter_en/services/* /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start mikrotik_analysis.service
sudo systemctl enable mikrotik_analysis.service
sudo systemctl start mikrotik_web.service
sudo systemctl enable mikrotik_web.service