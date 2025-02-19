import threading
import time
from pprint import pprint

import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

class Menu:
    def __init__(self, master):
        print("INIT MENU")
        self.master = master

    def execute_command(self, command):
        if not command:              return (True)
        if command == "stop":
            return (False)
        elif command == "threads":
            self.print_active_threads()
        elif command == "print_path_tree":
            self.print__path_tree()
        elif command == "print_init_config":
            self.print_init_config()
        else:
            print("COMMAND NOT EXIST")
        return (True)

    def main_loop(self):
        print("START MENU")
        self.is_main_loop = True
        while self.is_main_loop:
            command = self.input_with_timeout()  # (input() or self.event.wait())
            # print("command = ", command)

            if not self.execute_command(command):
                self.is_main_loop = False
            time.sleep(1)
        self.stop_menu()

    def stop_menu(self):
        print("STOP MENU")

    def input_with_timeout(self, timeout=1.0):
        line = sys.stdin.readline()
        if line:
            return line.strip()
        else:
            time.sleep(timeout)
            return False

    def print_init_config(self):
        self.paths.print_init_config()

    def print__path_tree(self):
        self.paths.print_base_path_tree()

    def print_active_threads(self):
        threads = threading.enumerate()
        print(f"Active threads ({len(threads)}):")
        for thread in threads:
            print(f"Thread name: {thread.name}, Thread ID: {thread.ident}")
