import sys
sys.path.append('/home/riverhals/Documents/Kasper/infohub/')
from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

router = APIRouter()

@router.get("/api/docs")
async def documentation():
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="API Documentation")

@router.get("/api/openapi.json")
async def openapi():
    return get_openapi(title="API Documentation", version=1.0, routers=api.routers)
