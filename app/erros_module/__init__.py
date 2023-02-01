# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:27:08
#  * @modify date 2023-01-23 16:27:08
#  * @desc [description]
#  */

from flask import Blueprint

error = Blueprint('errors_module', __name__)

from . import views
