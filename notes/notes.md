
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
sudo systemctl status prevent_idle
```

```yaml
- name: Set timezone to Asia/Bangkok
  become: true
  shell: timedatectl set-timezone Asia/Bangkok

- name: Set language and locale variables
  become: true
  lineinfile:
    path: ~/.bashrc
    line: "{{ item }}"
  with_items:
    - "export LANGUAGE=en_US.UTF-8"
    - "export LC_ALL=en_US.UTF-8"
    - "export LC_CTYPE=en_US.UTF-8"
    - "export LANG=en_US.UTF-8"

- name: Install psutil Python package
  become: true
  pip:
    name: psutil
    executable: pip3

- name: Create prevent_idle service file
  become: true
  copy:
    content: |
      [Unit]
      Description=Prevent Idle Detection
      After=network.target

      [Service]
      User=ubuntu
      WorkingDirectory=/home/ubuntu
      ExecStart=/usr/bin/env python3 /home/ubuntu/prevent_idle.py
      Restart=always

      [Install]
      WantedBy=multi-user.target
    dest: /etc/systemd/system/prevent_idle.service
  notify: Reload Systemd daemon

- name: Reload Systemd daemon
  become: true
  systemd:
    daemon_reload: yes
  changed_when: false

- name: Start and enable prevent_idle service
  become: true
  systemd:
    name: prevent_idle
    state: started
    enabled: yes

```
