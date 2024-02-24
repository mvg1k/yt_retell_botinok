import requests
import re
from dotenv import load_dotenv
import os

load_dotenv() #get .env variables


def extract_video_id(youtube_url):
    # searching for id in URL
    youtube_regex = (
    r'(https?://)?(www\.)?'
    r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
    r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
)


    youtube_match = re.match(youtube_regex, youtube_url)

    if youtube_match:
        return youtube_match.group(6)

    return None


id = extract_video_id('link on yt video')


def get_video_detail(videoID):
    # access the API
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    headers = {
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('RAPIDAPI_KEY')
    }
    # send a get request to the API 
    querystring = {"videoId": videoID}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # conver the response to json format
    json_response = response.json()
    # obtain the subtitle url (in XML format)
    subtitleURL = json_response['subtitles']['items'][0]['url']

    return subtitleURL

detail = get_video_detail(id)



def get_subtitle_text(subtitleUrl):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/subtitles"
    headers = {
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('RAPIDAPI_KEY')
    }
    querystring = {"subtitleUrl": subtitleUrl}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

subtitle = get_subtitle_text(detail)
print(subtitle)

