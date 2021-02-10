:: --- Diese Daeti ist für den Bot zu starten --
::  ---   Einfach ausführen mit cmd    ---
::          Made by Kuso der echte

@echo off
@cls

@where python.exe || cls && echo Python muss installiert sein um den Bot zu starten! && exit
@cls

:: den momentanen Pfad in die "Path" Variable setzen
FOR /F "tokens=*" %%g IN ('cd') do (SET path=%%g)
FOR /F "tokens=*" %%g IN ('where python.exe') do (SET pythonPath=%%g)
@cls

@cd path
@cls

echo Bot wird gestartet...

%pythonPath% """%path%\index.py"""