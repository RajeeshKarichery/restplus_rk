from flask_restplus import fields
from com.api.restplus import api
from datetime import datetime as rk


class DateFormat(fields.Raw):
    def format(self, value):
        return rk.strftime(value, '%d-%m-%Y')


blog_post = api.model('Blog post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(blog_post))
})

team = api.model('Team', {
    'title': fields.String(required=True, description='Team name'),
    #,'date_updated': fields.DateTime(dt_format='iso8601'),
    'date_updated': DateFormat()
})
team_post = api.model('Team', {
    'title': fields.String(required=True, description='Team name')
})
category_with_posts = api.inherit('Blog category with posts', team, {
    'posts': fields.List(fields.Nested(blog_post))
})
#m_date = rk.strptime("18012019","%d%m%Y").date()