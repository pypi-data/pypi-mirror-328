import threading
import gc
import time
import atexit
from threading import Timer

class CGC:
    def __init__(self, master):
        self.master = master

    def clear(self):
        self.gc_clear()
        self.timer = Timer(self.cleaning_interval_j, self.clear)
        self.timer.daemon = True
        self.timer.name = "GCTimerCleaningThread"
        self.timer.start()

    def gc_clear(self):
        collected = gc.collect()
        print("CUSTOM GARBAGE COLLECTOR: Память освобожена")

    def on_program_exit(self):
        if hasattr(self, "timer"):
            atexit.register(self.timer.cancel)
            print("CUSTOM GARBAGE COLLECTOR остановлен")

