from blog.core.views import core
from blog.error_pages.handlers import error_pages
from flask import Flask

app = Flask(__name__)

app.register_blueprint(core)
app.register_blueprint(error_pages)
