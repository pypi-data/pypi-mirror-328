
import threading
import time
class FSM:
    def __init__(self, master):
        print("INIT FSM")
        self.master = master
        self.set_state("")

    def set_state(self, state):
        self.state = state

    def execute_command(self, state):
        if not state:              return (True)
        if state == "stop":
            return (False)
        elif state == "threads":
            self.print_active_threads()
        else:
            print("COMMAND NOT EXIST")
        return (True)

    def main_loop(self):
        print("START FSM")
        self.is_main_loop = True
        while self.is_main_loop:
            if not self.execute_command(self.state):
                self.is_main_loop = False
        self.stop_FSM()

    def stop_FSM(self):
        print("STOP FSM")

    def print_active_threads(self):
        threads = threading.enumerate()
        print(f"Active threads ({len(threads)}):")
        for thread in threads:
            print(f"Thread name: {thread.name}, Thread ID: {thread.ident}")
        time.sleep(1)
