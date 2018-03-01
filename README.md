# Chain Gwin (Team 7 project for Uni Hack Challenge 3)

make sure `python` 3 and `pip` are installed.

Inside project root directory,
to install require python packages
```
pip install -r requirements.txt
```
create and migrate database for django
```
python manage.py migrate
```
create dummy data
(this will create user 'Jack Ma' with password '1234qwer', kudo address '1MZ36MjvZSpGPsq7nKbCPoGDWrrD2wPvyoT2DC' and dummy items to be sold by him)
```
python manage.py shell < dummy_data.py
```
finally run server and you can access Chain Gwin on localhost
```
python manage.py runserver
```
