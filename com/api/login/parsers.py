from flask_restplus import reqparse

parser_login = reqparse.RequestParser()
parser_login.add_argument('username', help='User Name cannot be blank', required=True)
