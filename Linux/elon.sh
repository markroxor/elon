#!/usr/bin/env bash
# Given the number of hacks I have used, this script will go rogue in around 
# 8536125172 seconds or ~270 years.

# echo "logging to "$log_file

while true
do
    midnight=$(date -d "$today 0" +%s)
    log_file=~/elon/logs/$midnight".log"

    test -f $log_file || touch $log_file
    
    current_time=$(date +%s)
    last_log=$(tail -n 1 $log_file || echo "failed")
    
    last_time=$(echo $last_log | cut -d " " -f1)
    last_counter=$(echo $last_log | cut -d " " -f2)
    last_event=${last_log:$((${#last_time}+${#last_counter}+2)):1000}

    if [[ $(gnome-screensaver-command -q) != *"inactive"* ]]
    then
        current_event="Screen is locked"
    else
        current_event=$(xdotool getwindowfocus getwindowname)
    fi
    if [[ $current_event != $last_event ]]
    then
        last_counter=0
    else
        sed -i '$d' $log_file
    fi

    echo $current_time $(($last_counter+1)) $current_event >> $log_file;
    sleep 5
done
