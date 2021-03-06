"""Using Flask template engines.

In this example we're using Flask template engine (Jinja2) to simplify
the process to generate the resulting HTML.

**TODO**
In our previous example we had to do a lot of string handling to
create the <ul> with authors.
It's your turn to use the template engine to build the same result.
"""
from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Hemil"
    html = """
        <html>
            <h1>Welcome to {{library_name}} library!</h1>
            # Using an <ul> tag add the authors using the template engine
            <ul>
                {% for each in authors %}
                <li> {{ each }}</li>
                {% endfor %}
            </ul>
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges","Hemil"]
    rendered_html = render_template_string(html, library_name=library_name,authors = authors)
    
    
    return rendered_html
