import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from typing import Dict
from api.models import Process

class ProcessResultManager:
    results = {}

    def add_result(self, process: Process, result: Dict):
        self.results[process.name] = result

    def get_last_result(self, process: Process):
        if process.name in self.results:
            return self.results[process.name]
        else:
            return None