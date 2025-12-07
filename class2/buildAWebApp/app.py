from flask import Flask, render_template_string
from datetime import datetime


app = Flask(__name__)


FAVORITE_MOVIES = [
"The Matrix",
"Spirited Away",
"Inception",
]


TEMPLATE = """
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>Assignment 1 - Hello</title>
</head>
<body>
<h1>Hello — {{ name }}</h1>
<p>Current date & time: {{ now }}</p>
<h2>Favorite movies</h2>
<ul>
{% for m in movies %}
<li>{{ m }}</li>
{% endfor %}
</ul>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(TEMPLATE, name="Rajiv Ramadoss", now=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), movies=FAVORITE_MOVIES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
