midnight=$(date -d "$today 0" +%s)
log_file_name=$midnight"_activity.log"

while true
do
    current_time=$(date +%s)
    if [[ $(gnome-screensaver-command -q) != *"inactive"* ]]
    then
        echo $current_time "Screen is locked" >> "~/logit/logs/"$log_file_name;
    else
        echo $current_time $(xdotool getwindowfocus getwindowname) >> "~/logit/logs/"$log_file_name;
    fi
    sleep 2
done

$(date -d "$today 0" +%s)

