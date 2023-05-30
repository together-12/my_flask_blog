import datetime
import traceback

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.errorhandler(500)
def handle_500_error(exception):
    trace = traceback.format_exc()
    return f"Error: {trace}", 500
# 用于存储帖子信息的列表
posts = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # 进行登录验证
    return redirect(url_for('forum'))

@app.route('/forum')
def forum():
    return render_template('forum.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # 处理发帖请求
        username = request.form['username']
        title = request.form['title']
        content = request.form['content']
        # 获取当前系统时间并格式化
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 添加新帖子到列表中
        posts.append({
            'title': title,
            'author': username,
            'content': content,
            'time': time
        })
        # 重定向到论坛页面
        return redirect(url_for('forum'))
    else:
        return render_template('post.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
        post = posts[post_id]
        return render_template('show_post.html', post=post)
    else:
        return "Post not found"

if __name__ == '__main__':
    app.run()
