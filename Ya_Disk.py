import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self,  path_to_file: str):
        self. path_to_file =  path_to_file
        file_name = os.path.basename(self. path_to_file)
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": "/" + file_name, "overwrite": "true"},
            headers={"Authorization": "OAuth " + self.token}
        )

        response.raise_for_status()
        j_link = response.json()
        href = j_link["href"]
        with open(self. path_to_file, "rb") as f:
            response_2 = requests.put(href, files={"file": f})

        response_2.raise_for_status()

        if response_2.status_code == 201:
            print(f'Загрузка файла произведена успешно, код ответа HTTP: [{response_2.status_code}], статус: [{response_2.reason}]')


if __name__ == '__main__':
    path_to_file = r"C:\Users\Asus\Desktop\recipes.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload( path_to_file)