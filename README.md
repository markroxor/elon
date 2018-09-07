# LogIt!
Log your daily routines stay productive.

![](https://github.com/markroxor/logit/raw/master/assets/piee.png)

## Installation -
Dependencies -   
`sudo apt-get install gnome-screensaver xdotool`    
`pip install pyyaml matplotlib numpy`  

Library -    
`git clone https://github.com/markroxor/logit.git ~/`           

## Usage instructions -  
`cd ~/logit`        

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

here YouTube will take precedence over the browser Google Chrome.





`bash ./logit.sh` - to start logging.        
`python get_data.py` - to plot the pie-chart.             

This project is supposed to be a bare minimum for Andrejs's [ulogme](https://github.com/karpathy/ulogme).
