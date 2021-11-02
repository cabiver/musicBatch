@echo off 
if [%1]==[] ( 
set OPTION=aleatorio
) else ( 
set OPTION=%1
)

@REM echo %~dp0%OPTION%
echo|set /p=%OPTION%|python "%~dp0routes.py"