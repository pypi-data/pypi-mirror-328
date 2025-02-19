import types
from typing import Any, Coroutine, Optional, List
import threading
import queue
import time
import inspect
from datetime import datetime
from pprint import pprint
import traceback
import hashlib
import uuid
import asyncio


class LoggerMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not (attr_name.startswith('__') and attr_name.endswith('__')) and not attr_name == "_complex_init":  # Если атрибут является методом
                # print(attr_name)

                # Оборачиваем метод
                def log_wrapper_creator(func, is_async):
                    def log_transition(self, func_log_mode):

                        # print(2, time.time())
                        if func_log_mode == "max":
                            transition_log = self.master.logger.create_max_transition_log(self, func, *args, **kwargs)
                        elif func_log_mode == "min":
                            transition_log = self.master.logger.create_min_transition_log(self, func, *args, **kwargs)
                        else:
                            transition_log = None
                        # self.times.append(f"9.3 {time.time()}")

                        # print(3, time.time())
                        return transition_log

                    def log_completion(self, func_log_mode, result, transition_log):
                        # self.times.append(f"9.4 {time.time()}")

                        # print(4, time.time())
                        if func_log_mode == "max":
                            self.master.logger.create_max_completion_log(self, result, transition_log)
                        elif func_log_mode == "min":
                            self.master.logger.create_min_completion_log(self, result, transition_log)

                        # self.times.append(f"9.5 {time.time()}")

                        # print(5, time.time())

                    def logging_wrapper(self, *args, **kwargs):
                        # if "count" not in self.__dict__.keys():
                        #     self.count = 0
                        # self.count +=1
                        # print(self.count)

                        # if "times" not in self.__dict__.keys():
                        #     self.times = []
                        # self.times.append(f"9.1 {time.time()}")

                        # print(1, time.time())
                        func_name = func.__name__
                        deep_func_log_mode = self.deep_logger_settings_j.get(func_name)
                        func_log_mode = self.logger_settings_j.get(func_name) if hasattr(self,
                                                                                         "logger_settings_j") else None
                        if func_log_mode is None:
                            func_log_mode = deep_func_log_mode

                        # self.times.append(f"9.2 {time.time()}")

                        transition_log = log_transition(self, func_log_mode)
                        result = func(self, *args, **kwargs)
                        log_completion(self, func_log_mode, result, transition_log)
                        return result

                    async def async_logging_wrapper(self, *args, **kwargs):
                        func_name = func.__name__
                        deep_func_log_mode = self.deep_logger_settings_j.get(func_name)
                        func_log_mode = self.logger_settings_j.get(func_name) if hasattr(self, "logger_settings_j") else None
                        if func_log_mode is None:
                            func_log_mode = deep_func_log_mode

                        transition_log = log_transition(self, func_log_mode)
                        result = await func(self, *args, **kwargs)
                        log_completion(self, func_log_mode, result, transition_log)
                        return result

                    if is_async:
                        return async_logging_wrapper
                    else:
                        return logging_wrapper

                if asyncio.iscoroutinefunction(attr_value):
                    dct[attr_name] = log_wrapper_creator(attr_value, True)
                else:
                    dct[attr_name] = log_wrapper_creator(attr_value, False)

        return super().__new__(cls, name, bases, dct)

    def log_call_stack(cls):
        stack = inspect.stack()
        for frame in stack:
            print(f"Function: {frame.function}, Line: {frame.lineno}, File: {frame.filename}")


class BaseProcedure(metaclass=LoggerMeta):
    module_type = "procedure"
    def __init__(self, master):
        self.master = master


class BaseThread(metaclass=LoggerMeta):
    module_type = "thread"
    def __init__(self, master):
        self.master = master
        self.command_queue = queue.Queue()

    def start(self):
        self.main_loop_thread = threading.Thread(target=self.main_loop, daemon=True)
        self.main_loop_thread.start()

    def add_command(self, command, *args):
        # result_queue = queue.Queue()
        result_queue = None
        self.command_queue.put((command, args, result_queue))
        # res = result_queue.get()
        # del result_queue
        # return res

    def main_loop(self):
        self.is_main_loop = True
        while self.is_main_loop:
            self.main_loop_func()

    def main_loop_func(self):
        try:
            command, args, result_queue = self.command_queue.get(timeout=1)
            result = command(*args)
            if result_queue:
                result_queue.put(result)
            self.command_queue.task_done()
        except queue.Empty:
            pass

    def stop(self):
        self.is_main_loop = False
        self.main_loop_thread.join()


