cd ../
".venv/Scripts/pyinstaller.exe" --noconfirm --onefile --windowed --icon "favicon.ico" --name "anime-player-portable" --add-data "shaders;shaders/" --add-data "favicon.ico;." --add-data "libmpv-2.dll;." --add-data "docs/GLSL_Instructions_Advanced.txt;docs/" --add-data "docs/GLSL_Instructions_Advanced_ru.txt;docs/" --add-data "images/play-button.png;images/" --add-data "images/anime-player-icon.png;images/" --add-data "images/icons/;images/icons/" "main.py"