
import os
from pprint import pprint

class ConfigsManager:
    def __init__(self, master):
        print("INIT CONFIGS MANAGER")
        self.master = master
        self.json_h = self.master.json_h
        self.paths  = self.master.paths

    def load_service_configs(self):
        # Перенос путей из pahts
        self.base_configs_folder_path    = self.paths.base_configs_folder_path
        root_folder_path            = self.paths.root_folder_path
        repository_path             = self.paths.repository_path
        self.start_file_name        = self.paths.start_file_name


        # Инициализация главного конфига
        self.json_h.unload_config(self, os.path.join(self.base_configs_folder_path,  "project_config.json"))
        self.json_h.unload_config(self, os.path.join(root_folder_path,          "project_config.json"))


        # Инициализация имен папок конфигов
        self.global_config_folder_name  = self.config_folder_name_j
        self.local_config_folder_name   = f"{self.paths.repo_folder_name}_{self.config_folder_name_j}"
        # Инициализация путей папок конфигов
        self.global_config_folder_path   = os.path.join(repository_path,     self.global_config_folder_name)
        self.local_config_folder_path    = os.path.join(root_folder_path,    self.local_config_folder_name)


        # Перенос имен папок конфигов в paths
        self.paths.init_path(self.paths, "global_config_folder_name",  self.global_config_folder_name)
        self.paths.init_path(self.paths, "local_config_folder_name",   self.local_config_folder_name)
        # Перенос путей папок конфигов в paths
        self.paths.init_path(self.paths, "global_config_folder_path",   self.global_config_folder_path)
        self.paths.init_path(self.paths, "local_config_folder_path",    self.local_config_folder_path)

        self.apply_important_config(self.paths, "paths_config.json")
        self.apply_config(self.paths, "init_config.json")
        self.apply_config(self, "init_config.json")
        self.apply_important_config(self.master.file_observer, "file_observer_config.json")
        self.apply_important_config(self.master.cgc, "cgc_config.json")
        self.apply_config(self.master.logger, "logger_config.json")

    def apply_important_config(self, obj, path_name):
        self.json_h.unload_config(obj, os.path.join(self.base_configs_folder_path, path_name))
        self.json_h.unload_config(obj, os.path.join(self.global_config_folder_path, path_name))
        self.json_h.unload_config(obj, os.path.join(self.local_config_folder_path, path_name))

    def apply_config(self, obj, path_name):
        self.json_h.unload_config(obj, os.path.join(self.base_configs_folder_path, path_name))
        self.json_h.unload_config(obj, os.path.join(self.global_config_folder_path, self.start_file_name, path_name))
        self.json_h.unload_config(obj, os.path.join(self.local_config_folder_path, self.start_file_name, path_name))

    def create_configs_folders(self):
        if self.folder_local_configs_j:
        # pprint(self.paths.configs_folder_view.configs_folder_struct)
            structure_create = {self.local_config_folder_name: {self.paths.start_file_name : self.paths.configs_folder_view.configs_folder_struct}}
            self.master.creator.creation_by_config_pii(structure_create, self.paths.root_folder_path)
        if self.folder_global_configs_j:
            structure_create = {self.global_config_folder_name: {self.paths.start_file_name : self.paths.configs_folder_view.configs_folder_struct}}
            self.master.creator.creation_by_config_pii(structure_create, self.paths.repository_path)
