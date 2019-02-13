from flask_restplus import fields
from com.api.restplus import api

login_model = api.model('login_model',{"username":fields.String(required=True, description='Username content')})