from flask import Flask
from flask import render_template
from flask import send_from_directory


def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return render_template('/index.html')
    return app
app = create_app()
