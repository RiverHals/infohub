import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from fastapi import APIRouter, HTTPException
from api.models import Process
from api.services.process_result_manager import ProcessResultManager

router = APIRouter()
process_result_manager = ProcessResultManager()

@router.get("/api/pn/result")
async def get_process_result(process: Process):
    result = process_result_manager.get_last_result(process)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="The process has not started yet")