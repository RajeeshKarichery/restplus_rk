import logging

from flask import request,jsonify
from flask_restplus import Resource
from com.api.blog.business import create_team, get_teams
from com.api.blog.serializers import team,team_post
from com.api.restplus import api
from com.api.blog.parsers import parser_team

log = logging.getLogger(__name__)

ns = api.namespace('blog/team', description='Operations related to blog Team')


@ns.route('/')
class TeamCollection(Resource):

    @api.marshal_list_with(team)
    def get(self):
        return get_teams()
        #return jsonify(get_teams())
        #return jsonify({'status': '', 'message': '', 'data': get_teams()})

    @api.response(201, 'Team successfully created.')
    @api.expect(team_post)
    def post(self):
        data = parser_team.parse_args()
        create_team(data)
        return "Saved", 201

