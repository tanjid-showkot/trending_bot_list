import requests
import telebot
import os
import time
token = os.environ.get('API_KEY')
bot = telebot.TeleBot(token)




url = "https://pinksale-trending.s3.amazonaws.com/trending.json"



@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "welcome to this bot. type /list ")


@bot.message_handler(['list'])
def list_tokens(message):
    prio = sto(url)
    token_list = ""
    for x, prios in enumerate(prio):
        token_list += f"{x+1}: {prios}\n"
    bot.reply_to(message, f"{token_list}\n Devoloped by @dev_andrei")


def sto(url):
    
   
    while True:
        store = []
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for x in range(len(data["data"])):
                store.append(data["data"][x]["token"])
            return store
        time.sleep(10)
      

  


bot.polling()
