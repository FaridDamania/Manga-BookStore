# bookstore
# Installation

## 1.First you need to create a virtual environment 
In windows the commands are below
py -3 -m venv venv
cd venv
pip install -r requirements.txt  (The requirements for this project will be installed)

## 2.Project Setup 
cd bookstore 
python manage.py migrate (this will migrate everythings)
Now create superuser (python manage.py createsuperuser) and add some books to it
