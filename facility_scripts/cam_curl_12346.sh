# !/bin/bash
help_s="You can use ${0} {0,1,2} to turn all cams off(0), on(1) or restart(2) them.
To handle a single camera you can use ${0} cam# {0,1,2}."
if [ "${1}" == "help" ]
then
	echo "${help_s}"
	exit
fi

if [ "$#" -eq 1 ]
then
	if [ ${1} -eq 0 ]
	then
		cmd=0000
	elif [ ${1} -eq 1 ]
	then
		cmd=1111
	elif [ ${1} -eq 2 ]
	then
		cmd=iiii
	else
		echo "Wrong parameter. ${help_s}"
		exit
	fi
elif [ "$#" -eq 2 ]
then
	cmd=uuuu
	if [ ${2} -eq 2 ]
	then
		cmd=`echo ${cmd} | sed s/./i/${1}`
	elif [ ${2} -eq 1 ] || [ ${2} -eq 0 ]
	then
		cmd=`echo ${cmd} | sed s/./${2}/${1}`
	else
		echo "Wrong parameter. ${help_s}"
	exit
	fi
fi
curl 'http://twbaccess.techfak.uni-bielefeld.de:12346/tgi/control.tgi?login=p:user:TwbC@Mpower&p='${cmd}
echo ""
