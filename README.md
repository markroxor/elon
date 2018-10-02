# LogIt!
Log your daily routines stay productive.

![](https://github.com/markroxor/logit/raw/master/assets/graph.jpg)

## Installation -
Dependencies -   
`sudo apt-get install gnome-screensaver xdotool`    
`pip3 install pyyaml matplotlib numpy`  
`sudo apt-get install -y nodejs`  # installs npm
   
## Clone in your home directory.
`git clone https://github.com/markroxor/logit.git ~/`           

## Usage instructions -  
`cd ~/logit`        
`cp config_original.yaml config.yaml` # create configuration.

Configure `config.yaml` as per your preference.    
1. The applications (Google Chrome) are grouped under categories (browsing).
2. The 'applications' should be a case-sensitive substring of the title of the application.
   Check title bar for the title. 
3. The priorties are held in the order of appearence. Eg.       
    Wasting Time:     
    \- 'YouTube'      
    Browsing:       
    \- 'Google Chrome'      
    \- 'Firefox'      

here YouTube will take precedence over Google Chrome.


## Pushing as a system service
`bash create_service.sh` # create service _without root_    
`sudo bash deploy_service.sh` # to push logit as a system service and start logging at each boot.        
`python3 get_data.py --time n` # to plot the pie-chart since last `n` days. `--time` is optional.             



# Deploy electron app

`python get_data.py --days 10` # to plot the stacked bar plot since last `10` days (`--days` is optional) in an electron app.             
