from flask import Flask, request, jsonify
import config
from ext import db
from models.core import Article
from views.utils import ApiResult


class ApiFlask(Flask):

    def make_response(self, rv):
        if isinstance(rv, dict):
            rv = ApiResult(rv)
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


def create_app():
    app = ApiFlask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    return app


api = create_app()


@api.route('/articles', methods=['get'])
def articles():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 0, type=int)

    query = db.session.query
    if page_size != 0:
        articles_obj = query(Article).order_by(Article.article_id.desc()).offset(
            (page - 1) * page_size).limit(page_size).all()
    else:
        articles_dict = {}
        articles_obj = query(Article.tag, Article.title, Article.article_id,
                             Article.create_at, Article.brief).order_by(Article.article_id.desc()).all()
        for article in articles_obj:
            if article[0] in articles_dict.keys():
                articles_dict[article[0]].append(article)  
            else:
                articles_dict[article[0]] = list()
                articles_dict[article[0]].append(article)
        return {"articles": articles_dict}

    articles = [data.to_dict() for data in articles_obj]

    return {"articles": articles}


@api.route('/article/<int:article_id>', methods=['get'])
def article(article_id):
    query_obj = db.session.query(Article).filter(Article.article_id == article_id).first()
    article = query_obj.to_dict()

    return {'article': article}


@api.route('/tags', methods=['get'])
def article_tags():
    query_obj = db.session.query(Article.tag).order_by(Article.tag.asc()).distinct().all()
    tags = [data[0] for data in query_obj]

    return {'tags': tags}


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

