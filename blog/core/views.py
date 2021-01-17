from flask import render_temlate, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_temlate('index.html')


@core.route('/info')
def info():
    return render_temlate('info.html')
