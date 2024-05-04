from http import HTTPStatus

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import (
    BadRequest,
    MethodNotAllowed,
    NotFound,
    UnsupportedMediaType
)

from . import db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id

bp = Blueprint('api', __name__, url_prefix='/api')


class APIError(Exception):

    def __init__(self, message, status=None):
        super().__init__()
        self.message = message
        if status:
            self.status_code = status.code

    def to_dict(self):
        return dict(message=self.message)


@bp.route('/id/', methods=('POST',))
def create_short_link():
    data = request.get_json()

    form = URLMapForm()
    form.original_link.data = data.get('url', None)
    form.custom_id.data = data.get('custom_id', None)
    if not form.custom_id.data:
        form.custom_id.data = get_unique_short_id()
    form.validate()

    if form.original_link.errors:
        raise APIError(form.original_link.errors[0], BadRequest)
    if form.custom_id.errors:
        raise APIError(form.custom_id.errors[0], BadRequest)

    urlmap = URLMap()
    urlmap.from_dict(
        {
            'original': form.original_link.data,
            'short': form.custom_id.data,
        }
    )
    db.session.add(urlmap)
    db.session.commit()

    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED


@bp.route('/id/<string:short_id>/', methods=('GET',))
def get_original_link(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first()
    if original_link is None:
        raise APIError('Указанный id не найден', NotFound)
    return jsonify({'url': original_link.original}), HTTPStatus.OK


@bp.errorhandler(APIError)
def api_error(error):
    return jsonify(error.to_dict()), error.status_code


@bp.app_errorhandler(MethodNotAllowed)
@bp.errorhandler(UnsupportedMediaType)
def api_error_handler(error):
    match error.code:
        case 405:
            message = 'Метод не доступен'
            code = error.code
        case 415:
            message = 'Отсутствует тело запроса'
            code = 400
        case _:
            message = 'Неизвестная ошибка'
            code = 500
    return jsonify({'message': message}), code
