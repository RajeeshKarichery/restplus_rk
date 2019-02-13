from flask_restplus import Resource
from com.api.login.parsers import parser_login
from com.api.restplus import api
from com.api.login.serializers import login_model
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

ns = api.namespace('login', description='Operations related to Login')

@ns.route('/ulogin')
class LoginCollection(Resource):

    @api.expect(login_model)
    def post(self):
        try:
            data = parser_login.parse_args()
            access_token = create_access_token(identity=data.get('username'))
            return access_token, 200
        except Exception as e:
            return 'Something went wrong', 500

@ns.route('/register')
class RegistrationCollection(Resource):

    @api.expect(login_model)
    def post(self):
        try:
            data = parser_login.parse_args()
            return "registered", 200
        except Exception as e:
            return 'Something went wrong', 500

@ns.route('/dash')
class DashCollection(Resource):

    @jwt_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            print current_user
            return "Dashboard", 200
        except Exception as e:
            return 'Something went wrong', 500

