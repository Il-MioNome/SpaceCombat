@echo off
echo Downloading Python...

curl -o python_installer.exe https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe

echo Start Python installer... Check "Add python to PATH" and leave "pip" enabled
python_installer.exe