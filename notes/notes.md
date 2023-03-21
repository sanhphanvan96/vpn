
# Things to Ansiblize

```
sudo timedatectl set-timezone Asia/Bangkok
```

```bash
#.bashrc
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8
export LANG=en_US.UTF-8
```

```
pip3 install psutil
```

```
sudo nano /etc/systemd/system/prevent_idle.service
sudo systemctl daemon-reload
sudo systemctl start prevent_idle
sudo systemctl enable prevent_idle
```
