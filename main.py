import requests
import telebot
import os
token = os.environ.get('API_KEY')
bot = telebot.TeleBot(token)




url = "https://pinksale-trending.s3.amazonaws.com/trending.json"
response = requests.get(url)


@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "welcome to this bot. type /list ")


@bot.message_handler(['list'])
def list_tokens(message):
    prio = sto(response)
    token_list = ""
    for x, prios in enumerate(prio):
        token_list += f"{x+1}: {prios}\n"
    bot.reply_to(message, f"{token_list}\n Devoloped by https://t.me/dev_andrei")


def sto(response):
    store = []

    if response.status_code == 200:
        data = response.json()
        for x in range(len(data["data"])):
            store.append(data["data"][x]["token"])
        return store
      

    else:
        return f"Failed to fetch data from {url}. Status code: {response.status_code}"


bot.polling()
