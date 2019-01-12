#!/bin/sh
# set -e
# Given the number of hacks I have used, this script will go rogue in around 
# 8536125172 seconds or ~270 years.

# echo "logging to "$log_file

t_minus1_time=$(date +%s)
while true
do
    midnight=$(date -v+0d -v0H -v0M -v0S +%s)
    log_file=~/elon/logs/$midnight".log"

    test -f $log_file || touch $log_file
    
    last_log=$(tail -n 1 $log_file || echo "failed")
    
    last_time=$(echo $last_log | cut -d " " -f1)
    last_counter=$(echo $last_log | cut -d " " -f2)
    last_event=${last_log:$((${#last_time}+${#last_counter}+2)):1000}

    # check if the screen is locked or if the screensaver is up
    if [[ $(eval 'python ~/elon/macos/is_locked.py') = "True" ]] || [[ $(pgrep ScreenSaverEngine) ]]
    then
        current_event="Screen is locked"
    else 
        current_event=$(echo `osascript ~/elon/macos/get_window_name.scpt`)
    fi
    
    if [[ $current_event != $last_event ]]
    then
        last_counter=0
    else
        sed -i '' -e '$ d' $log_file
    fi
    
    current_time=$(date +%s)
    echo $current_time $(($last_counter+$current_time-$t_minus1_time)) $current_event >> $log_file;
    t_minus1_time=$current_time
    sleep 5
done
