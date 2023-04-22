from typing import Optional
import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from api.models import Process

class ProcessManager:
    processes = {}

    def start_process(self, process: Process):
        if process.name not in self.processes:
            self.processes[process.name] = True
            return True
        else:
            return False

    def stop_process(self, process: Process):
        if process.name in self.processes:
            self.processes[process.name] = False
            return True
        else:
            return False