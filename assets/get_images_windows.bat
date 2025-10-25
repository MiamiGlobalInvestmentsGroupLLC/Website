@echo off
where python >nul 2>nul
if %errorlevel% neq 0 (
  echo Please install Python 3, then re-run this.
  pause
  exit /b
)
python -m pip install pillow
python fetch_images.py
echo Done. Images saved to assets\images\
pause
