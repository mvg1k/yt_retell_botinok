from dotenv import load_dotenv # get env variables(api tokens)
import os
import telebot  #tg api library
from get_cc import extract_video_id, get_video_detail, get_subtitle_text
import re
from g4f.client import Client  #chatgpt api calls

# Initialize the GPT client
gpt_client = Client()

# Load environment variables
load_dotenv()

# Get the bot token from the environment variable
bot_token = os.getenv('BOT_TOKEN')

# Initialize the bot
bot = telebot.TeleBot(bot_token)

# Maximum length of the message
MAX_MESSAGE_LENGTH = 4096

# Helper function to send large messages
def send_large_message(chat_id, text):
    for x in range(0, len(text), MAX_MESSAGE_LENGTH):
        bot.send_message(chat_id, text[x:x+MAX_MESSAGE_LENGTH])

# Start and help command handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, send me link to YouTube video and i will retell you what is it about!")

# Message handler for YouTube links
@bot.message_handler(func=lambda message: 'youtube.com' in message.text or 'youtu.be' in message.text)
def handle_message(message):
    bot.send_message(message.chat.id, "Please wait, analyzing the video...")
    
    video_id = extract_video_id(message.text)
    if video_id:
        subtitle_url = get_video_detail(video_id)
        subtitles = get_subtitle_text(subtitle_url)
        
        # Clean the subtitles by removing timestamps and other non-spoken text
        pattern = r'\d+\n\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\n'
        cleaned_text = re.sub(pattern, '', subtitles)
        cleaned_text = cleaned_text.strip().replace('\n', ' ')

        # Send the cleaned text to the summarization API
        response = gpt_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": " Your prompt to CHATGPT model " + cleaned_text }]
        )
        
        # Retrieve the summary from the response
        summary = response.choices[0].message.content
        
        # Send the summary back to the user
        send_large_message(message.chat.id, summary + " \n @yt_retell_bot")

    else:
        bot.send_message(message.chat.id, "Sorry, I cant find video ID in this URL.")


# Invalid message handler
@bot.message_handler(func=lambda message: True)
def handle_invalid_message(message):
    bot.send_message(message.chat.id, "Please, send me correct Youtube video link.")

# Start the bot's infinite polling
bot.infinity_polling()
