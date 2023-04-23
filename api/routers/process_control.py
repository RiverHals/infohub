import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')

import asyncio

# sys.path.append( '/.../infohub/api/services' )
# sys.path.append( '/.../infohub/api/' )
from fastapi import APIRouter, HTTPException
from api.models import Process
from api.services.process_manager import ProcessManager

router = APIRouter()
process_manager = ProcessManager()

@router.post("/api/pn/start")
async def start_process(process: Process):
    status = await process_manager.start_process(process)
    if status:
        return {"message": "The process has started successfully"}
    else:
        raise HTTPException(status_code=400, detail="The process is already running")
@router.post("/api/pn/stop")
async def stop_process(process: Process):
    status = process_manager.stop_process(process)
    if status:
        return {"message": "The process has stopped successfully"}
    else:
        raise HTTPException(status_code=400, detail="The process is not currently running")