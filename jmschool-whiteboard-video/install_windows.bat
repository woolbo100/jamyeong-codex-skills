@echo off
cd /d "%~dp0"
echo Installing JMSCHOOL Whiteboard Video Skill dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
  echo.
  echo Installation failed. Make sure Python is installed and added to PATH.
  pause
  exit /b %errorlevel%
)
echo.
echo Installation complete.
echo You can now ask Codex to create a whiteboard video using this skill.
pause
