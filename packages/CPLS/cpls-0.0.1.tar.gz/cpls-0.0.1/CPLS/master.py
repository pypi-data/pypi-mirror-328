import importlib
import atexit

from .services.Path_service.path_index                    import Paths
from .services.Creator_service.creator                    import Creator
from .services.Conf_manager_service.configs_manager       import ConfigsManager
from .services.File_observer_service.file_observer        import FileChangeHandler
from .services.Json_h.json_h                              import JsonHandler
from .services.Custom_garbage_collector_service.cgc       import CGC
from .services.Logger_service.logger                      import LoggerManager
from .services.Logger_service.base_saver                  import BaseLogSaver

class BaseMaster:
    def __init__(self, main_thread_obj):
        print("START MASTER")
        print("### INIT SERVICES ###")
        self.init_services()
        self.main_thread_obj = main_thread_obj(self)
        print("\n### SERVICES START ###")
        self.run_services()
        self.set_config()
        atexit.register(self.stop_services)
        print("\n### INIT MODULES ###")
        self.init_modules()
        self.init_modules_complex()
        print("\n### START MODULES ###")
        self.start_modules()
        self.main_thread_obj.main_loop()
        print("\n### STOP MODULES ###")
        self.stop_modules()
        print("\n### SERVICES STOP ###")
        self.stop_services()
        atexit.unregister(self.stop_services)
        print("END MASTER")


    def init_services(self):
        self.cgc                        = CGC(self)
        self.json_h                     = JsonHandler(self)
        self.creator                    = Creator(self)

        self.paths                      = Paths(self)
        self.configs_manager            = ConfigsManager(self)
        self.file_observer              = FileChangeHandler(self)
        self.logger                     = LoggerManager(self)
        self.base_log_saver             = BaseLogSaver(self)

    def run_services(self):
        self.paths.init_base_path()
        self.paths.init_view()
        self.file_observer.init_observer()
        self.configs_manager.load_service_configs()
        self.paths.update_base_tree()
        self.paths.update_main_view_processing()
        self.creator.creation_by_config_pii(self.paths.base_folder_structure_j, self.paths.root_folder_path)
        self.creator.creation_by_config_pii(self.paths.folder_structure_j, self.paths.root_folder_path)
        self.configs_manager.create_configs_folders()
        self.paths.update_second_view_processing()
        self.file_observer.run()
        self.cgc.clear()
        self.logger.init_logger()
        self.logger.start()
        self.base_log_saver.start()
        self.base_log_saver.init_saver()

    def set_config(self):
        self.complex_init_config    = set(self.paths.base_complex_init_j)
        self.start_stop_config      = []


    def init_modules(self):
        for module_path, module_config in self.paths.master_view.init_config.items():
            for class_name in module_config["classes_in_file"]:
                if class_name not in self.paths.init_class_ignore_j:
                    module_name, module_type = self._initialize_class(module_path, class_name, module_config["file_name"], master=self)
                    if module_name != None:
                        self.print_state_file("INIT", module_path, module_name)
                        self.complex_init_config.add(module_name)
                    if module_type == "thread":
                        self.start_stop_config.append(module_name)

    def init_modules_complex(self):
        ordered_list = sorted(self.complex_init_config, key=lambda x: (self.paths.complex_init_order_j.index(x) if x in self.paths.complex_init_order_j else len(self.paths.complex_init_order_j), x))
        complex_links_conf = {module_name: getattr(self, module_name) for module_name in ordered_list}
        for module in complex_links_conf.values():
            for module_name, dependence in complex_links_conf.items():
                if module != dependence:
                    setattr(module, module_name, dependence)

        self.logger.update_log_mods()
        self.json_h.update_all_repo_configs()

        for module in complex_links_conf.values():
            if hasattr(module, "_complex_init"):
                module._complex_init()

    def start_modules(self):
        self.start_stop_config.sort(key=lambda x: (self.paths.start_order_j.index(x) if x in self.paths.start_order_j else len(self.paths.start_order_j), x))
        for module_name in self.start_stop_config:
            self.print_state_file("START", module_name, "", "")
            module = getattr(self, module_name)
            module.start()

    def stop_modules(self):
        self.start_stop_config.sort(key=lambda x: (self.paths.stop_order_j.index(x) if x in self.paths.stop_order_j else len(self.paths.stop_order_j), x))
        for module_name in self.start_stop_config:
            self.print_state_file("STOP", module_name, "", "")
            module = getattr(self, module_name)
            module.stop()

    def stop_services(self):
        self.logger.on_program_exit()
        self.base_log_saver.stop()
        self.file_observer.on_program_exit()
        self.cgc.on_program_exit()

    def _initialize_class(self, import_path, class_name, file_name, master):
        try:
            module = importlib.import_module(import_path)
            class_ = getattr(module, class_name)
            instance = class_(master)
            # if hasattr(instance, 'module_name'):
            #     setattr(master, instance.module_name, instance)
            #     return instance.module_name, instance.module_type
            # else:
            setattr(master, file_name, instance)
            return file_name, instance.module_type
        except Exception as ex:
            print(f"Ошибка инициализации {ex}")
            return None, None



    def print_state_file(self, state, module_path, module_name, split_char = "="):
        print(f"{state} {' -> '.join(module_path.upper().split('.'))} {split_char} {module_name}")
