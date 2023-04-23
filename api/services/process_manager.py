import sys
sys.path.append(".")
import asyncio
import subprocess
from typing import Dict
from api.models import Process


async def run_command(command):
    proc = await asyncio.create_subprocess_shell(command,
                                                 stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return proc.returncode, stdout, stderr


class ProcessManager:
    processes: Dict[str, asyncio.Task] = []

    async def start_process(self, process: Process):
        if process.name in self.processes:
            print(f"Process '{process.name}' is already running")
            return False

        try:
            task = asyncio.create_task(run_command(process.name))
            self.processes[process.name] = task
            print(f"Process '{process.name}' started")
            return True
        except Exception as e:
            print(f"An error occurred while starting the process: {e}")
            return False

    async def stop_process(self, process: Process):
        if process.name not in self.processes:
            print(f"Process '{process.name}' is not currently running")
            return False

        try:
            process_tasks = [task for name, task in self.processes.items() if name == process.name]
            pid_list = []
            for task in process_tasks:
                command = task.get_name()
                proc = task.get_coro().cr_frame.f_locals['proc']
                await proc.wait()
                pid_list += subprocess.check_output(["pidof", command]).decode().split()
                task.cancel()

            for pid in pid_list:
                subprocess.run(["kill", pid], check=False)
                print(f"Process '{process.name}' stopped")
            del self.processes[process.name]
            return True

        except subprocess.CalledProcessError as e:
            print(f"Error terminating process '{process.name}': {e}")
            return False

        except Exception as e:
            print(f"An error occurred while stopping the process: {e}")
            return False

# Check if the process is running
def is_process_running(process_name):
    running_processes = subprocess.run(['ps', '-ax'], capture_output=True).stdout.decode('utf-8')
    if process_name in running_processes:
        return True
    return False


manager = ProcessManager()

# Call these functions as per your requirements
async def start_or_print_running(process):
    if is_process_running(process):
        print(f"Process '{process}' is already running")
        return
    await manager.start_process(process)

async def stop_or_print_not_running(process):
    if not is_process_running(process):
        print(f"Process '{process}' is not currently running")
        return
    await manager.stop_process(process)