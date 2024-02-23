from dotenv import load_dotenv
import os
import telebot  # tg api library
from gensim.summarization import summarize

load_dotenv()  # .env

bot_token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)  # bot initialization

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Lets start, send me link to youtube video and i will retell you content of that video!")

#WORK IN PROGRESS


bot.polling()  # listening messages
