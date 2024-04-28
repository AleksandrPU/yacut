from flask import redirect

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['POST'])
def get_short_link():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.text
        if URLMap.query.filter_by(custom_id=custom_id).first() is not None:
            return 'Предложенный вариант короткой ссылки уже существует.'
        if custom_id is None:
            custom_id = get_unique_short_id()
        urlmap = URLMap(
            original=form.original_link.text,
            short=custom_id,
        )
        db.session.add(urlmap)
        db.session.commit()
        return custom_id
    return 'Error get_short_link'


@app.route('/<string:custom_id>/', methods=['GET'])
def get_original_link(custom_id):
    original_link = URLMap.query.get_or_404(custom_id=custom_id)
    return redirect(original_link)
