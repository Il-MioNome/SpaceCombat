@echo off
cd /d %~dp0

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Installation complete. Now you can open "main.py" for open the game
pause