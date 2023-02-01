# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]
#  * @create date 2023-01-23 16:24:05
#  * @modify date 2023-01-23 16:24:05
#  * @desc [description]
#  */

from config import config


from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Você deve estar logado para realizar esta ação.'
login_manager.login_message_category = 'alert-warning'


def create_app(config_mode):

    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    config[config_mode].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    return app
