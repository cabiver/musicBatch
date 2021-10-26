@echo off
if [%1]==[] ( 
set OPTION=joker
) else ( 
set OPTION=%1
)


echo %OPTION%
if [%OPTION%]==[joker] ( 
start chrome.exe "https://www.youtube.com/watch?v=qk0J9b4BEqY&list=RDqk0J9b4BEqY&start_radio=1"
)
if [%OPTION%]==[bayonetta] ( 
start chrome.exe "https://www.youtube.com/watch?v=yckWVQlt8Mo&list=RDyckWVQlt8Mo&start_radio=1"
)
if [%OPTION%]==[dream] ( 
start chrome.exe "https://www.youtube.com/watch?v=SXJGTnVfJic"
)
if [%OPTION%]==[evangelion] ( 
start chrome.exe "https://www.youtube.com/watch?v=6kguaGI7aZg"
)


