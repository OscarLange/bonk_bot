import requests
import json
import time

#reads all chats and returns the data as json
def read_chat(token, offset):
    params = {'offset': offset}
    answer = requests.get(f"https://api.telegram.org/bot{token}/getUpdates", params=params)
    content = answer.content
    data = json.loads(content)
    return data

#incroporates msg information into stats object
def eval_msg(chat_stats, msg):

    #get id of sender
    sender_id = str(msg['from']['id'])

    #check if user was already counted in this run
    if sender_id in chat_stats:
        sender_stats = chat_stats[sender_id]
        sender_stats['msg_count'] = sender_stats['msg_count']+1
    
    #if user wasn't create object
    else:
        username = msg['from']['username']
        chat_stats[sender_id] = {
            'username': username,
            'msg_count': 1
        }

    return chat_stats


#get the stats of the data
def eval_data(data):
    
    #open dictionary to store collected stats in
    file = open('stats.json',)
    stats = json.load(file)

    #loop over all messages
    for msg in data:
        #filter for real messages
        if('message' in msg):

            #check in which chat the message was sent
            chat_id = str(msg['message']['chat']['id'])

            #check if chat is already logged
            if chat_id in stats:
                chat_stats = stats[chat_id]
                chat_stats = eval_msg(chat_stats, msg['message'])
            
            #if not create object
            else:
                chat_stats = eval_msg({}, msg['message'])
                stats[chat_id] = chat_stats

    #print result
    print(stats)

    #write result to file
    #TODO add mongoDB
    stats_json = json.dumps(stats)
    with open("stats.json", "w") as outfile:
        outfile.write(stats_json)
    

#read config values from file
file = open('config.json',)
config = json.load(file)

#retrieve bot token
token = config['token']

#retrieve chat offset
offset = config['offset']

while(True):
    #read chat data
    data = read_chat(token,offset)['result']
    
    if(len(data) > 0):
        #evaluate chat data
        eval_data(data)

        #increase offset 
        offset = data[-1]['update_id'] + 1
    
    time.sleep(30)

