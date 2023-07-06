from flask import Blueprint


themegeoportalkgt = Blueprint(
    "themegeoportalkgt", __name__)


def page():
    return "Hello, themegeoportalkgt!"


themegeoportalkgt.add_url_rule(
    "/themegeoportalkgt/page", view_func=page)


def get_blueprints():
    return [themegeoportalkgt]
