import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        yan_file_name = os.path.basename(file_path)
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": yan_file_name, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        with open(file_path, 'rb') as file:
            data = file.read()
        response = requests.put(href, data)
        response.raise_for_status()
        if response.status_code == 201:
            print(f"Файл {yan_file_name} добавлен на Яндекс.диск")
        return


if __name__ == '__main__':

    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите Token: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
