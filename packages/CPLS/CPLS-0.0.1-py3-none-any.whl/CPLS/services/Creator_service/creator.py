

import os


class Creator:
    def __init__(self, master):
        print("INIT CREATOR")
        self.master = master

    def creation_by_config(self, config, root_folder):
        self.create_structure(config, root_folder, self.create_directory, self.create_file)

    def creation_by_config_pii(self, config, root_folder):
        self.create_structure(config, root_folder, self.create_directory_pii, self.create_file_pii)

    def creation_by_config_piic(self, config, root_folder):
        self.create_structure(config, root_folder, self.create_directory_piic, self.create_file_piic)

    def create_structure(self, structure, current_path, create_dir_func, create_file_func):
        for key, value in structure.items():
            file_type = value.get("file_type", None)
            if not file_type:
                new_path = os.path.join(current_path, key)
                create_dir_func(new_path)
                if isinstance(value, dict):
                    self.create_structure(value, new_path, create_dir_func, create_file_func)
            else:
                file_name = f"{key}.{file_type}"
                default_value = value.get("default_value", "")
                create_file_func(file_name, current_path, default_value)

    """### PATH INDEX COMPLEX INTEGRATION CREATE FUNC ###"""
    def create_directory_piic(self, path):
        self.create_directory(path)
        self.master.paths.complex_init_folder_path(path)

    def create_file_piic(self, file_name, folder_path, content=""):
        self.create_file(file_name, folder_path, content)
        self.master.paths.complex_init_file_path(folder_path, file_name)


    """### PATH INDEX INTEGRATION CREATE FUNC ###"""

    def create_directory_pii(self, path):
        self.create_directory(path)
        self.master.paths.init_folder_path(path)

    def create_file_pii(self, file_name, folder_path, content=""):
        self.create_file(file_name, folder_path, content)
        self.master.paths.init_file_path(folder_path, file_name)


    """### BASE CREATE FUNC ###"""
    def create_file(self, file_name, folder_path, content=""):
        self.create_directory(folder_path)
        full_path = os.path.join(folder_path, file_name)
        if not os.path.exists(full_path):
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Файл '{file_name}' успешно создан в директории '{folder_path}'.")
        else:
            pass
            # print(f"Файл '{file_name}' уже существует в директории '{folder_path}'.")

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"'{path}' успешно создана.")

