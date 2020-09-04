@echo Enter "1" to create a data file
@echo Enter "2" to run the song fetching script
@echo off
set /p opt="Option: "

IF /i "%opt%"=="1" goto opt1
IF /i "%opt%"=="2" goto opt2

echo Wrong option.
goto commonexit

:opt1
echo Running getData.py...
python getData.py
goto commonexit

:opt2
echo Running openSongs.py...
python openSongs.py
goto commonexit

:commonexit
pause