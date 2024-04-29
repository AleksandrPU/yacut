from flask import render_template
from werkzeug.exceptions import InternalServerError, NotFound

from yacut import app


@app.errorhandler(NotFound)
def not_found(error):
    message = 'Такой короткой ссылки ещё не создали.'
    return render_template(
        'error.html', message=message, code=error.code,
    ), error.code


@app.errorhandler(InternalServerError)
def internal_server_error(error):
    message = 'Что-то пошло не так. Попробуйте ещё раз, пожалуйста.'
    return render_template(
        'error.html', message=message, code=error.code,
    ), error.code
