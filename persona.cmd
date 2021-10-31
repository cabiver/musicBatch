@echo off
if [%1]==[] ( 
set OPTION=nada
) else ( 
set OPTION=%1
)


echo opcion: %OPTION%
	
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
if [%OPTION%]==[caleb] ( 

	if [%2]==[] (
	start chrome.exe "https://www.youtube.com/watch?v=gcipipADLnw&list=RDMMyckWVQlt8Mo&index=2"
	)
	if [%2]==["face in fears"] ( 
	start chrome.exe "https://www.youtube.com/watch?v=doWygi9e5L8"
	)
)

if [%OPTION%]==[giveHearts] ( 

	if [%2]==[] (
	start chrome.exe "https://www.youtube.com/watch?v=wgNqW2gEDiY"
	)
	if [%2]==["addic"] ( 
	start chrome.exe "https://www.youtube.com/watch?v=RMTg5SA2c3o&list=RDMMyckWVQlt8Mo&index=5"
	)
)

if [%OPTION%]==[nada] ( 
echo joker
echo bayonetta
echo dream
echo evangelion
echo caleb
echo giveHearts
)
