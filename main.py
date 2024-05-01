from flask import Flask, render_template  # request, make_response, redirect,

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()

# ==== Закомментированный код, который использовался до этого ====

# from flask_script import Manager
# manager = Manager(app)


# @app.route('/')
# def index():
#     return redirect('https://www.youtube.com/')


# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response


# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Ypur browser is %s</p>' % user_agent


# @app.route('/')
# def index():
#     return '<h1>Hello, world!</h1>'


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name
