from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__ )

@bp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(f'Username: {login_form.username}\Password: {login_form.password}')
        flash(f'Successfully logged in. Hello! {login_form.username.data}', 'success')
        return redirect(url_for('main.index'))

    return render_template('user.html', form=login_form,  heading='Login')

@bp.route('/register', methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        flash(f'Successfully created the account {register_form.username.data}', 'success')
        print()
        return redirect(url_for('auth.login'))

    return render_template('user.html', form=register_form,  heading='Register')

@bp.route('/logout')
def logout():
    print('logout')
    return redirect(url_for('main.index'))