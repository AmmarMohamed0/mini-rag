from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    #  when a request is made to the route associated with the welcome function, 
    # FastAPI will automatically call the get_settings function to resolve the app_settings 
    # dependency and pass the result to the welcome function for further processing.
    
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
   
    return {
        'app_name': app_name,
        'app_version': app_version
        }