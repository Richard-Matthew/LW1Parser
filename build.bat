@echo off
echo ================================
echo   Building LW1Parser Portable
echo ================================

REM Clean previous build artifacts
echo Cleaning old build folders...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul

REM Build in onedir mode (creates _internal folder)
echo Running PyInstaller...

pyinstaller --windowed --name LW1Parser --icon=icon.ico ^
    --paths src ^
    --add-data "src/lw1parser/resources;lw1parser/resources" ^
    --hidden-import openpyxl ^
    launcher.py

REM Copy external resources into the dist folder
echo Copying config.ini...
copy config.ini dist\LW1Parser\ >nul

echo ================================
echo   Build complete!
echo   Output folder: dist\LW1Parser
echo ================================
pause
