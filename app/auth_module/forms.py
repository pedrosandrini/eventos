# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:27:51
#  * @modify date 2023-01-23 16:27:51
#  * @desc [description]
#  */


from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, length


class LoginForm(FlaskForm):

    email = EmailField('E-mail', validators=[DataRequired(), Email()])

    password = PasswordField('Senha', validators=[
                             DataRequired(), length(min=8)])

    remember_me = BooleanField('Mantenha-me conectado.', validators=[])

    submit = SubmitField('Entrar')
