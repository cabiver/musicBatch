@echo off 
if [%1]==[] ( 
set OPTION=aleatorio
) else ( 
set OPTION=%1
)

echo|set /p=%OPTION%|python "%~dp0routes.py"