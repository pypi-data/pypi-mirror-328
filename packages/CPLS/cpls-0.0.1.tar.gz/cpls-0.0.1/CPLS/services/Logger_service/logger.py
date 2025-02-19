import json
import types

from datetime import datetime
import inspect

import queue
import threading
import time
from pprint import pprint
import hashlib
import uuid


"""
        Уровни логгирования:
        max: максимально логирование
        min: минимальное логирование
        none: логирвоание отсутсвует

        типы логов:
        transition: лог берущийся при переходе от одной функии к другой
        completion: лог берущийся при завершении функции
        momentum:   моментальный лог вызванный в программе 
"""




class LoggerManager:
    def __init__(self, master):
        self.master = master
        self.logs_queue = queue.Queue()
        self.number_batch = 0
        self.interruption = False
        self.last_ids = {}

    def init_logger(self):
        self.log_storage_path = self.master.paths.folders.logs.path
        self.saver_obj = self.master.base_log_saver

    def update_log_mods(self):
        self.logger_config = self.master.paths.logger_config_view.logger_config
        for file_name, logger_config in self.logger_config.items():
            logger_config = {func_name: self.standard_log_mode_j for func_name in logger_config.keys()}
            self.master.json_h.apply_config(getattr(self.master, file_name), {"deep_logger_settings": logger_config})

    def add_log(self, log_dict):
        # print("put1", time.time())
        self.logs_queue.put(log_dict)
        # print("put2", time.time())

    def start(self):
        self.continue_timer()

    def continue_timer(self):
        self.main_loop_thread_timer = threading.Timer(self.logger_loop_delay_j, self.proc_logs)
        self.main_loop_thread_timer.name = "Logger"
        self.main_loop_thread_timer.daemon = True
        self.main_loop_thread_timer.start()

    def proc_logs(self):
        self.main_loop()
        # print(11111111)
        self.continue_timer()

    def main_loop(self):
        start_batch_forming = time.time()
        batch = {}

        # flag = False
        # if self.logs_queue.qsize() > 0:
        #     flag = True

        while self.logs_queue.qsize() > 0:
            try:
                data = self.logs_queue.get(timeout=1)
                # print(4, time.time())
                # print("log")
                log, save_day, save_hour = self.process_log(data, len(batch))

                if save_day not in batch:
                    batch[save_day] = {}
                if save_hour not in batch[save_day]:
                    batch[save_day][save_hour] = []

                # print(5, time.time())
                batch[save_day][save_hour].append(log)

                if time.time() - start_batch_forming > self.send_logs_frequency_j or len(batch) >= self.max_len_batch_j or not self.logs_queue.qsize() > 0:
                    self.saver_obj.add_log(batch.copy(), self.log_storage_path)
                    # print(6, time.time())
                    start_batch_forming = time.time()
                    del batch
                    batch = {}
                    self.number_batch += 1
                    if self.number_batch > 10000: self.number_batch = 0

                # print(4, time.time())
                if not self.interruption:
                    time.sleep(self.log_process_delay_j)
            except queue.Empty:
                pass

        # if flag:
        #     print(f"logger {time.time()}")

    def stop(self):
        self.interruption = True
        self.main_loop_thread_timer.cancel()
        self.main_loop()

    def on_program_exit(self):
        self.stop()
        print(f"Остановка ведения логов")


    def process_log(self, log, log_pos):
        # self.create_min_log("start_process_log", self)

        timestamp      = log.get("time")
        log_type       = log.get("type")
        thread_id      = log.get("thread_id")

        format_date, format_time = self.get_time(timestamp)
        save_hour = format_time.strftime("%H")
        save_day = format_date.strftime("%Y-%m-%d")
        log_id = self.gen_log_id(save_day, save_hour, self.number_batch, log_pos)

        log["format_date"] = format_date
        log["format_time"] = format_time
        log["log_id"]      = log_id

        if log_type in ["min_transition", "max_transition"]:
            self.last_ids[thread_id]  = log_id
        else:
            log["parent_log_id"] = self.last_ids.get(thread_id)

        self.remove_attributes(log, self.log_ignore_attributes_j)
        log_json = json.loads(json.dumps(log, default=str, indent=4))
        if self.flatten_json_j:
            self.flatten_json(log)
        # self.create_min_log("end_process_log", self)
        return log_json, save_hour, save_day

    def get_time(self, timestamp):
        now = datetime.fromtimestamp(timestamp)
        return now.date(), now.time()


    def gen_log_id(self, current_date, current_time, number_batch, log_pos):
        # return hashlib.sha256(f"{current_date}|{current_time}|{number_batch}|{log_pos}".encode()).hexdigest()
        return f"{current_date}|{current_time}|{number_batch}|{log_pos}"


    def remove_attributes(self, d, attributes_to_remove_list):
        if isinstance(d, dict):
            # Проходим по ключам и удаляем те, которые указаны в attributes
            for key in list(d.keys()):
                if key in attributes_to_remove_list:
                    del d[key]
                else:
                    self.remove_attributes(d[key], attributes_to_remove_list)  # Рекурсивно обрабатываем вложенные словари
        elif isinstance(d, list):
            # Если значение - список, рекурсивно обрабатываем его элементы
            for item in d:
                self.remove_attributes(item, attributes_to_remove_list)


    def flatten_json(self, nested_json):
        flat_dict = {}
        for key, value in nested_json.items():
            if isinstance(value, dict) and key in self.master.logger.flatten_accept_j:
                for nested_key, nested_value in value.items():
                    flat_key = f"{key}_{nested_key}"  # Создаем ключ в формате parentKey_nestedKey
                    flat_dict[flat_key] = self.serialize_value(nested_value)
            else:
                flat_dict[key] = self.serialize_value(value)
        return flat_dict


    def serialize_value(self, value):
        """Преобразует списки и словари в строку, а остальные данные возвращает как есть."""
        if isinstance(value, (list, dict)):
            return json.dumps(value, ensure_ascii=False)  # Преобразование в строку
        return value



    """#### MOMENTUM LOGS ####"""
    def create_log(self, identifier, save_args):

        thread_id = threading.get_ident()
        log_time = time.time()
        # current_date, current_time = self.get_time()

        log = {
            "identifier": identifier,
            "save_args": save_args,
            "type": "momentum",
            "thread_id": thread_id,
            "time": log_time,
        }

        # log = {
        #     "save_data": {
        #         "day": current_date,
        #         "time": current_time
        #     },
        #     "identifier": identifier,
        #     "save_args": save_args,
        #     "type": "momentum",
        #     "thread_id": thread_id,
        #     "time": snapshot_time,
        #     "format_day": current_date,
        #     "format_time": current_time
        # }

        self.add_log(log)
        return log

    def create_min_log(self, identifier, obj):
        frame = inspect.currentframe().f_back
        file_name, func_name, line_number, global_vars, local_vars = self.get_frame_inspect_data(frame)

        # current_date, current_time = self.get_time()

        thread_id = threading.get_ident()
        log_time = time.time()

        useful_attributes = self.get_obj_attr_inspect(obj)
        log = {
            "identifier": identifier,
            "func_data": {
                "file_name": file_name,
                "func_name": func_name,
                "calling_line": line_number,
                "global_vars": global_vars,
                "local_vars": local_vars,
                "class_attr": useful_attributes
            },
            "type": "min_momentum",
            "thread_id": thread_id,
            "time": log_time,
        }

        #
        #
        # log = {
        #     "save_data": {
        #         "day": current_date,
        #         "time": current_time
        #     },
        #     "identifier": identifier,
        #     "func_data":{
        #         "file_name": file_name,
        #         "func_name": func_name,
        #         "calling_line": line_number,
        #         "global_vars": global_vars,
        #         "local_vars": local_vars,
        #         "class_attr": useful_attributes
        #     },
        #     "type": "min_momentum",
        #     "thread_id": thread_id,
        #     "time":snapshot_time,
        #     "format_day": current_date,
        #     "format_time": current_time
        # }

        self.add_log(log)
        return log


    def create_max_log(self, obj):
        frame = inspect.currentframe().f_back
        file_name, func_name, line_number, global_vars, local_vars = self.get_frame_inspect_data(frame)

        current_date, current_time = self.get_time()

        thread_id = threading.get_ident()
        snapshot_time = time.time()

        useful_attributes = self.get_obj_attr_inspect(obj)

        log = {
            "save_data": {
                "day": current_date,
                "time": current_time
            },
            "func_data":{
                "file_name": file_name,
                "func_name": func_name,
                "calling_line": line_number,
                "global_vars": global_vars,
                "local_vars": local_vars,
                "class_attr": useful_attributes
            },
            "type": "max_momentum",
            "thread_id": thread_id,
            "time":snapshot_time,
            "format_day": current_date,
            "format_time": current_time
        }

        self.add_log(log)
        return log






    """#### TRANSITION LOGS ####"""
    def create_min_transition_log(self, obj, func, *args, **kwargs):
        func_name, file_name, line_number = self.get_func_data(func)

        current_date, current_time = self.get_time()

        class_attributes = self.get_obj_attr_inspect(obj)

        thread_id = threading.get_ident()
        start_time = time.time()

        log = {
            "save_data": {
                "day": current_date,
                "time": current_time
            },
            "func_data": {
                "file_name": file_name,
                "func_name": func_name,
                "calling_line": line_number,
                "args": args,
                "kwargs": kwargs,
                "class_attr": class_attributes,
            },
            "type": "min_transition",
            "thread_id": thread_id,
            "time": start_time,
            "format_day": current_date,
            "format_time": current_time
        }

        self.add_log(log)
        return log



    def create_max_transition_log(self, obj, func, *args, **kwargs):
        func_name, func_file_name, func_line_number = self.get_func_data(func)

        current_date, current_time = self.get_time()

        signature = inspect.signature(func)  # Получение параметров
        bound_arguments = signature.bind(self, *args, **kwargs)  # Собираем аргументы в словарь
        bound_arguments.apply_defaults()  # Заполняем значениями по умолчанию
        args_dict = dict(bound_arguments.arguments)  # Словарь с параметрами и переданными значениями

        thread_id = threading.get_ident()
        start_time = time.time()

        transition_frame = inspect.currentframe().f_back.f_back
        transition_file_name, transition_func_name, transition_line_number, globals_at_transition, locals_at_transition = self.get_frame_inspect_data(transition_frame)

        useful_attributes = self.get_obj_attr_inspect(obj)

        log = {
            "save_data": {
                "day": current_date,
                "time": current_time
            },
            "calling_func_data": {
                "file_name": transition_file_name,
                "func_name": transition_func_name,
                "calling_line": transition_line_number,
                "global_vars": globals_at_transition,
                "local_vars": locals_at_transition,
            },
            "callable_func_data": {
                "file_name": func_file_name,
                "func_name": func_name,
                "calling_line": func_line_number,
                "transmitted_parameters": args_dict,
                "class_attr": useful_attributes
            },
            "type": "max_transition",
            "thread_id": thread_id,
            "time": start_time,
            "format_day": current_date,
            "format_time": current_time
        }

        self.add_log(log)
        return log




    """#### COMPLETION LOGS ####"""
    def create_min_completion_log(self, obj, result, transition_log):
        current_date, current_time = self.get_time()

        start_time              = transition_log.get("time")
        thread_id               = transition_log.get("thread_id")
        func_data               = transition_log.get("func_data")
        file_name               = func_data.get("file_name")
        func_name               = func_data.get("func_name")
        line_number             = func_data.get("calling_line")


        class_attributes = self.get_obj_attr_inspect(obj)

        end_time = time.time()
        run_time = end_time - start_time

        log = {
            "save_data": {
                "day": current_date,
                "time": current_time
            },
            "func_data": {
                "file_name": file_name,
                "func_name": func_name,
                "calling_line": line_number,
                "returned_data": result,
                "class_attr": class_attributes,
            },
            "type": "min_completion",
            "thread_id": thread_id,
            "start_time": start_time,
            "run_time": run_time,
            "completion_time": end_time,
            "format_day": current_date,
            "format_time": current_time
        }

        self.add_log(log)
        return log



    def create_max_completion_log(self, obj, result, transition_log):
        current_date, current_time = self.get_time()

        start_time              = transition_log.get("time")
        thread_id               = transition_log.get("thread_id")
        callable_func_data      = transition_log.get("callable_func_data")
        func_file_name          = callable_func_data.get("file_name")
        func_name               = callable_func_data.get("func_name")
        func_line_number        = callable_func_data.get("calling_line")

        class_attributes = self.get_obj_attr_inspect(obj)

        end_time = time.time()
        run_time = end_time - start_time

        log = {
            "save_data": {
                "day": current_date,
                "time": current_time
            },
            "callable_func_data": {
                "file_name": func_file_name,
                "func_name": func_name,
                "calling_line": func_line_number,
                "returned_data": result,
                "class_attr": class_attributes,
            },
            "type": "min_completion",
            "thread_id": thread_id,
            "start_time": start_time,
            "run_time": run_time,
            "completion_time": end_time,
            "format_day": current_date,
            "format_time": current_time
        }

        self.add_log(log)
        return log





    """#### SERVICE LOG FUNCS ####"""
    def get_func_data(self, func):
        func_name = func.__name__
        func_code = func.__code__
        func_file_name = func_code.co_filename
        func_line_number = func_code.co_firstlineno

        return func_name, func_file_name, func_line_number

    def get_frame_inspect_data(self, frame):
        code = frame.f_code
        file_name = code.co_filename
        func_name = code.co_name
        line_number = frame.f_lineno
        global_vars = frame.f_globals
        local_vars = frame.f_locals
        return file_name, func_name, line_number, global_vars, local_vars

    def get_obj_attr_inspect(self, obj):
        class_attr = obj.__dict__
        useful_attributes = {
            name: value for name, value in class_attr.items()
            if not name.startswith('__') and not isinstance(value, (
            types.FunctionType, types.MethodType)) and isinstance(value, (int, float, bool, str, list, dict, set, tuple))
        }
        return useful_attributes

    #
    # def get_time(self):
    #     now = datetime.now()
    #     current_date = now.date()
    #     current_time = now.time()
    #     return current_date, current_time

