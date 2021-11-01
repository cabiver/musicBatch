@echo off 
if [%1]==[] ( 
set OPTION=persona
) else ( 
set OPTION=%1
)
echo|set /p=%OPTION%|python routes.py