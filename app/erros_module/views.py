# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:26:58
#  * @modify date 2023-01-23 16:26:58
#  * @desc [description]
#  */

from flask import render_template

from . import error


@error.app_errorhandler(404)
def page_not_found(error):

    return '<h1>Página de erro</h1>', 404


@error.app_errorhandler(500)
def internal_server_error(error):

    return '<h1>Erro de servidor</h1>', 500
