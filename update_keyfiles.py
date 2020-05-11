#!/usr/bin/env python3
import pathlib
import os
import requests
import shutil
import sys

"""
Script to download Letsencrypt cert files from another server to pihole.
Usage: # python3 update_keyfiles.py 'http://internal.host/path/to/certs/'
"""

# download pem files and save to current folder
base_url = sys.argv[1]
base_path = pathlib.Path().absolute()

privkey = requests.get(base_url + 'privkey.pem').text
cert = requests.get(base_url + 'cert.pem').text
fullchain = requests.get(base_url + 'fullchain.pem').text

# build combined keyfile
combined = privkey + cert

# save pems to current directory
combined_path = base_path.joinpath('combined.pem')
with open(combined_path, 'w') as combined_file:
    combined_file.write(combined)

fullchain_path = base_path.joinpath('fullchain.pem')
with open(fullchain_path, 'w') as fullchain_file:
    fullchain_file.write(fullchain)

# chown pems
try:
    shutil.chown(combined_path, user='www-data')
    shutil.chown(fullchain_path, user='www-data')
except PermissionError:
    print('This script needs root permissions.')
    sys.exit(-1)

# restart lighttpd server
os.system('service lighttpd restart')