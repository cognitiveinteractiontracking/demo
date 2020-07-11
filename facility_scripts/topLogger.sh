#!/bin/bash
echo "Logging tool top -b -n1 | head -6. Starttime: $(date +"%y-%m-%d-%H-%M")" > topLogger.txt
while true; do
topLog="$(top -b -n1 | head -6)"
echo "${topLog}" >> topLogger.txt
sleep 5m
done