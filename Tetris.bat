IF EXIST "%CD%\python-3.7.0.exe" (echo "go launch Tetris !")
ELSE (
  call Installer.bat
del Installer.bat
)
py script/main.py