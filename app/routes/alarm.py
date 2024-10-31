from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..models import AlarmCallback
from ..services.alarm_service import save_alarm_data, get_alarm_entries
from pathlib import Path
import json

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent.parent / "templates"))

@router.post("/callback/alarm")
async def callback_alarm(alarm_data: AlarmCallback):
    try:
        message = save_alarm_data(alarm_data)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"写入文件时发生错误: {str(e)}")

@router.get("/view_alarms", response_class=HTMLResponse)
async def view_alarms(request: Request):
    alarm_entries = get_alarm_entries()
    print(f"Number of alarm entries: {len(alarm_entries)}")  # 调试信息
    print(f"First entry: {alarm_entries[0] if alarm_entries else 'No entries'}")  # 调试信息
    return templates.TemplateResponse("view_alarms.html", {"request": request, "alarm_entries": alarm_entries})
