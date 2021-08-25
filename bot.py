import telegram
import logging
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler


#bonk someone
def bonk(update, context):
    name = 'bong' + str(random.randint(1,6)) + '.jpeg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(name, 'rb'))

#bonk someone
def threaten(update, context):
    name = 'threaten' + str(random.randint(1,6)) + '.jpeg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(name, 'rb'))

with open("token.txt") as file:

    #set up logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    
    #read bot token
    token = file.read()
    
    #create telegram-bot
    bot = telegram.Bot(token=token)

    #create updater
    updater = Updater(token=token, use_context=True)

    #create dispatcher
    dispatcher = updater.dispatcher

    #define handlers
    bonk_handler = CommandHandler('bonk', bonk)
    threaten_handler = CommandHandler('threaten', threaten)

    #start handlers
    dispatcher.add_handler(bonk_handler)
    dispatcher.add_handler(threaten_handler)

    #start bot
    updater.start_polling()

