#!/bin/bash
mkdir -p ../logs

sed -i '' -e "s/user_name/$(whoami)/" elon.plist
pip install pyobjc-framework-Quartz
pip install pyyaml oyaml

mv elon.plist /Users/$(whoami)/Library/LaunchAgents/elon.plist
launchctl load /Users/$(whoami)/Library/LaunchAgents/elon.plist
