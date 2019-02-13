import logging.config

import os
from flask import Flask, Blueprint,request
from com import settings
from com.api.blog.endpoints.team import ns as blog_team_namespace
from com.api.login.endpoints.login import ns as login_namespace
from com.api.restplus import api
from flask_jwt_extended import JWTManager,get_jwt_identity
from datetime import timedelta

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

@app.before_request
def before_request():
    print "cool", request.endpoint
    print "get_jwt_identity",get_jwt_identity()
    pass

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['JWT_SECRET_KEY'] = 'rk007'
    flask_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=86400)


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_team_namespace)
    api.add_namespace(login_namespace)
    flask_app.register_blueprint(blueprint)

    #db.init_app(flask_app)


def main():
    initialize_app(app)
    jwt = JWTManager(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
