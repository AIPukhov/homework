import requests


def token():  # Функция для получения токена из файла в этой же директории
    with open('token.txt', 'r', encoding='utf-8') as file:
        return file.readline()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        file_name = file_path
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {"path": f"/{file_name}", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл загружен'
        else:
            return f'Ошибка: {responce.status_code}'


if __name__ == '__main__':
    token = token()
    path_to_file = 'test.txt'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
