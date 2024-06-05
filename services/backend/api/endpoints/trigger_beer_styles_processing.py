# api/endpoints/trigger_beer_styles_processing.py

from fastapi import APIRouter, BackgroundTasks
from api.scripts.beer_styles_processing import scrape_and_process_beer_styles

router = APIRouter()


def run_beer_styles_script():
    scrape_and_process_beer_styles()


@router.post("/refresh-beer-styles")
async def trigger_script(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_beer_styles_script)
    return {"message": "Script is running in the background"}