import asyncio

class BaseAsync(metaclass=LoggerMeta):
    module_type = "async"

    def __init__(self, master):
        self.master = master

    def get_async_loop(self):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        return loop



    def add_task(self, loop, coro) -> asyncio.Task:
        task = loop.create_task(coro)
        return task

    def add_tasks(self, loop, coros) -> list[asyncio.Task]:
        tasks = [self.add_task(loop, coro) for coro in coros]
        return tasks

    def add_task_threadsafe(self, loop, coro) -> asyncio.Future:
        """
        Безопасно добавляет асинхронную задачу (корутину) в event loop из другого потока.
        :param coro: Корутина для выполнения.
        :return: Объект concurrent.futures.Future.
        """
        return asyncio.run_coroutine_threadsafe(coro, loop)

    def add_tasks_threadsafe(self, loop, coros: List[Coroutine]) -> List[asyncio.Future]:
        """
        Безопасно добавляет несколько асинхронных задач (корутин) в event loop из другого потока.
        :param coros: Список корутин для выполнения.
        :return: Список объектов concurrent.futures.Future.
        """
        futures = [self.add_task_threadsafe(loop, coros) for coro in coros]
        return futures

    def add_callback(self, loop, callback, *args):
        """
        Добавляет синхронную функцию (callback) в event loop для немедленного выполнения.
        :param callback: Синхронная функция для выполнения.
        :param args: Аргументы для функции.
        """
        loop.call_soon(callback, *args)

    def add_callback_threadsafe(self, loop, callback, *args):
        """
        Безопасно добавляет синхронную функцию (callback) в event loop из другого потока.
        :param callback: Синхронная функция для выполнения.
        :param args: Аргументы для функции.
        """
        loop.call_soon_threadsafe(callback, *args)

    def add_delayed_callback(self, loop, delay: float, callback, *args):
        """
        Добавляет синхронную функцию (callback) с задержкой выполнения.
        :param delay: Время задержки в секундах.
        :param callback: Синхронная функция для выполнения.
        :param args: Аргументы для функции.
        """
        loop.call_later(delay, callback, *args)

    def add_callback_at(self, loop, when: float, callback, *args):
        """
        Добавляет синхронную функцию (callback) для выполнения в определённое время.
        :param when: Абсолютное время (на основе loop.time()).
        :param callback: Синхронная функция для выполнения.
        :param args: Аргументы для функции.
        """
        loop.call_at(when, callback, *args)






    def run_until_complete(self, loop, coro):
        return loop.run_until_complete(coro)

    def run_forever(self, loop):
        """
        Запускает цикл событий в режиме бесконечного выполнения.
        """
        loop.run_forever()

    async def gather_tasks(self, tasks):
        """
        запуск выполнения списка корутин и возвращает результаты.
        Не поддерживает динамичное добавление задач
        :param tasks: Список корутин для выполнения.
        :return: Список результатов.
        """
        return await asyncio.gather(*tasks)






    async def get_result(self, task):
        """
        Ожидает завершения задачи и возвращает её результат.
        :param task: Объект asyncio.Task.
        :return: Результат задачи.
        """
        await asyncio.wait([task])
        return task.result()

    async def get_results(self, tasks):
        """
        Ожидает завершения всех задач и возвращает их результаты.
        :param tasks: Список объектов asyncio.Task.
        :return: Список результатов задач.
        """
        await asyncio.wait(tasks)
        return [task.result() for task in tasks]

    def get_moment_result(self, task):
        """
        Возвращает результат завершённой задачи.
        :param task: Объект asyncio.Task.
        :return: Результат задачи.
        """
        if task.done():
            return task.result()
        else:
            raise RuntimeError("Задача ещё не завершена")

    def get_moment_results(self, tasks):
        """
        Возвращает результаты завершённых задач.
        :param tasks: Список объектов asyncio.Task.
        :return: Список результатов задач.
        """
        results = []
        for task in tasks:
            if task.done():
                results.append(task.result())
            else:
                raise RuntimeError("Одна или несколько задач ещё не завершены")
        return results


    def cancel_all_tasks(self, loop):
        """
        Отменяет все задачи, связанные с указанным циклом событий.
        """
        if not loop.is_running():
            return

        tasks = [t for t in asyncio.all_tasks(loop) if not t.done()]
        for task in tasks:
            task.cancel()


    def stop_event_loop(self, loop):
        """
        Останавливает цикл событий, если он запущен.
        """
        if loop.is_running():
            loop.call_soon_threadsafe(loop.stop)