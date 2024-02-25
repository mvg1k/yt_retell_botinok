# YouTube Retell Bot
This repository contains the python code for a Telegram bot designed to enhance the user experience by providing concise video summaries. The bot leverages the YouTube Media Downloader API to fetch subtitles from YouTube videos. It processes the retrieved subtitles to strip away extraneous symbols and formatting, preparing clean text for further analysis.

Utilizing the powerful capabilities of ChatGPT 3.5, the bot sends the cleaned subtitles as a prompt to the language model, requesting a succinct summary of the video content based on the textual information. The response from ChatGPT is then directly relayed to the user who initiated the request through the Telegram bot.

The integration with ChatGPT is made possible by the tool provided in the [gpt4free repo](https://github.com/xtekky/gpt4free), which facilitates API interactions with the language model.

For security and functionality, API tokens and sensitive data are stored in a .env file, ensuring that credentials remain secure and are not exposed within the public codebase.

This bot aims to provide users with a quick understanding of a video's content without watching the entire footage, saving time and providing convenience by summarizing the essence of the video in a textual format.

This bot is still in development, you can use it soon by using @yt_retell_bot nickname in Telegram!
