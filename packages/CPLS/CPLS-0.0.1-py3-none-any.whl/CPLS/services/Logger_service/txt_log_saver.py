import json
import os
import time

class TxtLogSaver:
    def __init__(self, master):
        self.master = master

    def loging_iteration(self, hour, day, folder_path, batch):
        file_name = hour + "h_" + day + ".txt"
        self.master.creator.create_file_pii(file_name, folder_path, content="")
        file_path = os.path.join(folder_path, file_name)
        self.append_dicts_to_txt(file_path, batch)
        # print("saver", time.time())


    def append_dicts_to_txt(self, file_path, dict_list):
        """
        Открывает текстовый файл и дописывает в него массив словарей,
        записывая каждый dict в виде одной строки JSON.

        :param file_path: Путь к текстовому файлу.
        :param dict_list: Список словарей, которые нужно добавить.
        """
        try:
            with open(file_path, "a", encoding="utf-8") as file:
                for data in dict_list:
                    json_string = json.dumps(data, ensure_ascii=False)  # Преобразуем dict в JSON-строку
                    file.write(json_string + "\n")  # Записываем в файл, каждый dict на новой строке
        except Exception as e:
            print(f"Ошибка загрузки логов {e}")