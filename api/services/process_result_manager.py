import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from typing import Dict
from api.models import Process
import subprocess
import asyncio


class ProcessResultManager:
    results = {}

    def is_process_running(self, process: Process):
        running_processes = subprocess.run(['ps', '-ax'], capture_output=True).stdout.decode('utf-8')
        if process.name in running_processes:
            return True
        return False
    async def add_result(self, process: Process, result: Dict):
        try:
            running = await asyncio.create_subprocess_shell(process.name, stdout=asyncio.subprocess.PIPE,
                                                        stderr=asyncio.subprocess.PIPE)
            while True:
                output = await running.stdout.readline()
                print(output.decode().strip())
                if not output:
                    break
        except subprocess.CalledProcessError:
            print("Command failed to execute.")
        except Exception as e:
            print("An error occurred: ", e)
        self.results[process.name] = result

    async def get_last_result(self, process: Process):
        if process.name in self.results:
            return self.results[process.name]
        else:
            return None