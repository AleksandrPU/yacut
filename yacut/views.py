from flask import abort, flash, redirect, render_template, request

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
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


@app.route('/<string:custom_id>/', methods=['GET'])
def get_original_view(custom_id):
    original_link = URLMap.query.filter_by(short=custom_id).first()
    if original_link is None:
        abort(404)
    return redirect(original_link.original)
