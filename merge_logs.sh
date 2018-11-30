#!/bin/bash

set -e

rm -rf logs
mkdir -p logs

for log_folders in $(ls backup)
do
    echo $log_folders
    for log in $(ls backup/$log_folders)
    do
        if [ -f logs/$log ]
        then
            cat backup/$log_folders/$log >> logs/$log
            sort -o logs/$log logs/$log
            # sort -u logs/$log | tee logs/$log
            # head -n 3 logs/$log
            # awk '!x[$0]++' logs/$log | tee logs/$log
        else
            cp backup/$log_folders/$log logs/$log
        fi
    done
done    
