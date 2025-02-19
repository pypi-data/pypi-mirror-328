from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import threading

class FileChangeHandler(FileSystemEventHandler):
    observer_thread_name = "FileObserverThread"
    def __init__(self, master):
        print("INIT FILE OBSERVER")
        self.master = master

    def init_observer(self):
        self.path_monitored_folder = self.master.paths.root_folder_path
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = self.on_created
        self.event_handler.on_deleted = self.on_deleted
        self.event_handler.on_modified = self.on_modified
        self.event_handler.on_moved = self.on_moved
        self.observer = Observer()
        self.observer.name = f"{self.observer_thread_name}1"

    def on_created(self, event):
        if not set(event.src_path.split(os.sep)) & set(self.observe_ignore_j):
            self.master.paths.update_base_tree()
            self.master.paths.update_main_view_processing()
            self.master.paths.update_second_view_processing()
            # print(f"Создано: {event.src_path}")

    def on_deleted(self, event):
        if not set(event.src_path.split(os.sep)) & set(self.observe_ignore_j):
            self.master.paths.update_base_tree()
            self.master.paths.update_main_view_processing()
            self.master.paths.update_second_view_processing()
            # print(f"Удалено: {event.src_path}")

    def on_modified(self, event):
        if not set(event.src_path.split(os.sep)) & set(self.observe_ignore_j):
            if self.master.paths.is_subpath(self.master.paths.local_config_folder_path, event.src_path) or self.master.paths.is_subpath(self.master.paths.global_config_folder_path, event.src_path):
                self.master.paths.update_main_view_processing()
                self.master.paths.update_second_view_processing()
                self.master.json_h.update_all_repo_configs()
                # print(f"Изменено: {event.src_path}")

    def on_moved(self, event):
        if not set(event.src_path.split(os.sep)) & set(self.observe_ignore_j) or not set(event.dest_path.split(os.sep)) & set(self.observe_ignore_j):
            self.master.paths.update_base_tree()
            self.master.paths.update_main_view_processing()
            self.master.paths.update_second_view_processing()
            self.master.json_h.update_all_repo_configs()
            # print(f"Перемещено: {event.src_path} -> {event.dest_path}")

    def run(self):
        print(f"Начало отслеживания папки: {self.path_monitored_folder}")
        self.observer.schedule(self.event_handler, self.path_monitored_folder, recursive=True)
        self.observer.start()
        for thread in threading.enumerate():
            if thread.name.startswith("Thread"):
                # print(f"Поток: {thread.name}, ID: {thread.ident}, Запущен: {thread.is_alive()}")
                thread.name = f"{self.observer_thread_name}2"

    def on_program_exit(self):
        print(f"Остановка отслеживания папки: {self.path_monitored_folder}")
        self.observer.stop()
        self.observer.join()
