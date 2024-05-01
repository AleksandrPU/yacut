# from flask import jsonify, render_template, Blueprint
# from werkzeug.exceptions import (
# InternalServerError,
# MethodNotAllowed,
# NotFound
# )
#
# from . import db
#
#
# bp = Blueprint('error_handlers', __name__)


# class APIError(Exception):
#
#     def __init__(self, message, status=None):
#         super().__init__()
#         self.message = message
#         if status:
#             self.status_code = status.code
#
#     def to_dict(self):
#         return dict(message=self.message)
#
#
# @bp.errorhandler(APIError)
# def api_error(error):
#     return jsonify(error.to_dict()), error.status_code
#
#
# @bp.errorhandler(MethodNotAllowed)
# def method_not_allowed(error):
#     return jsonify({'message': 'Метод не доступен'}), error.code


# @bp.errorhandler(NotFound)
# def not_found(error):
#     return render_template(
#         'error.html',
#         message='Такой короткой ссылки ещё не создали.',
#         code=error.code,
#     ), error.code
#
#
# @bp.errorhandler(InternalServerError)
# def internal_server_error(error):
#     db.session.rollback()
#     return render_template(
#         'error.html',
#         message='Что-то пошло не так. Попробуйте ещё раз, пожалуйста.',
#         code=error.code,
#     ), error.code
