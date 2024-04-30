from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from yacut.validators import unique_custom_id


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='"url" является обязательным полем!'),
            URL(
                require_tld=True,
                message='Введенное выражение не является ссылкой',
            ),
        ],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                min=1,
                max=16,
                message='Указано недопустимое имя для короткой ссылки'
            ),
            Regexp(
                r'^[a-zA-Z0-9]+$',
                message='Указано недопустимое имя для короткой ссылки'
            ),
            Optional(),
            unique_custom_id(),
        ],
    )
    submit = SubmitField('Создать')
