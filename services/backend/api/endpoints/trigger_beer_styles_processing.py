# api/endpoints/trigger_beer_styles_processing.py

from fastapi import APIRouter, BackgroundTasks
import subprocess

router = APIRouter()


def run_beer_styles_script():
    subprocess.run(
        ["python", "api/scripts/beer_styles_processing.py"], check=True)


@router.post("/refresh-beer-styles")
async def trigger_script(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_beer_styles_script)
    return {"message": "Script is running in the background"}
