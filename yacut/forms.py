from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
    Regexp,
    URL,
    ValidationError,
)

from yacut.models import URLMap


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
        ],
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if URLMap.query.filter_by(short=field.data).first() is not None:
            raise ValidationError(
                'Предложенный вариант короткой ссылки уже существует.'
            )
