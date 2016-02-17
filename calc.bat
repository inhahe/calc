@echo off
if "%1"=="" goto calc
d:\python27\python d:\utils\calc.py %*
goto end
:calc
calc.exe
:end
