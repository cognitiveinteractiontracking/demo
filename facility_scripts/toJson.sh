#!/bin/bash
source setup.conf
rsbag cat --style 'json :separator #\Newline' -I${PROTO_LOCATION} --load-idl=${PROTO_LOCATION}/\*.proto ${1} > ${1}.json
