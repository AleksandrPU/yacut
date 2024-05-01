from http import HTTPStatus

from flask import Blueprint, flash, redirect, render_template, request
from werkzeug.exceptions import InternalServerError, NotFound

from . import db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id

bp = Blueprint('views', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            form.custom_id.data = get_unique_short_id()
        urlmap = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(
            f'{request.url}{form.custom_id.data}',
            'short-link'
        )
    return render_template('short_link.html', form=form)


@bp.route('/<string:custom_id>', methods=['GET'])
def get_original_link_view(custom_id):
    original_link = URLMap.query.filter_by(short=custom_id).first_or_404()
    return redirect(original_link.original, code=HTTPStatus.FOUND)


@bp.errorhandler(NotFound)
def not_found(error):
    return render_template(
        'error.html',
        message='Такой короткой ссылки ещё не создали.',
        code=error.code,
    ), error.code


@bp.errorhandler(InternalServerError)
def internal_server_error(error):
    db.session.rollback()
    return render_template(
        'error.html',
        message='Что-то пошло не так. Попробуйте ещё раз, пожалуйста.',
        code=error.code,
    ), error.code
