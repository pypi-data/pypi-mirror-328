
import os
import csv
import json
import time


class CSVLogSaver:
    def __init__(self, master):
        self.master = master

    def loging_iteration(self, hour, day, folder_path, batch):
        # self.master.logger.create_min_log("start_loging_iteration", self)
        # print(f"saver1 {time.time()}")

        file_name = hour + "h_" + day + ".csv"
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            self.master.creator.create_file_pii(file_name, folder_path, content="")
            self.create_csv_file(file_path, self.master.logger.scv_fields_config_saver_j)

        self.save_to_csv(batch, file_path, fieldnames=self.master.logger.scv_fields_config_saver_j)
        # print(f"saver2 {time.time()}")
        # self.master.logger.create_min_log("end_loging_iteration", self)

    def create_csv_file(self, file_path, fieldnames):
        """Создает CSV-файл с указанными заголовками."""
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    def save_to_csv(self, data, file_path, fieldnames):
        """Дополняет CSV-файл новыми значениями."""
        if not data:
            print(f"Нет логов для добавления в файл {file_path}.")
            return

        with open(file_path, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(data)
