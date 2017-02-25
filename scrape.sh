#!/bin/bash

die() {
	echo $@
	exit 1
}

if [ "a$1" == "a" ]; then
	die "Email needs to be supplied!"
fi

TO=$1
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd`
popd > /dev/null

# create emails with mail extension
for script in $SCRIPTPATH/*.py; do
	python3 $script 2> $SCRIPTPATH/error.log
done

if [ "$(wc -c $SCRIPTPATH/error.log | awk '{print $1}')" == "0" ]; then
	rm $SCRIPTPATH/error.log
else 
	echo >> $SCRIPTPATH/error.log
	echo "Generated on: $(date)" >> $SCRIPTPATH/error.log
fi

if [ -f $SCRIPTPATH/error.log ]; then
	cat <<-EOF > $SCRIPTPATH/emails/error.mail
	Subject: scraping errors
	
	EOF
	cat $SCRIPTPATH/error.log >> $SCRIPTPATH/emails/error.mail
	rm -f $SCRIPTPATH/error.log
fi

# send e-mails
for email in $SCRIPTPATH/emails/*.mail; do
	sendmail $TO < $email
	rm $email
done
