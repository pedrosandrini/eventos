# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:25:22
#  * @modify date 2023-01-23 16:25:22
#  * @desc [description]
#  */

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():

    # Chave para criar criptografia de formularios
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'e7ccc94e3632cd3dc1eb8f7d95dd9056316709d4'

    # SMTP
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.google.com')

    # Porta SMTP
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))

    #
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in [
        'true', 'on', '1']

    # Usuario SMTP
    MAIL_USER = os.environ.get('MAIL_USER')

    # Senha SMTP
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    SYSTEM_MAIL_SUBJECT_PREFIX = '[Eventos]'

    # Email do remetente
    MAIL_SENDER = f"Eventos <{os.environ.get('MAIL_SENDER')}>"

    SYSTEM_ADMIN = os.environ.get('SYSTEM_ADMIN')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevConfig,
    'production': ProductionConfig,

    'default': DevConfig
}
