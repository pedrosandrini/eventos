# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:26:28
#  * @modify date 2023-01-23 16:26:28
#  * @desc [description]
#  */


from flask import render_template, redirect, request, url_for, current_app

from . import main
from .. import db


@main.route('/')
def index():
    return '<h1>Página index</h1>'
