# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:26:44
#  * @modify date 2023-01-23 16:26:44
#  * @desc [description]
#  */


from flask import Blueprint

main = Blueprint('main_module', __name__)

from . import views
