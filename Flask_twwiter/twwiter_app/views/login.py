from flask import request, redirect, url_for, render_template, flash, session
from twwiter_app import app
from twwiter_app.models.entries import User_Table

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User_Table.query.filter(User_Table.name == request.form['username']).first()
        if not user:
            flash('登録されていないユーザー名です。')
        else:
            session['logged_in'] = True
            session['user_id'] = user.id
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('entries/login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))