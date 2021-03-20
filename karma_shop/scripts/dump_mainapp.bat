@ECHO OFF
chdir ..
ECHO dir changed to '%cd%'
ECHO ============================
ECHO Creating mainapp\json folder if it does not exist
if not exist "mainapp\json\" mkdir mainapp\json
ECHO ============================
ECHO Starting dumping data for 'mainapp'
ECHO ----------------------------
ECHO Dumping ProductCategory table data...
python manage.py dumpdata mainapp.ProductCategory > mainapp\json\categories.json
ECHO Data dumped
ECHO ----------------------------
ECHO Dumping ProductBrand table data...
python manage.py dumpdata mainapp.ProductBrand > mainapp\json\brands.json
ECHO Data dumped
ECHO ----------------------------
ECHO Dumping Product table data...
python manage.py dumpdata mainapp.Product > mainapp\json\products.json
ECHO Data dumped
ECHO ----------------------------
ECHO Dumping HotOffers table data...
python manage.py dumpdata mainapp.HotOffers > mainapp\json\hot_offers.json
ECHO Data dumped
ECHO ----------------------------
ECHO Dumping DealsOfTheWeek table data...
python manage.py dumpdata mainapp.DealsOfTheWeek > mainapp\json\deals_of_the_week.json
ECHO Data dumped
ECHO Program finished SUCCESSFULLY