@echo off
REM Configuración temporal de PATH para Git portátil
setlocal enabledelayedexpansion
set PATH=%TEMP%\PortableGit\bin;%PATH%
cd /d C:\Users\shpctac1003e\Desktop\30-archivos
git %*
