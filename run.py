# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]
#  * @create date 2023-01-23 16:29:27
#  * @modify date 2023-01-25 10:53:48
#  * @desc [description]
#  */


import os
import click

from app import create_app, db
from flask_migrate import Migrate
from app.models import Participant, Account

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Participant=Participant, Account=Account)
