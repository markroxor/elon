#!/bin/bash
mkdir -p ../logs

sed -i '' -e "s/user_name/$(whoami)/" elon.plist
pip install pyobjc-framework-Quartz --user
pip install pyyaml

cp elon.plist /Users/$(whoami)/Library/LaunchAgents/elon.plist
launchctl load /Users/$(whoami)/Library/LaunchAgents/elon.plist
