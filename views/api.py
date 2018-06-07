from flask import Flask, request, jsonify
import config
from ext import db
from models.core import Article


class ApiFlask(Flask):

    def make_response(self, rv):

        return Flask.make_response(self, rv)


def create_app():
    app = ApiFlask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    return app


api = create_app()


@api.route('/articles', methods=['get'])
def articles():
    print(request)
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 5, type=int)
    tag = request.args.get('tag', '', type=str)

    query = db.session.query
    if tag != '':
        articles_obj = query(Article).filter(Article.tag == tag).order_by(
            Article.article_id.desc()).offset((page - 1) * page_size).limit(page_size).all()
    else:
        articles_obj = query(Article).order_by(Article.article_id.desc()).offset(
            (page - 1) * page_size).limit(page_size).all()
    res = [data.to_dict() for data in articles_obj]

    return jsonify(res)


@api.route('/article/<int:article_id>', methods=['get'])
def article(article_id):
    query_obj = db.session.query(Article).filter(Article.article_id == article_id).first()
    res = query_obj.to_dict()

    return jsonify(res)


@api.route('/article/tags', methods=['get'])
def article_tags():
    query_obj = db.session.query(Article.tag).distinct().all()
    res = [data[0] for data in query_obj]

    return jsonify(res)


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

