from flask_wtf import FlaskForm
from wtforms import StringField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='"url" является обязательным полем!')],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16,
                   message='Указано недопустимое имя для короткой ссылки'),
            Regexp(r'[a-zA-Z0-9]+',
                   message='Указано недопустимое имя для короткой ссылки'),
            Optional()
        ],
    )
