:errorNoPython

echo.
echo Error^: Python not installed
echo.
echo.
echo Downloading Python 3.7.0...
IF EXIST "%CD%\python-3.7.0.exe" (
  echo Found Installer at "%CD%\python-3.7.0.exe"
) ELSE (
  powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12, [Net.SecurityProtocolType]::Tls11, [Net.SecurityProtocolType]::Ssl3, [Net.SecurityProtocolType]::Tls; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe' -OutFile '%CD%\python-3.7.0.exe';}"
  echo Python download completed.
)

echo Installing Python...
powershell %CD%\python-3.7.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 TargetDir=c:\Python\Python370
setx path "%PATH%;C:\Python\Python370\"
set "path=%PATH%;C:\Python\Python370\"

echo Python Installation completed.
echo Installing python dependencies.
py -3.7 -m pip install pygame
py -3.7 -m pip install pygame_gui