import json
import os
import queue
import threading
import time
from pprint import pprint

from .json_log_saver              import JsonLogSaver
from .csv_log_saver               import CSVLogSaver
from .txt_log_saver               import TxtLogSaver


class BaseLogSaver:
    def __init__(self, master):
        self.master = master
        self.is_main_loop = None
        self.command_queue = queue.Queue()
        self.saver_obj = None

    def init_saver(self):
        if self.master.logger.save_log_module_j == "json_log_saver":
            self.saver_obj             = JsonLogSaver(self.master)
        elif self.master.logger.save_log_module_j == "csv_log_saver":
            self.saver_obj              = CSVLogSaver(self.master)
        elif self.master.logger.save_log_module_j == "txt_log_saver":
            self.saver_obj              = TxtLogSaver(self.master)

    def start(self):
        self.main_loop_thread = threading.Thread(target=self.main_loop, daemon=True, name="Saver")
        self.main_loop_thread.start()

    def add_log(self, *args):
        self.command_queue.put((args))

    def main_loop(self):
        self.is_main_loop = True

        while self.is_main_loop or self.command_queue.qsize() > 0:
            self.main_loop_func()
            if self.is_main_loop:
                time.sleep(self.master.logger.save_logs_delay_j)

    def main_loop_func(self):
        if self.saver_obj:
            try:
                args = self.command_queue.get(timeout=1)
                # print("save_batch_logs")
                self.save_batch_logs(*args)
            except queue.Empty:
                pass

    def stop(self):
        self.is_main_loop = False
        if not self.saver_obj:
            self.command_queue.queue.clear()
        self.main_loop_thread.join()


    def save_batch_logs(self, batch, base_logger_folder):
        for day, hour_info in batch.items():
            folder_path = os.path.join(base_logger_folder, day)
            self.master.creator.create_directory_pii(folder_path)
            for hour, batch in hour_info.items():
                self.saver_obj.loging_iteration(hour, day, folder_path, batch)

