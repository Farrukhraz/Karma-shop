@ECHO OFF
chdir ..
ECHO dir changed to '%cd%'
ECHO ============================
ECHO Creating mainapp\json folder if it does not exist
if not exist "authapp\json\" mkdir authapp\json
ECHO ============================
ECHO Starting dumping data for 'authapp'
ECHO ----------------------------
ECHO Dumping AuthPageImages table data...
python manage.py dumpdata authapp.AuthPageImages > authapp\json\page_images.json
ECHO Data dumped
ECHO ============================
ECHO Program finished SUCCESSFULLY