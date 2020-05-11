# pihole-letsencrypt

Script to download Letsencrypt cert files from another server to Pi-hole.

## Setup and usage
### Prerequisites
You need a webserver in your LAN which serves the `*.pem` files you want to use on your Pi-hole. Usually, you obtain them from Letsencrypt via `certbot`.

### Setup:
- SSH into your Pi-hole: `ssh root@pihole`
- Install required Python3 libraries: `apt install python3-requests`
- Clone this repository: `git clone https://github.com/abaumg/pihole-letsencrypt`
- Edit crontab: `crontab -e` and add a new line containing `0 3 * * * /usr/bin/python3 /root/pihole-letsencrypt/update_keyfiles.py 'http://internal.host/path/to/certs/'`