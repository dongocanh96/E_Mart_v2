# E_Mart
An e-commerce web's built using Flask under the microservice architecture
## How to run:
1. create a virtualenv environment
2. Activate environment then run `python3 -m pip install -r requirements.txt`
3. Run project, first you need to initialize db
- `export FLASK_APP=emart.py`
- `export FLASK_ENV=development`
- `flask db init`
- `flask db migrate`
- `flask db upgrade`
- `flask run`
