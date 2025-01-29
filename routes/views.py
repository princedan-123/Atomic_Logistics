"""A blueprint for all view pages."""
from flask import Blueprint, render_template

views_blueprint = Blueprint('views_blueprint', __name__, template_folder='../templates')

@views_blueprint.route('/', methods=['GET'], strict_slashes=False)
def index():
    """An implementation of the index page."""
    return render_template('index.html')