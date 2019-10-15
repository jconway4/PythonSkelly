#!/bin/bash

# Run as root
if [ "$(whoami)" != "root" ]; then
	echo "error: Run this install script as root"
	exit 1
fi

echo "info: installing requirements for this project"
apt update

# Install Python 3.6
apt -y install python3
apt -f -y install
apt -y install python3-pip

# Install Requirements
pip3 install -r installation/requirements
