title FlaskDev
call workon flask
d:
cd /d %~dp0
dir
set FLASK_APP=%1
echo %FLASK_APP%
CMD