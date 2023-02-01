# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]
#  * @create date 2023-01-23 16:28:01
#  * @modify date 2023-01-23 16:28:01
#  * @desc [description]
#  */


from . import views
from flask import Blueprint

auth = Blueprint('auth_module', __name__)
