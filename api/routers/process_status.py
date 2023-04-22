import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from fastapi import APIRouter
from api.models import Process
from api.services.process_manager import ProcessManager

router = APIRouter()
process_manager = ProcessManager()

@router.get("/api/pn")
async def get_process_status(process: Process):
    try:
        Process(**process.dict())
    except ValueError as e:
        raise HTTPException(status_code=422, detail="Validation error: {}".format(str(e)))

    is_running = process_manager.processes.get(process.name, False)
    if is_running:
        return {"status": "running"}
    else:
        return RedirectResponse("/api/pn/")
