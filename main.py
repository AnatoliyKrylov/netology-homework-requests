import os
import requests
import time
from datetime import date

# Задача №1
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
heroes_intelligence_dict = {}
json_data = response.json()
for hero in json_data:
    if (hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or
            hero['name'] == 'Thanos'):
        (heroes_intelligence_dict.update(
            {hero['name']: hero['powerstats']['intelligence']}))
most_intelligence = max(heroes_intelligence_dict,
                        key=heroes_intelligence_dict.get)


# Задача 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, files_list: list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": ""
        }
        headers = {
            "Authorization": token
        }
        for file_path in files_list:
            params['path'] = file_path.split(os.sep)[-1]
            response = requests.get(url, headers=headers, params=params)
            if 200 <= response.status_code < 300:
                url_for_upload = response.json().get('href', '')
                with open(file_path, 'rb') as file:
                    response2 = requests.put(url_for_upload,
                                             files={'file': file})
                    if 200 <= response2.status_code < 300:
                        print(f'Файл {params["path"]} успешно загружен')
                    else:
                        print(f'Ошибка при загрузке файла {params["path"]}: '
                              f'{response2.json()["message"]}')
            else:
                print(f'Ошибка при загрузке файла {params["path"]}: '
                      f'{response.json()["message"]}')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    files_list = ['*Путь до файла 1*', '*Путь до файла 2*', ...]
    token = 'OAuth *Ваш токен*'
    uploader = YaUploader(token)
    result = uploader.upload(files_list)

# Задача 3
timestamp = time.mktime(date.today().replace(day=date.today().day-2).
                        timetuple())
url = (f'https://api.stackexchange.com/2.3/questions?fromdate='
       f'{int(timestamp)}&order=desc&sort=activity&tagged='
       f'Python&site=stackoverflow')
response = requests.get(url)
json_data = response.json()
for question in json_data['items']:
    print(f'{question["title"]}: {question["link"]}')
