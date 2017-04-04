#!/bin/bash
# launchd test script

~/anaconda/bin/python /Users/apple/PycharmProjects/WebProject_TanyaOrlov/launchd/PluginScrapToJSON.py

schtasks /Create /SC DAILY /TN "ScheduleTest" /TR "\Users\apple\PycharmProjects\WebProject_TanyaOrlov\SchTasks\scheduleTest.bat" /ST 15:00
Add Comment

chmod +x scheduleTest.sh

launchctl load /Library/LaunchAgents/WebProject_TanyaOrlov.scheduleTest.csc3130.plist

launchctl unload /Library/LaunchAgents/acreeg.scheduleTest.csc3130.plist

launchctl list 'acreeg.scheduleTest.csc3130'
