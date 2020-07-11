#!/bin/bash
source setup.conf
rsbag record -I${PROTO_LOCATION} --load-idl=${PROTO_LOCATION}/\*.proto -o ${MY_LOG_FILE} 'spread:/tracking/merger'
