# bonk_bot

This bot is made for community managment such as collecting user information.  
It is written in python and uses the telegram api.  

## files

1. statbot.py => collects user information
2. bot.py => older bot version that waits for commands
3. stats.json => current place to store stats, as database is not implemented yet

## setup

You need to create a config.json file like this:  
  
{  
    "token": "your_bot_token" ,  
    "offset": 130737589  
}  

And a stats.json file with an empty json:  
{  
     
}  
  
You can get a bot token from here https://core.telegram.org/bots
