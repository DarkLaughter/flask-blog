from blog.core.views import core
from flask import Flask

app = Flask(__name__)

app.register_blueprint(core)
