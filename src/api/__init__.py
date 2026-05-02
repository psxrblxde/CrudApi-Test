from fastapi import APIRouter
from src.api.HttpEndpoint import router as base_router

main_router = APIRouter()
main_router.include_router(base_router)