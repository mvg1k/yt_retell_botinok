import re
import requests
from xml.etree import ElementTree

# Ваш API ключ від YouTube Data API
api_key = 'key'

def extract_video_id(youtube_url):
    # Використовуємо регулярний вираз для пошуку ID відео в URL
    youtube_regex = (
    r'(https?://)?(www\.)?'
    r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
    r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
)


    youtube_match = re.match(youtube_regex, youtube_url)

    if youtube_match:
        return youtube_match.group(6)

    return None

# Функція для отримання субтитрів відео
def print_youtube_video_captions(video_id, api_key):
    # Отримуємо доступні доріжки субтитрів
    captions_url = f'https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId={video_id}&key={api_key}'
    captions_response = requests.get(captions_url)
    captions_data = captions_response.json()
    
    for item in captions_data.get('items', []):
        # Тут ви можете перевірити item['snippet']['language'] для вибору потрібної мови
        if item['snippet']['language'] == 'en':  # Припустимо, що вам потрібні англійські субтитри
            track_id = item['id']
            
            # Отримуємо субтитри
            captions_download_url = f'https://www.googleapis.com/youtube/v3/captions/{track_id}?key={api_key}&alt=media'
            captions_download_response = requests.get(captions_download_url)
            
            # Розбираємо XML та друкуємо субтитри
            if captions_download_response.status_code == 200:
                try:
                    root = ElementTree.fromstring(captions_download_response.content)
                    for elem in root.iter('{http://www.w3.org/2006/10/ttaf1}p'):
                        print(elem.text)
                except ElementTree.ParseError as e:
                    print("Помилка при розборі XML:", e)
            else:
                print("Не вдалося завантажити субтитри: HTTP Status Code", captions_download_response.status_code)
            break
    else:
        print("Субтитри на вказаній мові не знайдено.")

# Тестуємо на прикладі URL
video_url = "https://www.youtube.com/watch?v=Q293fDfWZnc"
video_id = extract_video_id(video_url)

# Викликаємо функцію для друкування субтитрів
print_youtube_video_captions(video_id, api_key)


