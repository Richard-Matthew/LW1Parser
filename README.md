# Long War 1.0 Save Game Parser (LW1Parser)
Converts Long War 1.0 save binaries into JSON with [xcom2save](https://github.com/tracktwo/xcomsave) and then to a .csv file and/or entries in a SQLite database with an optional GUI.

# Basic Usage
For Windows:
1. Download the zip file from the latest release.
2. Extract the contents of the zip file.
3. Download the [1.8.2 release of xcomsave](https://github.com/tracktwo/xcomsave/releases/tag/1.8.2) and move xcom2json.exe into the folder created by extracting the zip file.
4. Open config.ini with a text editor and change the entries under FILE PATHS to their respective folders for your system.
5. Run LW1Parser.exe.
6. Click Update to automatically parse the most recent savegame to csv or Convert to choose which file to parse.

Other OS:
1. Build the project (a build.bat using PyInstaller is included but has not been tested for non-Windows systems)

# Button Information
Update:
- Searches for the most recently modified file in strSaveFolder matching the name save*.
- Converts to JSON with xcom2json.
- Either inserts unit information into an SQLite database or directly exports to csv based on config.ini settings.

Convert:
- Opens a file dialog to select a save file to convert.
- Opens a file dialog for saving the resulting csv.

Export:
- Enabled when bUseDatabase is True.
- Queries the database for the most recent update.
- Saves the queried unit information to csv.

# Requirements
Windows:
- Windows 10+
- Some version of Microsoft Visual C++ Redistributable

Compiling:
- Python 3.11+
- Plus a version of xcom2json that works on your system