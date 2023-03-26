I use three bash scripts for this project : 
  1. scrap.sh : It is the script I use to scrap the price data from the yahoo website and to add it to a text file along with the time it was scraped.
  2. clear.sh : It is the script I use to clear the data of the price file every morning before the opening of the market.
  3. stats.sh : It is the script I use to create the daily report, updated every day at 8pm
 
I then have a python file in order to create my dashboard.

The cron.sh file is where I display the crons I used.

The name of my tmux session is : session_projet

Finally here is the link to my dashboard : http://13.39.47.124:8050/
