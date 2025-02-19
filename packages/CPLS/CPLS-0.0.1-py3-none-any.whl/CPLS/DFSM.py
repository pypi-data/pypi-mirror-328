
import os
import threading
import time
from .BaseDFSM import BaseDFSM

class DFSM(BaseDFSM):
    def __init__(self, master):
        print("INIT DFSM")
        super().__init__(master)

    """Основа DFSM"""
    def _complex_init(self):
        if self.paths.folder_global_configs_j:
            self.creator.create_file_pii("DFSM_config.json", os.path.join(self.paths.global_config_folder_path, self.paths.start_file_name), "{}")
        if self.paths.folder_local_configs_j:
            self.creator.create_file_pii("DFSM_config.json", os.path.join(self.paths.local_config_folder_path, self.paths.start_file_name), "{}")

        if self.paths.folder_global_configs_j:
            self.states_config = self.json_h.unload(os.path.join(self.paths.global_config_folder_path, self.paths.start_file_name, "DFSM_config.json"))
        else:
            self.states_config = {}
        if self.paths.folder_local_configs_j:
            self.states_config.update(self.json_h.unload(os.path.join(self.paths.local_config_folder_path, self.paths.start_file_name, "DFSM_config.json")))

        storage_path = os.path.join(self.paths.folders.temp.path, "DFSM_states")
        self.creator.create_directory_pii(storage_path)
        self.db_sates = os.path.join(self.paths.folders.DFSM_states.path, "DFSM_db_states.json")
        self.get_project_states_json()

        self.wait_event = threading.Event()
        self.set_start_state()

    def set_start_state(self):
        self.set_state("master", "main", "wait")

    def set_state(self, class_name, division_id, state):
        curr_state = self.get_state(class_name, division_id, "current_state")
        if curr_state == "wait":
            self.wait_event.set()
        if state == "wait":
            self.wait_event.clear()
        super().set_state(class_name, division_id, state)


    def main_loop(self):
        print("START DFSM")
        self.is_main_loop = True
        while self.is_main_loop:
            self.distributions_prompt(self, "master", "main", locals())
        print("STOP DFSM")

    def wait(self):
        self.wait_event.wait()

    def stop(self):
        self.is_main_loop = False
