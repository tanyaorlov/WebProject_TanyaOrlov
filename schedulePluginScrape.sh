#!/bin/bash

. /private/etc/rc.common
CheckForNetwork

while [ "${NETWORKUP}" != "-YES-" ]
do
        sleep 10
        NETWORKUP=
        CheckForNetwork
done

/Users/apple/anaconda/bin/python \
/Users/apple/PycharmProjects/WebProject_TanyaOrlov/PluginScraptoJSON.py