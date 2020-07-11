# !/bin/bash
if [ ${1} -eq 0 ]
then
	cmd="0000&z=1475844094972"
elif [ ${1} -eq 1 ]
then
	cmd="FF00&z=1475844078196"
else
	echo "Wrong parameter. Please choose between 0 and 1 to toggle the light!"
	exit
fi
curl 'http://twbaccess.techfak.uni-bielefeld.de:12347/?z=1475844053603&u=2&p=user' -H 'Host: twbaccess.techfak.uni-bielefeld.de:12347' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0' -H 'Accept: text/javascript, text/html, application/xml, text/xml, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: http://twbaccess.techfak.uni-bielefeld.de:12347/'
curl 'http://twbaccess.techfak.uni-bielefeld.de:12347/?x=F6C35101DA000100010A'${cmd} -H 'Host: twbaccess.techfak.uni-bielefeld.de:12347' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0' -H 'Accept: text/javascript, text/html, application/xml, text/xml, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: http://twbaccess.techfak.uni-bielefeld.de:12347/'