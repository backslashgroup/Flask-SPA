# Flask-SPA

Flask-SPA is a minimal Single-Page Applications (SPA) boilerplate with API

## Getting Started

clone the repository

```bash
git clone https://github.com/
```

## Installation

Create a virtual environment and activate it (can be any of your choices e.g. virtualenv or venv )

```bash
python -m venv venv
. venv/bin/activate
```

Or on Windows cmd

```bash
py -3 -m venv venv
venv\Scripts\activate.bat
```
Install other dependencies

```bash
cd flask-SPA
pip install -r requirements.txt
```

Flask installation guide:
https://flask.palletsprojects.com/en/1.1.x/installation/#installation

Production Deployment:
https://flask.palletsprojects.com/en/1.1.x/deploying/
https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/


## Run

```bash
export FLASK_APP=main
flask run
```

Or on Windows cmd

```bash
set FLASK_APP=main
flask run
```

Open http://127.0.0.1:5000 in a browser.


## Test

```bash
pytest
```

## License
[MIT](https://choosealicense.com/licenses/mit/)


## Theme
[Grayscale](https://startbootstrap.com/theme/grayscale)
A free, multipurpose, one page Bootstrap theme featuring a dark color scheme and smooth scrolling animations
