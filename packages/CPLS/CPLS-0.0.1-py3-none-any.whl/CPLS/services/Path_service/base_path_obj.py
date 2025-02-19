from pprint import pprint

from pydantic import BaseModel, Field, model_validator, field_validator,  ConfigDict
from typing import Optional, Dict, Union, List
import os

class PathFile(BaseModel):
    model_config = ConfigDict(extra="allow")  # Поле - расширение конфигурации pydantic для динамического добавления атрибутов
    name:                   str                     = Field(..., description="Название файла")
    type:                   str                     = Field(..., description="Тип файла (расширение, например, 'txt', 'csv')")
    path:                   str                     = Field(..., description="Полный путь к файлу")
    path_name:              str                     = Field(..., description="Название файла с форматом данных")
    relative_path:          str                     = Field(..., description="Относителньый путь к файлу")
    split_path:             List[str]               = Field(..., description="Полный путь к файлу, разбитый на части, например ['C:', 'User', 'test.txt']")
    split_relative_path:    List[str]               = Field(..., description="Относительный путь к файлу, разбитый на части, например ['telegram', 'test.txt']")
    root_folder_path:       str                     = Field(..., description="Путь к root папке")
    folder_path:            str                     = Field(..., description="Путь к родителю")
    folder:                 Optional["PathFolder"]  = Field(None, description="Объект папки")

    @model_validator(mode="before")
    def validate_and_route(cls, values):
        file_name = values.get("file_name")
        del values["file_name"]
        path_folder = values.get("folder_path")
        root_folder_path = values.get("root_folder_path")
        params = cls.unpack_path_file(file_name, path_folder, root_folder_path)
        values.update(params)
        return values

    @classmethod
    def unpack_path_file(cls, file_name, path_folder, root_folder_path):
        name, file_type = os.path.splitext(file_name)
        if name[0] in ["."]:
            name = name[1:]
            file_type = name
        else:
            file_type = file_type.lstrip('.')

        file_params = {}
        file_params["name"] = name
        file_params["type"] = file_type
        file_params["path_name"] = file_name
        file_params["path"] = os.path.join(path_folder, file_name)
        file_params["relative_path"] = os.path.relpath(file_params["path"], root_folder_path)
        file_params["split_path"] = file_params["path"].split(os.sep)
        file_params["split_relative_path"] = file_params["relative_path"].split(os.sep)

        return file_params

    def set_folder_obj(self, folder_obj):
        self.folder = folder_obj

    def get_explicitly_defined_parameters(self):
        return set(self.__pydantic_fields__.keys())

    def get_all_parameters(self):
        return self.__pydantic_fields_set__

    def get_hidden_parameters(self):
        all_parameters = self.get_all_parameters()
        explicitly_parameters = self.get_explicitly_defined_parameters()
        return all_parameters - explicitly_parameters



class PathFolder(BaseModel):
    model_config = ConfigDict(extra="allow") # Поле - расширение конфигурации pydantic для динамического добавления атрибутов
    name:                   str                         = Field(..., description="Название текущей папки")
    parent_name:            str                         = Field(..., description="Имя родительской папки")
    path:                   str                         = Field(..., description="Полный путь к текущей папке")
    parent_path:            str                         = Field(..., description="Полный путь к родительской папке")
    relative_path:          str                         = Field(..., description="Относительный путь к текущей папке от корня проекта")
    split_path:             List[str]                   = Field(..., description="Полный путь к папке, разбитый на части, например ['C:', 'User', 'Documents']")
    split_relative_path:    List[str]                   = Field(..., description="Относительный путь к папке, разбитый на части, например ['telegram', 'chat_history']")
    root_folder_path:       str                         = Field(..., description="Путь к root папке")
    children_folders_str:          Optional[List[str]]                  = Field(default_factory=list, description="Список имен дочерних папок в виде строк")
    full_children_folders_str:     Optional[List[str]]                  = Field(default_factory=list, description="Список полных путей к дочерним папкам")
    children_files_str:         Optional[List[str]]                  = Field(default_factory=list, description="Список имен дочерних файлов в виде строк")
    full_children_files_str:    Optional[List[str]]                  = Field(default_factory=list, description="Список полных путей к дочерним файлам")

    parent:                 Optional["PathFolder"]         = Field(None, description="Объект родителя")
    children_folders:       Optional[List["PathFolder"]]   = Field(default_factory=list, description="Список дочерних папок в виде объектов Pathfolder")
    children_files:         Optional[List["PathFile"]]     = Field(default_factory=list, description="Список дочерних файлов в виде строк")

    file_count:                Optional[int]               = Field(None, description="Количество файлов в директории")
    folder_count:              Optional[int]               = Field(None, description="Количество поддиректорий в директории")

    # Тут динамически добавляются все ссылки на обьекты директорий, например repository.path_block

    @model_validator(mode="before")
    def validate_and_route(cls, values):
        path                = values.get("path")
        root_folder_path    = values.get("root_folder_path")

        params = cls.unpack_path(path, root_folder_path)
        values.update(params)
        # pprint(values)
        return values

    @classmethod
    def unpack_path(cls, path, root_folder_path):
        split_root = path.split(os.sep)
        relative_path = os.path.relpath(path, root_folder_path)
        split_relative_root_folders = relative_path.split(os.sep)

        folder_name                    = split_root[-1]
        parent_name                 = split_root[-2]
        parent_path                 = os.path.dirname(path)

        params = {
            "name": folder_name,
            "parent_name": parent_name,
            "path": path,
            "parent_path": parent_path,
            "relative_path": relative_path,
            "split_path": split_root,
            "split_relative_path": split_relative_root_folders,
        }

        return params

    def update_values(self):
        self.__pydantic_fields_set__.update(self.get_explicitly_defined_parameters())
        self.set_full_child_folders()
        self.set_full_child_files()
        self.update_count_value()

    def update_count_value(self):
        self.file_count = len(self.children_files)
        self.folder_count  = len(self.children_folders)

    def set_full_child_folders(self):
        self.full_children_folders_str = [os.path.join(self.path, d) for d in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, d))]

    def set_full_child_files(self):
        self.full_children_files_str = [os.path.join(self.path, f) for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

    def set_parent_obj(self, parent_obj):
        self.parent = parent_obj

    def set_children_folder(self, children_folder: "PathFolder"):
        self.children_folders_str.append(children_folder.name)
        self.add_params(self.children_folders, children_folder)

    def set_children_file(self, children_file: "PathFile"):
        self.children_files_str.append(children_file.name)
        self.add_params(self.children_files, children_file)

    def add_params(self, changeable_array, add_data):

        changeable_array.append(add_data)
        if hasattr(self, add_data.name):
            print(
                f"Внимание риск повторения: В проекте одинаковые названия файлов {add_data.name} на уровне {self.name}")
        else:
            setattr(self, add_data.name, add_data)
            self.__pydantic_fields_set__.add(add_data.name)

    def get_explicitly_defined_parameters(self):
        return set(self.__pydantic_fields__.keys())

    def get_all_parameters(self):
        return self.__pydantic_fields_set__

    def get_hidden_parameters(self):
        all_parameters = self.get_all_parameters()
        explicitly_parameters = self.get_explicitly_defined_parameters()
        return all_parameters - explicitly_parameters
