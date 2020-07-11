#!/bin/bash
./setup.conf
# rsb-loggercl0.12 --style monitor --scope 'spread:/'

rsb-toolscl0.12 logger --on-error=continue --log-level=off -I/opt/twb/twb1.0.x/types --load-idl=/opt/twb/twb1.0.x/types/\*.proto --style monitor 'spread:/tracking/'	
