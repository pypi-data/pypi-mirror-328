import json
import os

class JsonLogSaver:
    def __init__(self, master):
        self.master = master

    def loging_iteration(self, hour, day, folder_path, batch):
        file_name = hour + "h_" + day + ".json"
        self.master.creator.create_file_pii(file_name, folder_path, content="[]")
        file_path = os.path.join(folder_path, file_name)
        json_data = self.master.json_h.unload(file_path, not_found_return = [])
        json_data.extend(batch)
        self.master.json_h.load(json_data, file_path)


