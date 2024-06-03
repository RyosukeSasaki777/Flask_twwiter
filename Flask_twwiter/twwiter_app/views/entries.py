from flask import request, redirect, url_for, render_template, flash, session
from twwiter_app import app
from twwiter_app import db
from twwiter_app.models.entries import User_Table
from twwiter_app.models.entries import Post_Table
from twwiter_app.models.entries import Comm_Table


# ルート
@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    posts = Post_Table.query.filter(Post_Table.community_id == None)
    # user = User_Table.query.filter(User_Table.id == posts['user_id'])
    # print(posts[0].user_id)
    for post in posts:
        post_datas = db.session.query(Post_Table, User_Table).join(Post_Table, Post_Table.user_id == User_Table.id)
        
    # print(post_datas[0].User_Table.name)

    return render_template('entries/index.html', post_datas=post_datas, id=session['user_id'])

# 投稿の編集画面へ遷移
@app.route('/edit_entry/<id>')
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    post = Post_Table.query.get(id)
    return render_template('entries/edit.html', post=post)

# 投稿のアップデート
@app.route('/update_post/<id>', methods=['POST'])
def update_post(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    print(id)
    post_edited = Post_Table.query.get(id)
    post_edited.title = request.form['title']
    post_edited.text = request.form['text']
    # Post_Table.image_url = request.form['image_url']
    db.session.merge(post_edited)
    db.session.commit()
    flash('記事タイトル「' + post_edited.title + '」の更新が完了しました')
    return redirect(url_for('show_entries'))

# 投稿の新規作成画面へ遷移
@app.route('/new_entry')
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    communities = Comm_Table.query.filter(Comm_Table.user_id == session['user_id'])
    return render_template('entries/new.html', communities=communities)

# 投稿の新規作成とDBへの登録
@app.route('/new_post', methods=['POST'])
def new_post():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if (request.form['community_id']==""):
        comm_id = None
    else:
        comm_id = request.form['community_id']
    newPost = Post_Table(
        user_id = session['user_id'],
        community_id = comm_id,
        title = request.form['title'],
        text = request.form['text']
        # image_url = ???  ここに画像のフォームからurlを受け取る
    )
    db.session.add(newPost)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))