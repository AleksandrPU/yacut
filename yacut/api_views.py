from http import HTTPStatus

from flask import jsonify, request
from werkzeug.exceptions import BadRequest, NotFound

from yacut import app, db
from yacut.error_handlers import APIError
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if data is None:
        raise APIError(
            'Отсутствует тело запроса', BadRequest
        )

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


@app.route('/api/id/<string:short_id>/')
def get_original_link(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first()
    if original_link is None:
        raise APIError('Указанный id не найден', NotFound)
    return jsonify({'url': original_link.original}), HTTPStatus.OK
