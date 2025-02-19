import json
import os
from fix_busted_json import repair_json

class JsonHandler:
    def __init__(self, master):
        print("INIT JSON_H")
        self.master = master

    """### HIGH_LEVEL FUNC ###"""
    def update_all_repo_configs(self):
        self.mailing_by_conf(self.master.paths.configs_folder_view.configs_struct_json_sender)
        if hasattr(self.master.paths.global_configs_view, "json_config_sender"):
            send_config = self.unload(self.master.paths.global_configs_view.json_config_sender.path, {})
            self.mailing_by_conf(send_config)
        if hasattr(self.master.paths.local_configs_view, "json_config_sender"):
            send_config = self.unload(self.master.paths.local_configs_view.json_config_sender.path, {})
            self.mailing_by_conf(send_config)

    def mailing_by_conf(self, config):
        for subject_name, config_names in config.items():
            for config_name in config_names:
                try:
                    if self.paths.folder_global_configs_j:
                        global_path_obj = getattr(self.master.paths.global_configs_view, config_name)
                        self.unload_config(subject_name, global_path_obj.path)
                except:
                    print(f"Ошибка загрузки глобального конфига {config_name}")

                try:
                    if self.paths.folder_local_configs_j:
                        local_path_obj = getattr(self.master.paths.local_configs_view, config_name)
                        self.unload_config(subject_name, local_path_obj.path)
                except:
                    print(f"Ошибка загрузки локального конфига {config_name}")

    """### UPDATING FUNCTIONS ###"""
    def unload_config(self, subject, path):
        if isinstance(subject, str):
            try:
                obj = getattr(self.master, subject)
            except:
                print(f"Ошибка получения обьекта {subject}")
            self.get_json(obj, path)
        elif isinstance(subject, object) and not isinstance(self, (type(None), int, float, str, list, dict, tuple)):
            self.get_json(subject, path)


    def load(self, data, path):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def unload(self, path, not_found_return = False):
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Обнаружен поврежденный json {e}")
                return self._try_repair_json(path, not_found_return)
        else:
            return not_found_return



    """### SYSTEM FUNCTIONS ###"""
    def get_json(self, obj, path):
        config = self.unload(path, not_found_return={})
        self.apply_config(obj, config)

    def apply_config(self, obj, config):
        for var_name, value in config.items():
            self.add_variable(obj, var_name, value)

    def add_variable(self, obj, var_name, value):
        setattr(obj, f"{var_name}_j", value)  # Добавляем переменную в объект

    def _try_repair_json(self, path, not_found_return):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()

            backup_path = f"{path.split('.')[0]}_backup.{path.split('.')[1]}"
            print(f"{path} backup json сохранён")
            with open(backup_path, 'w', encoding='utf-8') as file:
                file.write(content)

            repaired_data = json.loads(repair_json(content))

            self.load(repaired_data, path)
            print("JSON успешно восстановлен и сохранён.")
            return repaired_data
        except Exception as e:
            print(f"Не удалось восстановить JSON: {e}")
            return not_found_return
