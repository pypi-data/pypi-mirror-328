from pydantic import BaseModel, Field, model_validator, field_validator,  ConfigDict
from typing import Optional, Dict, Union, List, ForwardRef
from .base_path_obj import PathFile, PathFolder
import sys

class TreeProject(BaseModel):
    name: str
    path: str
    root: PathFolder

    @model_validator(mode="before")
    def main_validation(cls, values):
        obj_root        = values.get("root")
        values["name"]  = obj_root.parent_name
        values["path"]  = obj_root.parent_path
        return values

class Files(BaseModel):
    model_config = ConfigDict(extra="allow")  # Поле - расширение конфигурации pydantic для динамического добавления атрибутов
    all_file_name:  Optional[List[str]] = []
    all_paths:      Optional[List[str]] = []
    all_file_obj:   Optional[List["PathFile"]] = []
    # Тут динамически добавляются все ссылки на обьекты директорий, например telegram_block

    def set_file(self, file: "PathFile"):
        current_obj = getattr(self, file.name, None)
        if not current_obj or current_obj.path != file.path:
            self.all_paths.append(file.path)
            self.all_file_name.append(file.name)
            self.all_file_obj.append(file)

            if hasattr(self, file.name):
                print(f"Внимание риск повторения: В проекте одинаковые названия файлов {file.name}")
            else:
                setattr(self, file.name, file)
                self.__pydantic_fields_set__.add(file.name)


class Folders(BaseModel):
    model_config = ConfigDict(extra="allow")  # Поле - расширение конфигурации pydantic для динамического добавления атрибутов
    all_folder_name:   Optional[List[str]] = []
    all_paths:      Optional[List[str]] = []
    all_folder_obj:    Optional[List["PathFolder"]] = []
    # Тут динамически добавляются все ссылки на обьекты директорий, например telegram_block

    def set_folder(self, folder: "PathFolder"):
        current_obj = getattr(self, folder.name, None)
        if not current_obj or current_obj.path != folder.path:
            self.all_paths.append(folder.path)
            self.all_folder_name.append(folder.name)
            self.all_folder_obj.append(folder)

            if hasattr(self, folder.name):
                print(f"Внимание риск повторения: В проекте одинаковые названия папок {folder.name}")
            else:
                setattr(self, folder.name, folder)
                self.__pydantic_fields_set__.add(folder.name)



import ast

class MasterView(BaseModel):
    init_config: Optional[dict] = Field({}, description="Поле для инициализации проекта Masterом")
    init_ignore: Optional[set[str]] = Field(set(), description="Список модулей или папок для игнорирования инициализации")

    def set_init_ignore(self, base_init, init_ignore):
        self.init_ignore = set()
        self.init_ignore.update(base_init)
        self.init_ignore.update(init_ignore)

    def set_file(self, file: "PathFile", repo_folder_name: str):
        file_type = file.type
        if file_type == "py":
            split_relative_path     = file.folder.split_relative_path
            if repo_folder_name in split_relative_path:
                split_import_path = split_relative_path[1:]
                # if split_import_path:
                split_import_path.append(file.name)
                if not set(split_import_path) & self.init_ignore:
                    import_path         = ".".join(split_import_path)
                    path                = file.path
                    classes_in_file     = self.get_classes_in_file(path)

                    self.init_config[import_path] = {"file_name": split_import_path[-1],"classes_in_file": classes_in_file}

    def get_classes_in_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        tree = ast.parse(file_content, filename=file_path)
        classes_in_file = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        return classes_in_file


class ConfigsFolderView(BaseModel):
    configs_folder_struct: Optional[dict] = Field({}, description="Структура создания папки Configs")
    configs_struct_json_sender: Optional[dict] = Field({}, description="Конфиг отправки json онфигураций")

    def create_config(self, repo_folder_obj, data_config, ignore_list):
        config = {}
        self.recursive_creation(repo_folder_obj, config, data_config, ignore_list)
        self.configs_folder_struct = config

    def recursive_creation(self, root_obj, config_node, final_element, ignore_list):
        for param in root_obj.get_hidden_parameters():
            obj = getattr(root_obj, param)
            if obj.name not in ignore_list:
                config_node[obj.name] = {}
                if obj.get_hidden_parameters():
                    self.recursive_creation(obj, config_node[obj.name], final_element, ignore_list)
                else:
                    if hasattr(obj, "type") and obj.type == "py":
                        config_node[obj.name] = final_element
                        self.configs_struct_json_sender[obj.name] = [obj.name]


class ConfigFileView(BaseModel):
    model_config = ConfigDict(extra="allow")  # Поле - расширение конфигурации pydantic для динамического добавления атрибутов
    all_config_names: Optional[List[str]] = []
    all_config_paths: Optional[List[str]] = []
    all_config_obj: Optional[List["PathFolder"]] = []

    def add_config(self, root_obj, ignore_list):
        for file in root_obj.children_files:
            if file.name not in ignore_list and file.type == "json":
                self.add_node(file)

        for folder in root_obj.children_folders:
            if folder.name not in ignore_list:
                self.add_config(folder, ignore_list)

    def add_node(self, obj):
        self.all_config_paths.append(obj.path)
        self.all_config_names.append(obj.name)
        self.all_config_obj.append(obj)

        if hasattr(self, obj.name):
            temp_obj = getattr(self, obj.name)
            if temp_obj != obj:
                print(f"Внимание риск повторения: В проекте одинаковые названия папок {obj.name}")
        else:
            setattr(self, obj.name, obj)
            self.__pydantic_fields_set__.add(obj.name)



class LoggerView(BaseModel):
    logger_config: Optional[dict] = {}
    init_ignore: Optional[set[str]] = Field(set(), description="Список модулей или папок для игнорирования инициализации")

    def set_init_ignore(self, base_init, init_ignore):
        self.init_ignore = set()
        self.init_ignore.update(base_init)
        self.init_ignore.update(init_ignore)


    def set_file(self, file: "PathFile", repo_folder_name):
        file_type = file.type
        if file_type == "py":
            split_relative_path     = file.folder.split_relative_path
            if repo_folder_name in split_relative_path:
                split_import_path = split_relative_path[1:]
                split_import_path.append(file.name)
                if not set(split_import_path) & self.init_ignore:
                    path                = file.path
                    funcs_list          = self.get_logger_node(path)

                    self.logger_config[file.name] = {func_name:None for func_name in funcs_list}

    def get_logger_node(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        tree = ast.parse(file_content, filename=file_path)
        functions_in_classes = [
            n.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)
            for n in node.body if isinstance(n, ast.FunctionDef)
        ]
        return functions_in_classes


