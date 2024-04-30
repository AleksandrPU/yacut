from wtforms.validators import ValidationError

from yacut.models import URLMap


def unique_custom_id():
    """Проверка уникальности короткого id."""

    def _unique_custom_id(form, field):
        if URLMap.query.filter_by(short=field.data).first() is not None:
            raise ValidationError(
                'Предложенный вариант короткой ссылки уже существует.'
            )

    return _unique_custom_id
