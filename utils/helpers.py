import pathlib
from datetime import datetime

def screenshot_path(name: str) -> str:
    out_dir = pathlib.Path("reports")/"screenshots"
    out_dir.mkdir(parents=True, exiss_ok=True)
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return f"{out_dir}/¨{timestamp}_{name}.png"