from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/logs")
async def get_logs():
    try:
        # Read log content from file

        with open("logs.log", "r") as file:
            log_content = file.read()
        # Return log content as JSON response

        return JSONResponse(content={"log_content": log_content})
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to read log file: {e}"
        )
