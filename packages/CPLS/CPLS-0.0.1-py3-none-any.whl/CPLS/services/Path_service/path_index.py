import os
import sys
import pathlib
import json
from .base_path_obj import PathFile, PathFolder
from .category import Folders, Files, TreeProject, MasterView, ConfigsFolderView, ConfigFileView, LoggerView


class Paths:
    def __init__(self, master):
        print("INIT PATHS")
        self.master = master

        self.parent_children_all_folder = {}
        self.parent_children_all_file   = {}



    """### INIT VAR ###"""
    def init_base_path(self):
        self.base_configs_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "base_configs")

        self.start_file_path            = os.path.abspath(sys.argv[0])
        self.start_file_name_path       = os.path.basename(self.start_file_path)
        self.start_file_name            = self.start_file_name_path.split(".")[0]

        self.repository_path            = os.path.dirname(self.start_file_path)
        self.repo_folder_name           = os.path.basename(self.repository_path)

        self.root_folder_path           = os.path.dirname(self.repository_path)

    def init_path(self, obj, name, path):
        setattr(obj, name, path)

    def init_view(self):
        self.folders            = Folders()
        self.files              = Files()

        self.master_view            = MasterView()
        self.configs_folder_view    = ConfigsFolderView()

        self.global_configs_view     = ConfigFileView()
        self.local_configs_view      = ConfigFileView()

        self.logger_config_view = LoggerView()

    """### MAIN RUN ###"""

    def update_base_tree(self):
        self.analysis_paths_way()
        self.update_links_base_tree()

    """### RUN STEP 1 ###"""
    def analysis_paths_way(self):
        for root, folders, files in os.walk(self.root_folder_path):
            is_unnecessary_folder = self.get_is_unnecessary_folder(root)
            if not is_unnecessary_folder:
                self.add_folder(root)
                for file_name in files:
                    is_unnecessary_file = self.get_is_unnecessary_file(file_name)
                    if not is_unnecessary_file:
                        self.add_file(root, file_name)

    """### analysis_paths_way SERVICE FUNC ###"""
    def get_is_unnecessary_folder(self, path):
        relative_path                   = os.path.relpath(path, self.root_folder_path)
        split_relative_root_folders     = relative_path.split(os.sep)
        is_unnecessary = bool(set(split_relative_root_folders) & set(self.base_tree_analysis_ignore_j))
        return is_unnecessary

    def get_is_unnecessary_file(self, file_name):
        name, file_type = os.path.splitext(file_name)
        if name in self.base_tree_analysis_ignore_j:
            return True

    def add_folder(self, path):
        if path not in self.parent_children_all_folder:
            init_params = {"path": path, "root_folder_path": self.root_folder_path}
            current_folder = PathFolder(**init_params)
            self.parent_children_all_folder[path] = current_folder

    def add_file(self, folder_path, file_name):
        full_path = os.path.join(folder_path, file_name)
        if full_path not in self.parent_children_all_file:
            init_params = {"file_name": file_name, "folder_path": folder_path, "root_folder_path": self.root_folder_path}
            file_obj = PathFile(**init_params)
            self.parent_children_all_file[full_path] = file_obj


    """### RUN STEP 2 ###"""
    def update_links_base_tree(self):
        # print(self.parent_children_all_folder.keys())
        # print(self.parent_children_all_file.keys())
        root = getattr(self, "root", None)
        if not root:
            self.root = self.parent_children_all_folder.get(self.root_folder_path)
            print(f"Ядро системы путей: {self.root.path}")
        self.update_links_files()
        self.update_links_folders()


    """### update_links_base_tree SERVICE FUNC ###"""
    def update_links_files(self):
        for i, file_obj in enumerate(self.parent_children_all_file.values()):
            folder = self.parent_children_all_folder.get(file_obj.folder_path, None)
            if folder:
                if file_obj.folder is None or folder.path != file_obj.folder.path:
                    file_obj.set_folder_obj(folder)
                    folder.set_children_file(file_obj)
            else:
                print(f"Ошибка разрыва пути: Файл {file_obj.path} висит в воздухе (не имеет родительской папки в индексе)")


    def update_links_folders(self):
        for i, folder_obj in enumerate(self.parent_children_all_folder.values()):
            parent_obj = self.parent_children_all_folder.get(folder_obj.parent_path, None)
            if parent_obj:
                if folder_obj.parent is None or parent_obj.path != folder_obj.parent.path:
                    parent_obj.set_children_folder(folder_obj)
                    folder_obj.set_parent_obj(parent_obj)
                    folder_obj.update_values()


    """### RUN STEP 3 ###"""
    def update_main_view_processing(self):
        self.processing_tree()
        self.processing_folders()
        self.processing_files()
        self.processing_master_view()
        self.processing_configs_folders_view()
        self.processing_logger_view()

    def update_second_view_processing(self):
        if self.folder_global_configs_j:
            self.processing_global_config_view()
        if self.folder_local_configs_j:
            self.processing_local_configs_view()

    """### update_view_processing SERVICE FUNC ###"""
    def processing_tree(self):
        if hasattr(self, "root"):
            self.tree = TreeProject(root=self.root)
        else:
            print("Ошибка Древовидного Представления: Корневой узен не найден")

    def processing_folders(self):
        for i, folder_obj in enumerate(self.parent_children_all_folder.values()):
            if not set(folder_obj.split_path) & (set(self.folders_view_ignore_j) | set([self.local_config_folder_name, self.global_config_folder_name])):
                self.folders.set_folder(folder_obj)


    def processing_files(self):
        for i, file_obj in enumerate(self.parent_children_all_file.values()):
            if not set(file_obj.split_path) & (set(self.folders_view_ignore_j) | set([self.local_config_folder_name, self.global_config_folder_name])) and not file_obj.name in self.folders_view_ignore_j:
                self.files.set_file(file_obj)


    def processing_master_view(self):
        self.master_view.set_init_ignore(set(self.base_init_ignore_j), set(self.init_ignore_j))
        repo_folder_name = os.path.basename(self.repository_path)
        for i, file in enumerate(self.files.all_file_obj):
            self.master_view.set_file(file, repo_folder_name)


    def processing_configs_folders_view(self):
        repo_obj = getattr(self.folders, self.repo_folder_name)
        ignore_list = self.configs_folder_view_ignore_j.copy()
        ignore_list.extend(self.init_ignore_j)
        ignore_list.extend([self.local_config_folder_name, self.global_config_folder_name])
        data_config = self.data_config_j
        self.configs_folder_view.create_config(repo_obj, data_config, ignore_list)

    def processing_global_config_view(self):
        global_config_obj = getattr(self.parent_children_all_folder[self.global_config_folder_path], self.start_file_name)
        ignore_list = self.init_ignore_j.copy()
        self.global_configs_view.add_config(global_config_obj, ignore_list)

    def processing_local_configs_view(self):
        local_config_obj = getattr(self.parent_children_all_folder[self.local_config_folder_path], self.start_file_name)
        ignore_list = self.init_ignore_j.copy()
        self.local_configs_view.add_config(local_config_obj, ignore_list)

    def processing_logger_view(self):
        self.logger_config_view.set_init_ignore(set(self.base_init_ignore_j), set(self.init_ignore_j))
        repo_folder_name = os.path.basename(self.repository_path)
        for i, file in enumerate(self.files.all_file_obj):
            self.logger_config_view.set_file(file, repo_folder_name)

    """### PATH INDEX API ###"""
    def complex_init_folder_path(self, folder_path):
        parent_folder_path = os.path.dirname(folder_path)
        if parent_folder_path in self.parent_children_all_folder:
            self.init_folder_path(folder_path)
        else:
            if folder_path == self.root_folder_path:
                print("Ошибка инициализации Path_index: Достигнута максимальная длина рекурсии")
            else:
                self.complex_init_folder_path(parent_folder_path)

    def init_folder_path(self, folder_path):
        self.add_folder(folder_path)
        self.update_links_base_tree()
        self.update_main_view_processing()

    def complex_init_file_path(self, folder_path, file_name):
        if folder_path not in self.parent_children_all_folder:
            self.complex_init_folder_path(folder_path)
        self.init_file_path(folder_path, file_name)

    def init_file_path(self, folder_path, file_name):
        self.add_file(folder_path, file_name)
        self.update_links_base_tree()
        self.update_main_view_processing()

    def is_subpath(self, base_path, verifiable_path):
        if os.path.commonpath([os.path.abspath(base_path), os.path.abspath(verifiable_path)]) == os.path.abspath(base_path):
            return True
        else:
            return False

    def print_init_config(self):
        print("Init Config\n" + str(json.dumps(self.master_view.init_config, indent=4)))
        print("Ignore Config\n" + str(self.master_view.init_ignore))

    def print_base_path_tree(self, indent_txt=" ", indent_lvl=1):
        node = self.tree.root
        print(node.name)
        self.print_tree(node, indent_txt=indent_txt, indent_lvl=indent_lvl)

    def print_tree(self, node, indent_txt=" ", indent_lvl=1):
        indent = indent_txt * (indent_lvl * 4)  # Отступ для текущего уровня
        for obj in node.children_folders:
            print(f"{indent}{obj.name}")
            self.print_tree(obj, indent_lvl=indent_lvl + 1)
        for obj in node.children_files:
            print(f"{indent}{obj.name}")


