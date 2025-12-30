@echo off
python "%~dp0puff.py" %*

REM Check if there was an error
if errorlevel 1 (
    echo.
    echo [ERROR] Program exited with errors
)

REM Always pause at the end so window doesn't close
echo.
echo =====================================
echo Program finished. Press any key to exit...
pause > nul