# from typing import Optional
import subprocess
import asyncio
import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from api.models import Process

class ProcessManager:
    processes = {}
    run = []
    async def start_process(self, process: Process):
        if process.name not in self.processes:
            try:
                # await asyncio.create_subprocess_shell(process.name, stdout=asyncio.subprocess.PIPE,
                #                                                 stderr=asyncio.subprocess.PIPE)
                subprocess.run(process.name, shell=True, check=True, capture_output=True, text=True)
                self.processes.append([process.name])
                return True

            except subprocess.CalledProcessError:
                print("Command failed to execute.")
            except Exception as e:
                print("An error occurred: ", e)
            return True
        else:
            return False

    async def stop_process(self, process: Process):
        if process.name in self.processes:
            try:
                pid_list = subprocess.check_output(["pidof", process.name])
                pids = [int(pid) for pid in pid_list.decode().split()]
                for pid in pids:
                    subprocess.check_call(["kill", str(pid)])

                print(f"Command '{process.name}' terminated successfully.")
                self.processes[process.name] = False

            except subprocess.CalledProcessError as e:
                print(f"Error terminating command '{process.name}': {e}")
            except Exception as e:
                print("An error occurred: ", e)
            return True
        else:
            return False