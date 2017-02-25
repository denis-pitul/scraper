#!/bin/bash

die() {
	echo $@
	exit 1
}

sudo true
if [ $? -ne 0 ]; then
	die "Sudo needed! Please fix!"
fi

sudo yum install -y nodejs npm
sudo npm -g install phantomjs-prebuilt
sudo pip install selenium
