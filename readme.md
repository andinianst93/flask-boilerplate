
```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```


## To run the CSS:

```
npx tailwindcss -i ./app/static/css/input.css -o ./app/static/css/dist/output.css --watch
```


## To run the app:

MAC OS:

```
export FLASK_APP=manage.py
```

# DB migrations

```
flask db init
```

```
flask db migrate
```

```
flask db upgrade
```