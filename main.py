from flask import Flask, render_template  # request, make_response, redirect,
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.now(timezone.utc))
    # В КНИГЕ БЫЛО НАПИСАНО ТАК, НО ЭТО УСТАРЕВШИЙ ФОРМАТ:
    # return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(_):
    return render_template('500.html'), 500


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
