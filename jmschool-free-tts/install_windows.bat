@echo off
chcp 65001 >nul
cd /d "%~dp0"
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo 설치에 실패했습니다. Python과 인터넷 연결을 확인하세요.
  pause
  exit /b 1
)
echo.
echo 설치 완료. Codex에서 이 스킬을 사용하세요.
pause
