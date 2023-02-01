# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]  
#  * @create date 2023-01-23 16:27:41
#  * @modify date 2023-01-25 14:56:18
#  * @desc [description]
#  */


from flask import render_template, url_for, redirect, flash, request, session

from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from .forms import LoginForm
from .. import bcrypt
from ..models import Participant, Account


@auth.route('/login', method=['GET', 'POST'])
def login():

    if current_user.is_authenticated:

        next = request.args.get('next')

        if next is None or not next.startswith('/'):

            next = url_for('main_module.index')

        return redirect(next)

    else:
        form = LoginForm()

        if form.validate_on_submit():

            user = Account.query.filter_by(email=form.email.data).first()

            if user is not None and user.verify_password(form.password.data):

                login_user(user, form.remember_me.data)

                next = request.args.get('next')

                if next is None or not next.startswith('/'):

                    next = url_for('main_module.index')

                return redirect(next)

            flash('Usuario e/ou senha inválidos.')

        return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    flash('Você saiu de sua conta.')

    return redirect(url_for('main_module.index'))
